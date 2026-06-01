# 📊 DecodeLabs Data Analytics Internship
### Batch 2026 | Industrial Training Projects

![Data Analytics](https://img.shields.io/badge/Domain-Data%20Analytics-blue)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20Python%20%7C%20SQL%20%7C%20Power%20BI-orange)

---

## 🚀 About This Repository

This repository contains all 4 Data Analytics projects completed during my
industrial internship at **DecodeLabs (Batch 2026)**. Each project builds on
the previous one — from raw data to clean data to insights to SQL queries to
interactive dashboards.

---

## 📁 Project Structure

| Project | Title | Key Skills | Status |
|---------|-------|------------|--------|
| [Project 1](./decodelabs_task%201(Project1)) | Data Cleaning & Preparation | Excel, Python, Pandas | ✅ Completed |
| [Project 2](./decodelabs_task%202(Project2)) | Exploratory Data Analysis (EDA) | Statistics, EDA, Visualization | ✅ Completed |
| [Project 3](./decodelabs_task%203(Project3)) | SQL Data Analysis | SQL, SQLite, Aggregations | ✅ Completed |
| [Project 4](./decodelabs_task%204(Project4)) | Data Visualization | Power BI, Charts, Dashboards | ✅ Completed |

---

## 🧹 Project 1 — Data Cleaning & Preparation

📂 **Folder:** [decodelabs_task 1(Project1)](./decodelabs_task%201(Project1))

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

### Files in This Folder
| File | Description |
|------|-------------|
| `DecodeLabs_Cleaned_Dataset_P1.xlsx` | Production-ready cleaned dataset |
| `DecodeLabs_Change_Log.xlsx` | Full documentation of all 4 changes (CR001–CR004) |
| `project1_data_cleaning.py` | Python source code |

---

## 📈 Project 2 — Exploratory Data Analysis (EDA)

📂 **Folder:** [decodelabs_task 2(Project2)](./decodelabs_task%202(Project2))

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

### Files in This Folder
| File | Description |
|------|-------------|
| `DecodeLabs_EDA_Report_P2.xlsx` | 7-sheet EDA report with full analysis |
| `project2_eda.py` | Python source code |

---

## 🗄️ Project 3 — SQL Data Analysis

📂 **Folder:** [decodelabs_task 3(Project3)](./decodelabs_task%203(Project3))

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

### Files in This Folder
| File | Description |
|------|-------------|
| `DecodeLabs_SQL_Analysis_P3.xlsx` | 12-sheet SQL report + cheat sheet |
| `project3_sql_analysis.py` | Python source code with all 10 queries |

---

## 📊 Project 4 — Data Visualization

📂 **Folder:** [decodelabs_task 4(Project4)](./decodelabs_task%204(Project4))

**Goal:** Create interactive visualizations and a Power BI dashboard to
communicate data insights clearly to stakeholders.

### Visualizations Built

| # | Chart Title | Chart Type | Business Question |
|---|-------------|------------|-------------------|
| C1 | Revenue by Product Category | Horizontal Bar | Which product generates the most revenue? |
| C2 | Order Status Distribution | Donut Chart | What % of orders are delivered vs lost? |
| C3 | Monthly Revenue Trend | Line Chart | How does revenue trend month by month? |
| C4 | Revenue by Marketing Channel | Bar Chart | Which referral source drives most revenue? |
| C5 | Avg Order Value by Payment | Bar + Reference Line | Which payment method has highest avg order? |
| C6 | Order Value Distribution | Histogram | Is order value normally distributed? |
| C7 | Orders & Revenue by Quantity | Dual-Axis Bar | How does bulk ordering affect revenue? |
| C8 | Coupon Code Performance | Side-by-Side Bar | Which coupon drives the most revenue? |
| C9 | Correlation Heatmap | Heatmap | Which variables are most strongly correlated? |
| C10 | Order Status by Product | Stacked Bar | Which products have worst cancellation rate? |

### Key Visual Insights
- 📌 **C2 + C10:** Only 19.3% Delivered — 41.4% are Cancelled or Returned
- 📌 **C3:** Revenue peaked at **$68,069 in June 2024** — lowest was April 2023 ($27,752)
- 📌 **C4:** Instagram leads all channels at **$275,285** total revenue
- 📌 **C6:** Order value is **right-skewed** — median ($823) better than mean ($1,054)
- 📌 **C9:** UnitPrice↔TotalPrice: **r = 0.717** — price is the #1 revenue driver
- 📌 **C7:** Qty=5 orders average **$1,751** — 5× more than Qty=1 orders ($352)

### Files in This Folder
| File | Description |
|------|-------------|
| `project4_data_visualization.pbix` | Power BI interactive dashboard |
| `project4_visualization.py` | Python source code (10 charts using matplotlib & seaborn) |
| `DecodeLabs_Visualization_Report_P4.xlsx` | Excel report with all 10 charts embedded |

---

## 🛠️ Tools & Technologies

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat&logo=sqlite&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=powerbi&logoColor=black)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=flat&logo=python&logoColor=white)

---

## 📬 Connect With Me

Feel free to connect on [LinkedIn](https://www.linkedin.com/in/kandunuri-gayathri-28a636342) 🤝

---
*Industrial Training Kit | Batch 2026 | Powered by DecodeLabs*
