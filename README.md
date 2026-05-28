# 📊 DecodeLabs Data Analytics Internship
### Batch 2026 | Industrial Training Projects

![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20Python%20%7C%20SQL-orange)

---

## 🚀 About This Repository

This repository contains all 3 Data Analytics projects completed during my
industrial internship at **DecodeLabs (Batch 2026)**. Each project builds on
the previous one — from raw data to clean data to insights to SQL queries.

---

## 📁 Project Structure

| Project | Title | Key Skills | Status |
|---------|-------|------------|--------|
| Project 1 | Data Cleaning & Preparation | Excel, Python, Pandas | ✅ Completed |
| Project 2 | Exploratory Data Analysis (EDA) | Statistics, EDA, Visualization | ✅ Completed |
| Project 3 | SQL Data Analysis | SQL, SQLite, Aggregations | ✅ Completed |

---

## 🧹 Project 1 — Data Cleaning & Preparation

**Goal:** Clean a raw 1,200-row e-commerce dataset by handling missing values,
duplicates, and incorrect formats.

### What I Did
- ✅ Fixed **1,200 date values** — stripped time component to YYYY-MM-DD (ISO 8601)
- ✅ Imputed **309 missing CouponCode** values with 'No Coupon' (preserved all records)
- ✅ Standardised **PaymentMethod** label — 'Online' → 'Online Payment'
- ✅ Enforced **2-decimal precision** on all monetary columns

### Verification Gate (Passed ✅)
- 0 duplicate OrderIDs
- 0 null values remaining
- TotalPrice = Qty × UnitPrice verified for all 1,200 rows

### Files
- `DecodeLabs_Cleaned_Dataset.xlsx` — Production-ready cleaned data
- `DecodeLabs_Change_Log.xlsx` — Full documentation of all 4 changes

---

## 📈 Project 2 — Exploratory Data Analysis (EDA)

**Goal:** Analyze the dataset to uncover patterns, trends, and outliers using
descriptive statistics and segmentation.

### Key Findings
- 📌 **41.4% cancellation/return rate** — $519,674 revenue at risk
- 📌 **Only 19.3% of orders are Delivered** — $242,600 confirmed revenue
- 📌 **UnitPrice is the strongest revenue driver** (Pearson r = 0.717)
- 📌 **Instagram is the top marketing channel** — $275,285 total revenue
- 📌 **TotalPrice is right-skewed** (skew = 0.891) — median is better measure
- 📌 **8 high-value outliers** detected above $3,330 IQR upper fence

### Techniques Used
- Five-number summary (Min, Q1, Median, Q3, Max)
- IQR outlier detection
- Pearson correlation analysis
- Monthly revenue trend analysis
- Segmentation by Product, Payment, Referral, Coupon, Status

### File
- `DecodeLabs_EDA_Report_P2.xlsx` — 7-sheet EDA report

---

## 🗄️ Project 3 — SQL Data Analysis

**Goal:** Write SQL queries to extract business intelligence from the orders
database using SELECT, WHERE, GROUP BY, HAVING, ORDER BY, and aggregations.

### Queries Written

| # | Query | Clauses Used |
|---|-------|-------------|
| Q1 | Overall Business Summary | COUNT, SUM, AVG, MIN, MAX |
| Q2 | Revenue by Product | GROUP BY, ORDER BY |
| Q3 | Orders by Status | GROUP BY, COUNT, Subquery |
| Q4 | Revenue by Payment Method | GROUP BY, SUM, AVG |
| Q5 | Revenue by Referral Source | GROUP BY, ORDER BY |
| Q6 | High-Value Orders > $2,000 | WHERE, ORDER BY |
| Q7 | Delivered Orders Only | WHERE, GROUP BY |
| Q8 | Coupon Code Performance | GROUP BY, HAVING |
| Q9 | Monthly Revenue Trend | SUBSTR(), GROUP BY |
| Q10 | Revenue at Risk (Lost Orders) | WHERE IN, GROUP BY, Subquery |

### File
- `DecodeLabs_SQL_Analysis_P3.xlsx` — 12-sheet SQL report + cheat sheet

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)

---

## 📬 Connect With Me

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/kandunuri-gayathri-28a636342?utm_source=share_via&utm_content=profile&utm_medium=member_android) 🤝

---
*Industrial Training Kit | Batch 2026 | Powered by DecodeLabs*
