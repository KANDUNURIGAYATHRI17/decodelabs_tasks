# ============================================================
#
#  What this code does:
#  1. Loads the raw dataset
#  2. Audits every column for issues
#  3. Fixes: date format, missing CouponCode,
#            PaymentMethod label, numeric precision
#  4. Verifies the cleaned data (0 duplicates, 0 nulls)
#  5. Saves: Cleaned Dataset + Change Log as Excel files
#
#  Run:  python project1_data_cleaning.py
# ============================================================

import pandas as pd
import numpy as np
from datetime import datetime

# ── STEP 0: Load the raw dataset ─────────────────────────────
print("=" * 60)
print("  PROJECT 1: Data Cleaning & Preparation")
print("=" * 60)
df_raw = pd.read_excel("Dataset_for_Data_Analytics.xlsx", dtype=str)
df = df_raw.copy()          # always work on a copy, keep original safe
print(f"\n✓ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"  Columns: {list(df.columns)}")

# ── STEP 1: Initial Audit ─────────────────────────────────────
print("\n--- INITIAL AUDIT ---")
print("Null counts per column:")
print(df.isnull().sum())
print("\nDuplicate OrderIDs:", df.duplicated("OrderID").sum())
print("Sample dates (raw):", df["Date"].head(3).tolist())
print("PaymentMethod values:", df["PaymentMethod"].unique().tolist())

# ── STEP 2: Track every change in a changelog list ───────────
changelog = []          # list of dicts — one per change record

# ── FIX 1: Date Format ───────────────────────────────────────
# Problem : All 1,200 dates contain '00:00:00' time suffix
#           e.g. '2023-01-04 00:00:00'  →  should be '2023-01-04'
# Action  : Convert to datetime then format as YYYY-MM-DD (ISO 8601)
bad_date_count = df["Date"].str.contains("00:00:00", na=False).sum()
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
print(f"\n✓ FIX 1 — Date format: {bad_date_count} dates cleaned")
changelog.append({
    "Change ID"       : "CR001",
    "Column Affected" : "Date",
    "Issue"           : f"All {bad_date_count} date values contained a '00:00:00' "
                        f"time suffix, violating ISO 8601 date-only format.",
    "Action Taken"    : "Stripped time component; standardised all values to YYYY-MM-DD.",
    "Impact"          : f"{bad_date_count} records corrected",
    "Method"          : "Format Standardisation",
    "Status"          : "Resolved",
})

# ── FIX 2: Missing CouponCode ─────────────────────────────────
# Problem : 309 rows have NaN in CouponCode — orders without a coupon
# Action  : Fill NaN with 'No Coupon' so the column is fully queryable
#           (Do NOT delete rows — that would reduce statistical power)
missing_coupon = df["CouponCode"].isna().sum()
df["CouponCode"] = df["CouponCode"].fillna("No Coupon")
print(f"✓ FIX 2 — CouponCode: {missing_coupon} missing values imputed")
changelog.append({
    "Change ID"       : "CR002",
    "Column Affected" : "CouponCode",
    "Issue"           : f"{missing_coupon} rows (25.75%) had blank CouponCode — "
                        f"orders placed without a discount code.",
    "Action Taken"    : "Imputed missing values with 'No Coupon' to preserve all records.",
    "Impact"          : f"{missing_coupon} records preserved (row deletion avoided)",
    "Method"          : "Strategic Imputation",
    "Status"          : "Resolved",
})

# ── FIX 3: PaymentMethod label ────────────────────────────────
# Problem : 'Online' appears 258 times — inconsistent naming convention
#           All other values use two words: 'Credit Card', 'Debit Card' etc.
# Action  : Rename 'Online' → 'Online Payment'
online_count = (df["PaymentMethod"] == "Online").sum()
df["PaymentMethod"] = df["PaymentMethod"].replace("Online", "Online Payment")
print(f"✓ FIX 3 — PaymentMethod: {online_count} 'Online' → 'Online Payment'")
changelog.append({
    "Change ID"       : "CR003",
    "Column Affected" : "PaymentMethod",
    "Issue"           : f"'Online' appeared {online_count} times — inconsistent with "
                        f"two-word naming convention used by all other payment methods.",
    "Action Taken"    : "Renamed 'Online' to 'Online Payment'.",
    "Impact"          : f"{online_count} records standardised",
    "Method"          : "Format Standardisation (Naming Convention)",
    "Status"          : "Resolved",
})

# ── FIX 4: Numeric Precision ──────────────────────────────────
# Problem : Some monetary values lack consistent decimal places
#           e.g. '224' instead of '224.00'
# Action  : Convert to float and round to 2 decimal places
df["UnitPrice"]  = pd.to_numeric(df["UnitPrice"]).round(2)
df["TotalPrice"] = pd.to_numeric(df["TotalPrice"]).round(2)
print(f"✓ FIX 4 — Numeric precision: UnitPrice & TotalPrice rounded to 2dp")
changelog.append({
    "Change ID"       : "CR004",
    "Column Affected" : "UnitPrice, TotalPrice",
    "Issue"           : "Some monetary values had inconsistent decimal precision "
                        "(e.g. '224' instead of '224.00').",
    "Action Taken"    : "Enforced 2-decimal-place precision on all monetary columns.",
    "Impact"          : "All 1,200 records now have consistent numeric precision",
    "Method"          : "Numeric Precision Standardisation",
    "Status"          : "Resolved",
})

# ── STEP 3: Verification Gate ─────────────────────────────────
print("\n--- VERIFICATION GATE ---")
dup_count  = df.duplicated("OrderID").sum()
null_count = df.isnull().sum().sum()
# Verify TotalPrice = Quantity × UnitPrice
df_check = df.copy()
df_check["Quantity"]   = pd.to_numeric(df_check["Quantity"])
df_check["UnitPrice"]  = pd.to_numeric(df_check["UnitPrice"])
df_check["TotalPrice"] = pd.to_numeric(df_check["TotalPrice"])
df_check["Expected"]   = (df_check["Quantity"] * df_check["UnitPrice"]).round(2)
price_errors = (abs(df_check["Expected"] - df_check["TotalPrice"]) > 0.05).sum()
print(f"  Duplicate OrderIDs  : {dup_count}   ← must be 0")
print(f"  Null values remaining: {null_count}  ← must be 0")
print(f"  TotalPrice errors   : {price_errors}  ← must be 0")
assert dup_count  == 0, "❌ FAILED: Duplicates found!"
assert null_count == 0, "❌ FAILED: Null values remain!"
assert price_errors == 0, "❌ FAILED: TotalPrice mismatch!"
print("\n✅ All verification checks PASSED — dataset is production-ready")

# ── STEP 4: Save Cleaned Dataset ─────────────────────────────
output_cleaned = "DecodeLabs_Cleaned_Dataset_P1.xlsx"
df.to_excel(output_cleaned, index=False, sheet_name="Cleaned Data")
print(f"\n✓ Cleaned dataset saved → {output_cleaned}")

# ── STEP 5: Save Change Log ───────────────────────────────────
output_log = "DecodeLabs_Change_Log.xlsx"
df_log = pd.DataFrame(changelog)
df_log.to_excel(output_log, index=False, sheet_name="Change Log")
print(f"✓ Change log saved    → {output_log}")

# ── STEP 6: Summary Report ────────────────────────────────────
print("\n" + "=" * 60)
print("  SUMMARY")
print("=" * 60)
print(f"  Total rows     : {len(df)}")
print(f"  Total columns  : {len(df.columns)}")
print(f"  Changes made   : {len(changelog)}")
print(f"  Change IDs     : {', '.join(c['Change ID'] for c in changelog)}")
print("=" * 60)
print("  PROJECT 1 COMPLETE ✅")
print("=" * 60)
