# ============================================================
#
#  What this code does:
#  Generates 10 professional charts covering:
#   C1  - Revenue by Product (Horizontal Bar)
#   C2  - Order Status Distribution (Donut)
#   C3  - Monthly Revenue Trend (Line)
#   C4  - Revenue by Referral Channel (Bar)
#   C5  - Avg Order Value by Payment Method (Bar)
#   C6  - Order Value Distribution (Histogram)
#   C7  - Orders & Revenue by Quantity (Dual-Axis)
#   C8  - Coupon Code Performance (Side-by-Side Bar)
#   C9  - Correlation Heatmap (Seaborn)
#   C10 - Order Status by Product (Stacked Bar)
#
#  Requirements: pip install pandas matplotlib seaborn openpyxl
#  Run: python project4_visualization.py
# ============================================================

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ── STEP 0: Load dataset ──────────────────────────────────────
print("=" * 60)
print("  PROJECT 4: Data Visualization")
print("=" * 60)
df = pd.read_excel("Dataset_for_Data_Analyticsp4.xlsx")
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')
df['Date']       = pd.to_datetime(df['Date'])
df['YearMonth']  = df['Date'].dt.to_period('M')
df['Year']       = df['Date'].dt.year
print(f"\n✓ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
# ── Colour palette ────────────────────────────────────────────
NAVY   = '#1F4E79'
TEAL   = '#00B0F0'
GREEN  = '#375623'
RED    = '#C00000'
AMBER  = '#FFC000'
ORANGE = '#E26B0A'
PURPLE = '#7030A0'
# Global matplotlib settings
plt.rcParams.update({
    'font.family'         : 'DejaVu Sans',
    'axes.spines.top'     : False,
    'axes.spines.right'   : False,
    'figure.facecolor'    : 'white',
})

# ── CHART 1: Revenue by Product (Horizontal Bar) ─────────────
print("\nGenerating C1: Revenue by Product...")
prod = df.groupby('Product')['TotalPrice'].sum().sort_values()
colors1 = [NAVY if v == prod.max() else TEAL for v in prod.values]
fig, ax = plt.subplots(figsize=(10, 5))
bars = ax.barh(prod.index, prod.values, color=colors1, edgecolor='white', height=0.6)
# Add value labels on bars
for bar, val in zip(bars, prod.values):
    ax.text(val + 2000, bar.get_y() + bar.get_height() / 2,
            f'${val:,.0f}', va='center', ha='left',
            fontsize=10, fontweight='bold', color=NAVY)
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.set_xlabel('Total Revenue ($)', fontsize=11, color='#444')
ax.set_title('Total Revenue by Product Category',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart1_revenue_by_product.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart1_revenue_by_product.png")

# ── CHART 2: Order Status Distribution (Donut) ───────────────
print("Generating C2: Order Status Donut...")
status_counts = df['OrderStatus'].value_counts()
colors2 = [RED, '#FF6B6B', AMBER, TEAL, GREEN]
fig, ax = plt.subplots(figsize=(8, 6))
wedges, texts, autotexts = ax.pie(
    status_counts.values,
    colors=colors2,
    autopct='%1.1f%%',
    startangle=90,
    pctdistance=0.75,
    wedgeprops=dict(width=0.5, edgecolor='white', linewidth=2)
)
for at in autotexts:
    at.set_fontsize(10)
    at.set_fontweight('bold')
    at.set_color('white')
legend_labels = [f'{s} ({c:,})' for s, c in zip(status_counts.index, status_counts.values)]
ax.legend(wedges, legend_labels, loc='lower center',
          bbox_to_anchor=(0.5, -0.08), ncol=3, fontsize=9, frameon=False)
ax.set_title('Order Status Distribution\n(1,200 Total Orders)',
             fontsize=14, fontweight='bold', color=NAVY, pad=20)
plt.tight_layout()
plt.savefig('chart2_order_status.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart2_order_status.png")

# ── CHART 3: Monthly Revenue Trend (Line) ────────────────────
print("Generating C3: Monthly Revenue Trend...")
monthly = df.groupby('YearMonth')['TotalPrice'].sum().reset_index()
monthly['YearMonth_str'] = monthly['YearMonth'].astype(str)
x = range(len(monthly))
fig, ax = plt.subplots(figsize=(14, 5))
ax.fill_between(x, monthly['TotalPrice'], alpha=0.15, color=TEAL)
ax.plot(x, monthly['TotalPrice'], color=NAVY, linewidth=2.5,
        marker='o', markersize=5, markerfacecolor=TEAL)
# Annotate the peak month
peak_idx = monthly['TotalPrice'].idxmax()
ax.annotate(
    f"Peak\n${monthly.loc[peak_idx, 'TotalPrice']:,.0f}",
    xy=(peak_idx, monthly.loc[peak_idx, 'TotalPrice']),
    xytext=(peak_idx - 2, monthly.loc[peak_idx, 'TotalPrice'] + 3000),
    arrowprops=dict(arrowstyle='->', color=RED, lw=1.5),
    fontsize=9, color=RED, fontweight='bold'
)
step = max(1, len(monthly) // 10)
ax.set_xticks(list(x)[::step])
ax.set_xticklabels(monthly['YearMonth_str'].tolist()[::step], rotation=45, ha='right', fontsize=9)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v/1000:.0f}K'))
ax.set_title('Monthly Revenue Trend (2023–2025)',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_ylabel('Revenue ($)', fontsize=11, color='#444')
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart3_monthly_trend.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart3_monthly_trend.png")

# ── CHART 4: Revenue by Referral Source (Bar) ────────────────
print("Generating C4: Revenue by Channel...")
ref = df.groupby('ReferralSource')['TotalPrice'].sum().sort_values(ascending=False)
colors4 = [NAVY, TEAL, ORANGE, AMBER, PURPLE]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(ref.index, ref.values, color=colors4, edgecolor='white', width=0.6)
for bar, val in zip(bars, ref.values):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 1500,
            f'${val:,.0f}', ha='center', va='bottom',
            fontsize=9, fontweight='bold', color=NAVY)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v/1000:.0f}K'))
ax.set_title('Total Revenue by Marketing Channel',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_ylabel('Total Revenue ($)', fontsize=11, color='#444')
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart4_referral_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart4_referral_revenue.png")

# ── CHART 5: Avg Order Value by Payment Method ───────────────
print("Generating C5: Avg Order by Payment...")
pay = df.groupby('PaymentMethod')['TotalPrice'].mean().sort_values(ascending=False)
overall_avg = df['TotalPrice'].mean()
colors5 = [GREEN if v == pay.max() else '#90EE90' for v in pay.values]
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(pay.index, pay.values, color=colors5, edgecolor='white', width=0.6)
# Reference line for overall average
ax.axhline(y=overall_avg, color=RED, linestyle='--', linewidth=1.5,
           label=f'Overall Avg: ${overall_avg:,.0f}')
for bar, val in zip(bars, pay.values):
    ax.text(bar.get_x() + bar.get_width() / 2, val + 8,
            f'${val:,.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax.set_title('Average Order Value by Payment Method',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_ylabel('Avg Order Value ($)', fontsize=11, color='#444')
ax.legend(fontsize=10, frameon=False)
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart5_payment_avg.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart5_payment_avg.png")

# ── CHART 6: TotalPrice Distribution (Histogram) ─────────────
print("Generating C6: Order Value Distribution...")
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(df['TotalPrice'], bins=40, color=TEAL, edgecolor='white', alpha=0.85)
ax.axvline(df['TotalPrice'].mean(),   color=RED,   linestyle='--', lw=2,
           label=f"Mean:   ${df['TotalPrice'].mean():,.0f}")
ax.axvline(df['TotalPrice'].median(), color=AMBER, linestyle='--', lw=2,
           label=f"Median: ${df['TotalPrice'].median():,.0f}")
ax.set_title('Distribution of Order Values (Right-Skewed)',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_xlabel('Total Order Value ($)', fontsize=11, color='#444')
ax.set_ylabel('Number of Orders',     fontsize=11, color='#444')
ax.legend(fontsize=10, frameon=False)
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart6_distribution.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart6_distribution.png")

# ── CHART 7: Revenue by Quantity (Dual-Axis Bar) ─────────────
print("Generating C7: Revenue by Quantity...")
qty = df.groupby('Quantity').agg(
    Orders  = ('OrderID',    'count'),
    Revenue = ('TotalPrice', 'sum')
).reset_index()
x_qty = np.arange(len(qty))
w = 0.4
fig, ax1 = plt.subplots(figsize=(9, 5))
ax2 = ax1.twinx()
ax1.bar(x_qty - w/2, qty['Orders'],  width=w, color=TEAL, label='Orders',       alpha=0.9)
ax2.bar(x_qty + w/2, qty['Revenue'], width=w, color=NAVY, label='Revenue ($)',   alpha=0.9)
ax1.set_xticks(x_qty)
ax1.set_xticklabels([f'Qty {q}' for q in qty['Quantity']])
ax1.set_ylabel('Number of Orders', color=TEAL, fontsize=10)
ax2.set_ylabel('Total Revenue ($)', color=NAVY, fontsize=10)
ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v/1000:.0f}K'))
ax1.set_title('Orders & Revenue by Quantity Ordered',
              fontsize=14, fontweight='bold', color=NAVY, pad=15)
legend_handles = [mpatches.Patch(color=TEAL, label='Order Count'),
                  mpatches.Patch(color=NAVY, label='Total Revenue')]
ax1.legend(handles=legend_handles, fontsize=9, frameon=False, loc='upper left')
ax1.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart7_qty_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart7_qty_revenue.png")

# ── CHART 8: Coupon Code Performance (Side-by-Side) ──────────
print("Generating C8: Coupon Performance...")
coup = df.groupby('CouponCode')['TotalPrice'].agg(['sum','mean','count']).reset_index()
coup.columns = ['CouponCode','TotalRevenue','AvgOrder','Orders']
coup = coup.sort_values('TotalRevenue', ascending=False)
colors8 = [NAVY, TEAL, ORANGE, AMBER]
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
# Left: Total Revenue
bars = axes[0].bar(coup['CouponCode'], coup['TotalRevenue'],
                   color=colors8[:len(coup)], edgecolor='white')
for bar, val in zip(bars, coup['TotalRevenue']):
    axes[0].text(bar.get_x() + bar.get_width()/2, val + 2000,
                 f'${val/1000:.0f}K', ha='center', va='bottom',
                 fontsize=9, fontweight='bold')
axes[0].yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${v/1000:.0f}K'))
axes[0].set_title('Total Revenue by Coupon', fontsize=12, fontweight='bold', color=NAVY)
axes[0].set_ylabel('Revenue ($)', fontsize=10)
axes[0].set_facecolor('#F8F9FA')
# Right: Avg Order Value
bars2 = axes[1].bar(coup['CouponCode'], coup['AvgOrder'],
                    color=colors8[:len(coup)], edgecolor='white')
for bar, val in zip(bars2, coup['AvgOrder']):
    axes[1].text(bar.get_x() + bar.get_width()/2, val + 5,
                 f'${val:,.0f}', ha='center', va='bottom',
                 fontsize=9, fontweight='bold')
axes[1].set_title('Avg Order Value by Coupon', fontsize=12, fontweight='bold', color=NAVY)
axes[1].set_ylabel('Avg Order ($)', fontsize=10)
axes[1].set_facecolor('#F8F9FA')
fig.suptitle('Coupon Code Performance Analysis',
             fontsize=14, fontweight='bold', color=NAVY, y=1.01)
plt.tight_layout()
plt.savefig('chart8_coupon.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart8_coupon.png")

# ── CHART 9: Correlation Heatmap (Seaborn) ───────────────────
print("Generating C9: Correlation Heatmap...")
corr = df[['Quantity','UnitPrice','ItemsInCart','TotalPrice']].corr()
fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(
    corr, annot=True, fmt='.3f', cmap='coolwarm',
    center=0, linewidths=0.5, linecolor='white', ax=ax,
    square=True, annot_kws={'size': 11, 'weight': 'bold'},
    vmin=-1, vmax=1
)
ax.set_title('Correlation Heatmap (Pearson r)',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.tick_params(labelsize=10)
plt.tight_layout()
plt.savefig('chart9_correlation.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart9_correlation.png")

# ── CHART 10: Product × Status Stacked Bar ───────────────────
print("Generating C10: Product × Status...")
ct = pd.crosstab(df['Product'], df['OrderStatus'])
ct = ct[['Delivered','Shipped','Pending','Returned','Cancelled']]
colors10 = [GREEN, TEAL, AMBER, ORANGE, RED]
fig, ax = plt.subplots(figsize=(12, 5))
ct.plot(kind='bar', stacked=True, color=colors10,
        edgecolor='white', width=0.65, ax=ax, linewidth=0.5)
ax.set_title('Order Status Breakdown by Product Category',
             fontsize=14, fontweight='bold', color=NAVY, pad=15)
ax.set_xlabel('Product', fontsize=11, color='#444')
ax.set_ylabel('Number of Orders', fontsize=11, color='#444')
ax.legend(title='Order Status', bbox_to_anchor=(1.01, 1),
          loc='upper left', fontsize=9, frameon=False)
ax.tick_params(axis='x', rotation=0)
ax.set_facecolor('#F8F9FA')
plt.tight_layout()
plt.savefig('chart10_product_status.png', dpi=150, bbox_inches='tight')
plt.close()
print("  ✓ chart10_product_status.png")

# ── STEP final: Summary ───────────────────────────────────────
print("\n" + "=" * 60)
print("  KEY VISUAL INSIGHTS")
print("=" * 60)
prod_rev = df.groupby('Product')['TotalPrice'].sum()
ref_rev  = df.groupby('ReferralSource')['TotalPrice'].sum()
pay_avg  = df.groupby('PaymentMethod')['TotalPrice'].mean()
monthly_r = df.groupby('YearMonth')['TotalPrice'].sum()
lost_pct = len(df[df['OrderStatus'].isin(['Cancelled','Returned'])]) / len(df) * 100
print(f"  Top Product (Revenue)  : {prod_rev.idxmax()} (${prod_rev.max():,.0f})")
print(f"  Top Channel            : {ref_rev.idxmax()} (${ref_rev.max():,.0f})")
print(f"  Best Payment (Avg)     : {pay_avg.idxmax()} (${pay_avg.max():,.0f} avg)")
print(f"  Peak Revenue Month     : {monthly_r.idxmax()} (${monthly_r.max():,.0f})")
print(f"  Order Value Skewness   : {df['TotalPrice'].skew():.3f} (right-skewed)")
print(f"  Loss Rate (C+R)        : {lost_pct:.1f}% of all orders")
print(f"  Strongest Correlation  : UnitPrice↔TotalPrice r="
      f"{df[['UnitPrice','TotalPrice']].corr().iloc[0,1]:.3f}")
print("=" * 60)
print("  10/10 charts saved as PNG files ✅")
print("  PROJECT 4 COMPLETE ✅")
print("=" * 60)
