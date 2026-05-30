# ============================================================
#
#  What this code does:
#  1. Loads the cleaned dataset into a SQLite database
#  2. Runs 10 SQL queries covering:
#       SELECT, WHERE, GROUP BY, ORDER BY,
#       HAVING, COUNT, SUM, AVG, MIN, MAX,
#       Subqueries, SUBSTR(), WHERE IN
#  3. Prints every query + its results
#  4. Saves all results to Excel (one sheet per query)
#
#  Run:  python project3_sql_analysis.py
# ============================================================

import pandas as pd
import sqlite3
from datetime import datetime
print("=" * 60)
print("  PROJECT 3: SQL Data Analysis")
print("=" * 60)

# ── STEP 0: Load dataset & create SQLite database ────────────
df = pd.read_excel("DecodeLabs_Cleaned_Dataset_P1.xlsx")
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
df["Date"]       = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")

# Connect to an in-memory SQLite database
conn = sqlite3.connect(":memory:")   # ':memory:' = no file saved to disk

# Load the dataframe as a SQL table named 'orders'
df.to_sql("orders", conn, if_exists="replace", index=False)
print(f"\n✓ Database created: table 'orders' with {len(df)} rows")
print(f"  Columns: {list(df.columns)}")

# ── Helper function: run query, print results, return df ─────
def run_query(query_num, title, sql):
    """Executes a SQL query and prints nicely formatted results."""
    print(f"\n{'='*60}")
    print(f"  {query_num}: {title}")
    print(f"{'='*60}")
    print(f"\n  SQL:\n")
    for line in sql.strip().split("\n"):
        print(f"    {line}")
    result = pd.read_sql_query(sql, conn)
    print(f"\n  RESULT ({len(result)} rows):\n")
    print(result.to_string(index=False))
    return result

# ── QUERY 1: Overall Business Summary ────────────────────────
# Clauses: SELECT, COUNT, SUM, AVG, MIN, MAX, DISTINCT

q1_result = run_query("Q1", "Overall Business Summary",
"""
SELECT
    COUNT(*)                        AS Total_Orders,
    ROUND(SUM(TotalPrice), 2)       AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value,
    ROUND(MIN(TotalPrice), 2)       AS Min_Order,
    ROUND(MAX(TotalPrice), 2)       AS Max_Order,
    COUNT(DISTINCT CustomerID)      AS Unique_Customers
FROM orders
""")

# ── QUERY 2: Revenue by Product ──────────────────────────────
# Clauses: SELECT, GROUP BY, ORDER BY, SUM, AVG

q2_result = run_query("Q2", "Revenue & Orders by Product",
"""
SELECT
    Product,
    COUNT(*)                        AS Total_Orders,
    ROUND(SUM(TotalPrice), 2)       AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value,
    ROUND(AVG(UnitPrice), 2)        AS Avg_Unit_Price
FROM orders
GROUP BY Product
ORDER BY Total_Revenue DESC
""")

# ── QUERY 3: Orders by Status ─────────────────────────────────
# Clauses: SELECT, GROUP BY, COUNT, SUM, Subquery for percentage

q3_result = run_query("Q3", "Order Count & Revenue by Status",
"""
SELECT
    OrderStatus,
    COUNT(*)                                                    AS Order_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 1) AS Pct_of_Total,
    ROUND(SUM(TotalPrice), 2)                                   AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)                                   AS Avg_Order_Value
FROM orders
GROUP BY OrderStatus
ORDER BY Order_Count DESC
""")

# ── QUERY 4: Revenue by Payment Method ───────────────────────
# Clauses: SELECT, GROUP BY, SUM, AVG, ORDER BY

q4_result = run_query("Q4", "Revenue by Payment Method",
"""
SELECT
    PaymentMethod,
    COUNT(*)                        AS Orders,
    ROUND(SUM(TotalPrice), 2)       AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value
FROM orders
GROUP BY PaymentMethod
ORDER BY Total_Revenue DESC
""")

# ── QUERY 5: Revenue by Referral Source ──────────────────────
# Clauses: SELECT, GROUP BY, COUNT, SUM, AVG, ORDER BY

q5_result = run_query("Q5", "Revenue by Referral Source",
"""
SELECT
    ReferralSource,
    COUNT(*)                        AS Orders,
    ROUND(SUM(TotalPrice), 2)       AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value
FROM orders
GROUP BY ReferralSource
ORDER BY Total_Revenue DESC
""")

# ── QUERY 6: High-Value Orders > $2,000 ──────────────────────
# Clauses: SELECT, WHERE, ORDER BY, LIMIT

q6_result = run_query("Q6", "High-Value Orders Above $2,000",
"""
SELECT
    OrderID,
    CustomerID,
    Product,
    Quantity,
    ROUND(UnitPrice, 2)             AS UnitPrice,
    ROUND(TotalPrice, 2)            AS TotalPrice,
    OrderStatus,
    PaymentMethod
FROM orders
WHERE TotalPrice > 2000
ORDER BY TotalPrice DESC
LIMIT 20
""")

# ── QUERY 7: Delivered Orders Only ────────────────────────────
# Clauses: SELECT, WHERE, GROUP BY, SUM, AVG, ORDER BY

q7_result = run_query("Q7", "Confirmed Revenue — Delivered Orders by Product",
"""
SELECT
    Product,
    COUNT(*)                        AS Delivered_Orders,
    ROUND(SUM(TotalPrice), 2)       AS Confirmed_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value
FROM orders
WHERE OrderStatus = 'Delivered'
GROUP BY Product
ORDER BY Confirmed_Revenue DESC
""")

# ── QUERY 8: Coupon Code Performance ─────────────────────────
# Clauses: SELECT, GROUP BY, HAVING (filters groups with < 50 orders)

q8_result = run_query("Q8", "Coupon Code Performance (HAVING filter)",
"""
SELECT
    CouponCode,
    COUNT(*)                        AS Orders,
    ROUND(SUM(TotalPrice), 2)       AS Total_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value
FROM orders
GROUP BY CouponCode
HAVING COUNT(*) > 50
ORDER BY Total_Revenue DESC
""")

# ── QUERY 9: Monthly Revenue Trend ───────────────────────────
# Clauses: SELECT, SUBSTR() to extract YYYY-MM from date, GROUP BY, SUM

q9_result = run_query("Q9", "Monthly Revenue Trend",
"""
SELECT
    SUBSTR(Date, 1, 7)              AS Year_Month,
    COUNT(*)                        AS Orders,
    ROUND(SUM(TotalPrice), 2)       AS Monthly_Revenue,
    ROUND(AVG(TotalPrice), 2)       AS Avg_Order_Value
FROM orders
GROUP BY SUBSTR(Date, 1, 7)
ORDER BY Year_Month
""")

# ── QUERY 10: Revenue at Risk (Cancelled + Returned) ─────────
# Clauses: SELECT, WHERE IN, GROUP BY, Subquery for percentage

q10_result = run_query("Q10", "Revenue at Risk — Cancelled & Returned by Product",
"""
SELECT
    Product,
    COUNT(*)                        AS Lost_Orders,
    ROUND(SUM(TotalPrice), 2)       AS Revenue_At_Risk,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM orders WHERE OrderStatus IN ('Cancelled','Returned')),
    1)                              AS Pct_of_Total_Losses
FROM orders
WHERE OrderStatus IN ('Cancelled', 'Returned')
GROUP BY Product
ORDER BY Revenue_At_Risk DESC
""")

# ── STEP 1: Close the database connection ────────────────────
conn.close()

# ── STEP 2: Save all results to Excel ────────────────────────
print("\n--- SAVING SQL RESULTS TO EXCEL ---")
output_file = "DecodeLabs_SQL_Analysis_P3.xlsx"
all_queries = {
    "Q1 Overall Summary"     : q1_result,
    "Q2 Revenue by Product"  : q2_result,
    "Q3 Orders by Status"    : q3_result,
    "Q4 Payment Method"      : q4_result,
    "Q5 Referral Source"     : q5_result,
    "Q6 High Value Orders"   : q6_result,
    "Q7 Delivered Orders"    : q7_result,
    "Q8 Coupon Performance"  : q8_result,
    "Q9 Monthly Revenue"     : q9_result,
    "Q10 Revenue at Risk"    : q10_result,
}
with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
    for sheet_name, result_df in all_queries.items():
        result_df.to_excel(writer, sheet_name=sheet_name, index=False)
print(f"✓ SQL Results saved → {output_file}")

# ── STEP 3: Final Key Insights ────────────────────────────────
print("\n" + "=" * 60)
print("  KEY SQL INSIGHTS")
print("=" * 60)
total_rev     = q1_result["Total_Revenue"].iloc[0]
total_orders  = q1_result["Total_Orders"].iloc[0]
top_product   = q2_result.iloc[0]["Product"]
top_product_r = q2_result.iloc[0]["Total_Revenue"]
cancel_pct    = q3_result[q3_result["OrderStatus"] == "Cancelled"]["Pct_of_Total"].values[0]
return_pct    = q3_result[q3_result["OrderStatus"] == "Returned"]["Pct_of_Total"].values[0]
top_referral  = q5_result.iloc[0]["ReferralSource"]
top_ref_rev   = q5_result.iloc[0]["Total_Revenue"]
best_month    = q9_result.loc[q9_result["Monthly_Revenue"].idxmax(), "Year_Month"]
best_rev      = q9_result["Monthly_Revenue"].max()
print(f"  Q1  Total Revenue        : ${total_rev:,.2f} from {total_orders} orders")
print(f"  Q2  Top Product          : {top_product} (${top_product_r:,.2f})")
print(f"  Q3  Cancellation Rate    : {cancel_pct}% | Return Rate: {return_pct}%")
print(f"  Q5  Best Marketing Ch.   : {top_referral} (${top_ref_rev:,.2f})")
print(f"  Q9  Peak Revenue Month   : {best_month} (${best_rev:,.2f})")
print(f"  Q10 Highest Risk Product : {q10_result.iloc[0]['Product']} "
      f"(${q10_result.iloc[0]['Revenue_At_Risk']:,.2f} at risk)")
print("=" * 60)
print("  SQL EXECUTION ORDER (how the DB reads it):")
print("  FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY")
print("=" * 60)
print("  PROJECT 3 COMPLETE ✅")
print("=" * 60)
