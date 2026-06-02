# ============================================================
#
#  What this code does:
#  1. Loads the cleaned dataset from Project 1
#  2. Descriptive statistics — mean, median, std, skewness
#  3. Distribution analysis — five-number summary
#  4. Outlier detection — IQR method
#  5. Trend analysis — monthly & yearly revenue
#  6. Segmentation — by product, status, payment, referral, coupon
#  7. Correlation analysis — Pearson r
#  8. Saves full EDA Report as Excel (7 sheets)
#
#  Run:  python project2_eda.py
# ============================================================

import pandas as pd
import numpy as np
from datetime import datetime
print("=" * 60)
print("  PROJECT 2: Exploratory Data Analysis (EDA)")
print("=" * 60)

# ── STEP 0: Load cleaned dataset ─────────────────────────────
df = pd.read_excel("DecodeLabs_Cleaned_Dataset_P1.xlsx")
# Convert types properly
df["Date"]       = pd.to_datetime(df["Date"])
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
# Create helper columns
df["Year"]      = df["Date"].dt.year
df["Month"]     = df["Date"].dt.month
df["YearMonth"] = df["Date"].dt.to_period("M")
print(f"\n✓ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")

# ── STEP 1: Descriptive Statistics ───────────────────────────
print("\n--- STEP 1: DESCRIPTIVE STATISTICS ---")
numeric_cols = ["TotalPrice", "UnitPrice", "Quantity", "ItemsInCart"]
stats = {}
for col in numeric_cols:
    stats[col] = {
        "Count"   : df[col].count(),
        "Mean"    : round(df[col].mean(),   2),
        "Median"  : round(df[col].median(), 2),
        "Std Dev" : round(df[col].std(),    2),
        "Min"     : round(df[col].min(),    2),
        "Q1"      : round(df[col].quantile(0.25), 2),
        "Q3"      : round(df[col].quantile(0.75), 2),
        "Max"     : round(df[col].max(),    2),
        "IQR"     : round(df[col].quantile(0.75) - df[col].quantile(0.25), 2),
        "Skewness": round(df[col].skew(),   3),
    }
    print(f"\n  {col}:")
    for k, v in stats[col].items():
        print(f"    {k:<12}: {v}")
# Key interpretation
print("\n  INTERPRETATION:")
print(f"  TotalPrice skew = {stats['TotalPrice']['Skewness']} → RIGHT-SKEWED")
print(f"  Mean ({stats['TotalPrice']['Mean']}) > Median ({stats['TotalPrice']['Median']}) → use Median as centre")
print(f"  UnitPrice skew  = {stats['UnitPrice']['Skewness']} → nearly symmetric")
df_stats = pd.DataFrame(stats).T.reset_index()
df_stats.columns = ["Column"] + list(list(stats.values())[0].keys())

# ── STEP 2: Outlier Detection (IQR Method) ───────────────────
print("\n--- STEP 2: OUTLIER DETECTION (IQR METHOD) ---")
Q1  = df["TotalPrice"].quantile(0.25)
Q3  = df["TotalPrice"].quantile(0.75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR
outliers = df[
    (df["TotalPrice"] < lower_fence) |
    (df["TotalPrice"] > upper_fence)
].copy()
print(f"\n  Q1             = ${Q1:,.2f}")
print(f"  Q3             = ${Q3:,.2f}")
print(f"  IQR            = ${IQR:,.2f}")
print(f"  Lower fence    = ${lower_fence:,.2f}")
print(f"  Upper fence    = ${upper_fence:,.2f}")
print(f"  Outliers found = {len(outliers)} orders")
print(f"\n  Top 5 outliers:")
print(outliers.nlargest(5, "TotalPrice")[
    ["OrderID", "Product", "Quantity", "UnitPrice", "TotalPrice", "OrderStatus"]
].to_string(index=False))

# ── STEP 3: Revenue by Product ────────────────────────────────
print("\n--- STEP 3: REVENUE BY PRODUCT ---")
product_stats = df.groupby("Product").agg(
    Orders        = ("OrderID",    "count"),
    Total_Revenue = ("TotalPrice", "sum"),
    Avg_Order     = ("TotalPrice", "mean"),
    Avg_UnitPrice = ("UnitPrice",  "mean"),
).round(2).sort_values("Total_Revenue", ascending=False).reset_index()
print(product_stats.to_string(index=False))

# ── STEP 4: Order Status Analysis ────────────────────────────
print("\n--- STEP 4: ORDER STATUS ANALYSIS ---")
status_stats = df.groupby("OrderStatus").agg(
    Count   = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    Avg     = ("TotalPrice", "mean"),
).round(2).reset_index()
status_stats["Pct"] = (status_stats["Count"] / len(df) * 100).round(1)
print(status_stats.to_string(index=False))
# Calculate loss metrics
lost_orders  = df[df["OrderStatus"].isin(["Cancelled", "Returned"])]
lost_revenue = lost_orders["TotalPrice"].sum()
lost_pct     = len(lost_orders) / len(df) * 100
print(f"\n  ⚠️  CRITICAL: {len(lost_orders)} orders ({lost_pct:.1f}%) cancelled/returned")
print(f"  Revenue at risk: ${lost_revenue:,.2f}")

# ── STEP 5: Revenue by Referral Source ───────────────────────
print("\n--- STEP 5: REFERRAL SOURCE ANALYSIS ---")
referral_stats = df.groupby("ReferralSource").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    Avg     = ("TotalPrice", "mean"),
).round(2).sort_values("Revenue", ascending=False).reset_index()
print(referral_stats.to_string(index=False))

# ── STEP 6: Revenue by Payment Method ────────────────────────
print("\n--- STEP 6: PAYMENT METHOD ANALYSIS ---")
payment_stats = df.groupby("PaymentMethod").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    Avg     = ("TotalPrice", "mean"),
).round(2).sort_values("Revenue", ascending=False).reset_index()
print(payment_stats.to_string(index=False))

# ── STEP 7: Coupon Code Analysis ─────────────────────────────
print("\n--- STEP 7: COUPON CODE ANALYSIS ---")
coupon_stats = df.groupby("CouponCode").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    Avg     = ("TotalPrice", "mean"),
).round(2).sort_values("Revenue", ascending=False).reset_index()
print(coupon_stats.to_string(index=False))

# ── STEP 8: Monthly Revenue Trend ────────────────────────────
print("\n--- STEP 8: MONTHLY REVENUE TREND ---")
monthly = df.groupby("YearMonth")["TotalPrice"].agg(
    Orders  = "count",
    Revenue = "sum",
    Avg     = "mean",
).round(2).reset_index()
monthly["YearMonth"] = monthly["YearMonth"].astype(str)
best_month  = monthly.loc[monthly["Revenue"].idxmax()]
worst_month = monthly.loc[monthly["Revenue"].idxmin()]
print(f"\n  Best month  : {best_month['YearMonth']}  ${best_month['Revenue']:,.2f}")
print(f"  Worst month : {worst_month['YearMonth']} ${worst_month['Revenue']:,.2f}")
print(f"\n  {monthly[['YearMonth','Orders','Revenue','Avg']].to_string(index=False)}")

# ── STEP 9: Correlation Analysis ─────────────────────────────
print("\n--- STEP 9: CORRELATION ANALYSIS (Pearson r) ---")
corr = df[["Quantity", "UnitPrice", "ItemsInCart", "TotalPrice"]].corr().round(3)
print(corr)
print("\n  INTERPRETATIONS:")
corr_interpretations = [
    ("UnitPrice  ↔ TotalPrice",  corr.loc["UnitPrice",  "TotalPrice"], "Higher price = stronger revenue driver"),
    ("Quantity   ↔ TotalPrice",  corr.loc["Quantity",   "TotalPrice"], "More units = higher order value"),
    ("ItemsInCart↔ TotalPrice",  corr.loc["ItemsInCart","TotalPrice"], "Larger cart = moderate revenue effect"),
    ("UnitPrice  ↔ Quantity",    corr.loc["UnitPrice",  "Quantity"],   "Price does not influence qty ordered"),
]
for pair, r, note in corr_interpretations:
    strength = "STRONG" if abs(r) >= 0.6 else ("MODERATE" if abs(r) >= 0.3 else "WEAK")
    print(f"  {pair} : r={r:>6.3f}  [{strength}] — {note}")

# ── STEP 10: Revenue by Quantity ─────────────────────────────
print("\n--- STEP 10: REVENUE BY QUANTITY ---")
qty_stats = df.groupby("Quantity").agg(
    Orders  = ("OrderID",    "count"),
    Revenue = ("TotalPrice", "sum"),
    Avg     = ("TotalPrice", "mean"),
).round(2).reset_index()
print(qty_stats.to_string(index=False))

# ── STEP 11: Save EDA Report to Excel (7 sheets) ─────────────
print("\n--- SAVING EDA REPORT ---")
output_file = "DecodeLabs_EDA_Report_P2.xlsx"
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:

    # Sheet 1: Descriptive Statistics
    df_stats.to_excel(writer, sheet_name="Descriptive Statistics", index=False)

    # Sheet 2: Product Analysis
    product_stats.to_excel(writer, sheet_name="Product Analysis", index=False)

    # Sheet 3: Order Status
    status_stats.to_excel(writer, sheet_name="Order Status", index=False)

    # Sheet 4: Referral & Payment
    referral_stats.to_excel(writer, sheet_name="Referral & Payment", index=False)
    payment_stats.to_excel(
        writer, sheet_name="Referral & Payment",
        index=False, startrow=len(referral_stats) + 3
    )

    # Sheet 5: Coupon Analysis
    coupon_stats.to_excel(writer, sheet_name="Coupon Analysis", index=False)

    # Sheet 6: Monthly Revenue
    monthly.to_excel(writer, sheet_name="Revenue Trends", index=False)

    # Sheet 7: Correlation Matrix
    corr.to_excel(writer, sheet_name="Correlation Analysis")

    # Sheet 8: Outliers
    outliers[["OrderID","Product","Quantity","UnitPrice","TotalPrice","OrderStatus"]]\
        .sort_values("TotalPrice", ascending=False)\
        .to_excel(writer, sheet_name="Outlier Analysis", index=False)
print(f"✓ EDA Report saved → {output_file}")

# ── STEP 12: Final Summary ────────────────────────────────────
print("\n" + "=" * 60)
print("  KEY FINDINGS SUMMARY")
print("=" * 60)
print(f"  Total Orders           : {len(df):,}")
print(f"  Total Revenue          : ${df['TotalPrice'].sum():,.2f}")
print(f"  Avg Order Value (Mean) : ${df['TotalPrice'].mean():,.2f}")
print(f"  Avg Order Value (Med)  : ${df['TotalPrice'].median():,.2f}")
print(f"  TotalPrice Skewness    : {df['TotalPrice'].skew():.3f} (right-skewed)")
print(f"  Cancellation+Return %  : {lost_pct:.1f}%")
print(f"  Revenue at Risk        : ${lost_revenue:,.2f}")
print(f"  Top Referral Channel   : Instagram (${referral_stats.iloc[0]['Revenue']:,.2f})")
print(f"  Outliers Detected      : {len(outliers)} orders above ${upper_fence:,.2f}")
print(f"  Strongest Correlation  : UnitPrice↔TotalPrice (r={corr.loc['UnitPrice','TotalPrice']:.3f})")
print("=" * 60)
print("  PROJECT 2 COMPLETE ✅")
print("=" * 60)
