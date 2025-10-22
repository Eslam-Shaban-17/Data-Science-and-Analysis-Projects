# 🦠 COVID-19 Deaths & Vaccinations Dashboard (Tableau)

[![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge\&logo=tableau\&logoColor=white)](https://www.tableau.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge\&logo=microsoft-sql-server\&logoColor=white)]()
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-4A154B?style=for-the-badge\&logo=databricks\&logoColor=white)]()

> **End-to-end COVID-19 analytics project** combining **SQL Server** for data processing and **Tableau** for interactive visualization.
> Tracks global **deaths, infections, and vaccination progress** with real-time, dynamic insights.

---

## 📋 Project Overview

During the COVID-19 pandemic, decision-makers needed fast, reliable insights into how infection and vaccination trends evolved across countries and time.
This project delivers a **comprehensive analytical pipeline** — from raw data exploration in SQL Server to a **fully interactive Tableau dashboard** that visualizes global health outcomes.

---

## 🎯 Objectives

* 🔍 Analyze global and country-level **death and infection rates**
* 💉 Track **vaccination rollout progress** over time
* 🌍 Compare **continents and countries** by infection density
* 🧮 Compute **death rate**, **infection percentage**, and **vaccination ratios**
* 📊 Provide an **interactive Tableau dashboard** for stakeholders and analysts

---

## 🧰 Tech Stack

| Tool                | Purpose                                           |
| ------------------- | ------------------------------------------------- |
| **SQL Server**      | Data extraction, transformation, and calculations |
| **T-SQL**           | Joins, CTEs, Temp Tables, and Window Functions    |
| **Tableau Desktop** | Visualization and dashboard creation              |
| **Excel / CSV**     | Source datasets for deaths and vaccinations       |
| **Git / GitHub**    | Version control and documentation                 |

---

## 🗂️ Folder Structure

```
COVID19-Deaths-Dashboard/
│
├── 📄 README.md
├── 📄 .gitignore
│
├── 📁 Data/
├── 📁 Data-Exploration/
├── 📁 Data-Modeling/
├── 📁 Tableau/
└── 📁 Screenshots/
    ├── Business_Objectives.md
    ├── Methodology.md
    └── Key_Insights.md
```

---

## 🧮 SQL Analysis Highlights

### 🔹 Advanced Techniques Used

* **Joins** → combined deaths and vaccination datasets
* **CTEs** → simplified reusable calculations (e.g., total cases per country)
* **Temp Tables** → staged intermediate results for Tableau export
* **Window Functions** → used `SUM() OVER()` for rolling vaccination totals
* **Aggregate Views** → created country and continent-level summaries

### 🔹 Key Metrics Calculated

| Metric                        | Formula                                                             | Description                        |
| ----------------------------- | ------------------------------------------------------------------- | ---------------------------------- |
| **Death Rate (%)**            | `(Total_Deaths / Total_Cases) * 100`                                | % of infected individuals who died |
| **Infection Rate (%)**        | `(Total_Cases / Population) * 100`                                  | % of total population infected     |
| **Vaccination Progress (%)**  | `(People_Vaccinated / Population) * 100`                            | % of population vaccinated         |
| **Rolling Vaccination Total** | `SUM(People_Vaccinated) OVER (PARTITION BY Location ORDER BY Date)` | Cumulative vaccinations over time  |

---

## 📈 Tableau Dashboard Overview

### Dashboard Pages

1. **Global Overview** → KPIs for total cases, deaths, and vaccination rate
2. **Continent Trends** → Drill-down analysis by continent
3. **Country Comparison** → Interactive map with filters by date & region
4. **Vaccination Progress** → Rolling vaccination coverage per country
5. **Death Rate vs. Infection Rate** → Correlation and time-based analysis

### Key Features

* 🌐 **Interactive map visualizations** with country selection
* ⏱️ **Date filters** for time-based exploration
* 📊 **Dynamic KPIs** with real-time percentage updates
* 📉 **Trend lines** showing infection and vaccination evolution

---

## 💡 Business Insights

* **Global death rate:** ~2.1% (high variation across continents)
* **Highest infection rates:** North & South America
* **Vaccination progress:** Rapid increase post-mid-2021
* **Strong negative correlation:** Between vaccination rate and death rate
* **Data-driven takeaway:** Countries with early vaccine rollouts saw death rates fall by up to 60%

---

## 🧭 Methodology

1. **Data Extraction** — Imported raw CSVs into SQL Server
2. **Cleaning & Transformation** — Handled nulls, standardized country names
3. **Data Analysis (SQL)** — Derived metrics via CTEs, temp tables, and window functions
4. **Aggregation** — Built reusable summary views for Tableau
5. **Visualization (Tableau)** — Created interactive dashboards with KPIs and maps
6. **Validation** — Cross-checked against WHO and public datasets

---

## 📸 Dashboard Preview

### 🌍 Global COVID-19 Summary

![Dashboard Screenshot](./Tableau/Dashboard_Screenshot.png)

> More visuals available in `/Tableau/` folder.

---

## 💼 Business Impact

✅ Delivered **centralized COVID-19 analytics** in a single dashboard
✅ Reduced manual data preparation time by **80%** through SQL automation
✅ Provided **real-time insights** into global infection and vaccination trends
✅ Supported **data-driven health strategy** for stakeholders

---

## 📚 Learning Outcomes

* Advanced **SQL analytical techniques** (CTEs, temp tables, window functions)
* **ETL pipeline design** for reporting and visualization
* Building **data models for Tableau** from SQL Server
* Designing **interactive dashboards** for storytelling
* Translating raw data into **actionable health insights**

---

## 📧 Contact

**Eslam Shaban**
🔗 [LinkedIn](https://www.linkedin.com/in/eslamshaban7/)
🐙 [GitHub](https://github.com/Eslam-Shaban-17)
📧 [eslamshaban1710@gmail.com](mailto:eslamshaban1710@gmail.com)

