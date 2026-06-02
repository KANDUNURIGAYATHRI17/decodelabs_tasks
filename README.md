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
| [Project 4](./decodelabs_task%204(Project4)) | Data Visualization | Power BI, DAX, Dashboards | ✅ Completed |

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

**Goal:** Transform cleaned e-commerce data into an executive-level interactive
Power BI dashboard tracking **$1.26M in revenue** across 1,200 transactions
(Jan 2023 – Jun 2025) — uncovering operational inefficiencies and systemic
revenue leakage in order fulfillment.

> 💡 **What is Data Visualization?**
> Data Visualization is the process of representing raw numbers as charts,
> graphs, and dashboards so that patterns, trends, and outliers become
> instantly visible to decision-makers. Instead of reading rows of data,
> stakeholders can *see* the story the data is telling — in seconds.
> The goal is not just to make things look good, but to make insights
> **undeniable and actionable**.

---

### Dashboard Preview
![Dashboard Preview](./decodelabs_task%204(Project4)/project4_data_visualization.jpeg)

---

### 📋 Executive Summary (SCQA Framework)

> The **SCQA (Situation → Complication → Question → Answer)** framework
> ensures decision-makers immediately understand the business context,
> the core problem, and the recommended action — without reading a report.

| | |
|---|---|
| **Situation** | $1.26M gross revenue generated across 7 product categories and 5 acquisition channels over a multi-year period |
| **Complication** | Only **19.3%** of orders reach "Delivered" status — **20.8%** are Cancelled, leaking significant revenue out of the pipeline |
| **Resolution** | Overhaul fulfillment for **Chair** (top revenue driver with 25% cancellation rate) + investigate **Google** and **Email** channel quality |

---

### 🛠️ Tech Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Data Source | Excel (.xlsx) | 1,200-row cleaned e-commerce dataset |
| Transformation | Power Query (M Language) | Schema validation, data type enforcement |
| Analytics | Microsoft Power BI Desktop | Dashboard building and interactivity |
| Measures | DAX (Data Analysis Expressions) | KPI calculations and conditional logic |
| Charts (Python) | Matplotlib & Seaborn | 10 static charts for Excel report |

---

### 📐 DAX Measures Written

> **DAX (Data Analysis Expressions)** is Power BI's formula language —
> used to create calculated KPIs, percentages, and conditional metrics
> that update dynamically as users filter the dashboard.

```DAX
-- 1. Total Revenue — sums all transaction values
Total Revenue = SUM('Sheet1'[TotalPrice])

-- 2. Total Orders — counts every row in the dataset
Total Orders = COUNTROWS('Sheet1')

-- 3. Delivered Rate — % of orders successfully fulfilled
Delivered Rate =
DIVIDE(
    CALCULATE([Total Orders], 'Sheet1'[OrderStatus] = "Delivered"),
    [Total Orders], 0
)

-- 4. Cancellation Rate — % of orders that were cancelled
Cancellation Rate =
DIVIDE(
    CALCULATE([Total Orders], 'Sheet1'[OrderStatus] = "Cancelled"),
    [Total Orders], 0
)

-- 5. Average Order Value — mean spend per transaction
Average Order Value = AVERAGE('Sheet1'[TotalPrice])
```

---

### 🎨 Visualizations Built

#### Power BI Dashboard Visuals

| # | Visual | Chart Type | Why This Chart? |
|---|--------|------------|-----------------|
| 1 | KPI Summary Cards | Card (New) — 1×4 grid | Gives leadership instant top-line numbers at a glance |
| 2 | Revenue by Product | Clustered Bar | Compares categories side-by-side; highlights Chair in red as risk |
| 3 | Monthly Revenue Trend | Line Chart | Shows seasonality and growth trajectory over time |
| 4 | Revenue by Channel | Clustered Column | Compares acquisition channel quality visually |
| 5 | Payment × Status Matrix | Conditional Table | Cross-references payment method with order outcome |

#### Python Charts (Matplotlib & Seaborn)

| # | Chart Title | Chart Type | Business Question Answered |
|---|-------------|------------|---------------------------|
| C1 | Revenue by Product Category | Horizontal Bar | Which product generates the most revenue? |
| C2 | Order Status Distribution | Donut Chart | What % of orders are delivered vs lost? |
| C3 | Monthly Revenue Trend | Line + Area | How does revenue trend month by month? |
| C4 | Revenue by Marketing Channel | Bar Chart | Which referral source drives most revenue? |
| C5 | Avg Order Value by Payment | Bar + Reference Line | Which payment method has highest avg order? |
| C6 | Order Value Distribution | Histogram | Is order value normally distributed or skewed? |
| C7 | Orders & Revenue by Quantity | Dual-Axis Bar | How does bulk ordering affect revenue? |
| C8 | Coupon Code Performance | Side-by-Side Bar | Which coupon drives the most revenue? |
| C9 | Correlation Heatmap | Seaborn Heatmap | Which numeric variables are most strongly linked? |
| C10 | Order Status by Product | Stacked Bar | Which products have the worst cancellation rate? |

---

### 🔑 Key Visual Insights Uncovered

- 🚨 **Chair Fulfillment Crisis** — Leads in revenue but carries a **25% cancellation rate** — capital leaking directly from the supply chain
- ⚠️ **Google & Email Risk** — High order volume but **worst post-purchase retention** — ad spend quality needs investigation
- ✅ **Instagram Quality** — Brings highly qualified buyers with **near-zero cancellation rates** — increase ad spend here
- 📉 **Only 19.3% Delivered** — Systemic fulfillment failure across all categories — urgent operational overhaul needed
- 📊 **Right-Skewed Revenue** — Median ($823) is the better performance benchmark vs Mean ($1,054)
- 💡 **Qty=5 orders earn 5× more** — Bundle promotions targeting Qty=2/3 buyers could significantly lift revenue

---

### 📁 Files in This Folder

| File | Description |
|------|-------------|
| `project4_data_visualization.pbix` | Power BI interactive dashboard (main deliverable) |
| `project4_data_visualization.jpeg` | Dashboard screenshot preview |
| `project4_visualization.py` | Python source code — 10 charts using matplotlib & seaborn |
| `DecodeLabs_Visualization_Report_P4.xlsx` | Excel report with all 10 charts embedded + data tables |

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
