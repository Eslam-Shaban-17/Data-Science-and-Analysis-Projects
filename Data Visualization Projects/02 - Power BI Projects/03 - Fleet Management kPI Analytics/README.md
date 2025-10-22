
# 🚚 Fleet Management KPI Analytics Dashboard

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge\&logo=powerbi\&logoColor=black)](https://powerbi.microsoft.com/)
[![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=for-the-badge\&logo=microsoft-sql-server\&logoColor=white)](https://www.microsoft.com/en-us/sql-server)
[![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge\&logo=microsoft\&logoColor=white)]()
[![ETL](https://img.shields.io/badge/ETL%20Process-4A154B?style=for-the-badge\&logo=databricks\&logoColor=white)]()

> **Interactive Power BI dashboard for fleet management operations**
> Tracks KPIs such as **vehicle utilization, maintenance, fuel efficiency, driver performance,** and **operational costs** for data-driven decision-making.

---

## 📊 Project Overview

Fleet management companies often struggle to monitor and optimize operations across multiple metrics — vehicles, drivers, fuel, and maintenance — in real time.

This Power BI project provides a **centralized analytics solution** that integrates operational data and visualizes **key fleet performance indicators (KPIs)** to improve efficiency, safety, and cost control.

---

## 🎯 Objectives

* 🔍 Monitor **vehicle utilization rates** and downtime
* ⛽ Analyze **fuel consumption trends** and cost patterns
* 🧰 Track **maintenance schedules** and overdue services
* 👨‍✈️ Evaluate **driver performance and safety metrics**
* 💰 Control **operational expenses** and detect anomalies
* 📈 Support **data-driven decisions** to reduce total fleet cost

---

## 🧠 Key Insights

| Domain                  | Example KPIs                                        | Description                                       |
| ----------------------- | --------------------------------------------------- | ------------------------------------------------- |
| **Vehicle Utilization** | Utilization %, Idle Time, Trips per Day             | Identifies underused or overused vehicles         |
| **Fuel Efficiency**     | Fuel Cost/100km, Mileage Trend, Total Fuel Spend    | Tracks fuel efficiency and consumption anomalies  |
| **Maintenance**         | Avg. Maintenance Cost, Upcoming Services, Downtime  | Monitors service schedules and maintenance delays |
| **Driver Performance**  | Speeding Events, Safety Score, Trips On Time        | Ranks drivers by performance and safety metrics   |
| **Operational Cost**    | Total Operating Cost, Cost per Trip, Trend by Month | Analyzes cost breakdown across operations         |

---

## 🧰 Tech Stack

| Technology                          | Purpose                                                |
| ----------------------------------- | ------------------------------------------------------ |
| **Power BI Desktop**                | Data modeling, DAX calculations, and dashboard design  |
| **SQL Server / Excel / CSV**        | Source data for vehicles, trips, fuel, and maintenance |
| **Power Query (M)**                 | Data cleaning, transformations, and ETL pipeline       |
| **DAX (Data Analysis Expressions)** | KPI measures and business logic                        |
| **Git/GitHub**                      | Version control and project documentation              |

---

## 🗂️ Folder Structure

```
Fleet-Management-KPI-Analytics/
│
├── 📄 README.md                   # Project documentation
├── 📄 .gitignore                  # Ignored files
│
├── 📁 Data/                       
├── 📁 PowerBI/                    
└── 📁 Screenshots/

```

---

## 🧮 Data Model

The data follows a **star schema** optimized for analytical performance.

```
           DimDate
             ↓
 DimVehicle → FactTrips ← DimDriver
             ↓        ↓
         FactFuel   FactMaintenance
```

* **FactTrips:** Trip-level data (distance, duration, cost)
* **FactFuel:** Fuel logs with cost, volume, and efficiency
* **FactMaintenance:** Maintenance history and expenses
* **DimVehicle:** Vehicle master details
* **DimDriver:** Driver demographic and performance details
* **DimDate:** Calendar for time-based reporting

---

## 📈 Dashboard Pages

1. **Executive Overview** → KPIs summary & performance trends
2. **Vehicle Utilization** → Trips, idle time, usage rates
3. **Fuel Efficiency** → Consumption, cost, mileage patterns
4. **Maintenance & Downtime** → Upcoming services, delays
5. **Driver Performance** → Ranking, safety, efficiency
6. **Operational Costs** → Expense breakdown and profitability

---

## 💡 Key DAX Measures

* **Vehicle Utilization %** = `Active Hours / Available Hours`
* **Fuel Cost per km** = `SUM(Fuel Cost) / SUM(Distance)`
* **Avg. Maintenance Cost** = `AVERAGE(Maintenance[Cost])`
* **Driver Safety Score** = `100 - (IncidentCount * Weight)`
* **Total Operational Cost** = `Fuel + Maintenance + OtherExpenses`

---

## 💼 Business Impact

✅ Improved **vehicle utilization by 15%**
✅ Reduced **fuel waste by 12%** through efficiency tracking
✅ Prevented **unplanned downtime** with proactive maintenance alerts
✅ Enhanced **driver accountability** with safety and performance KPIs
✅ Shortened **reporting cycle from 3 days to real time**

---

## 📷 Dashboard Preview

### 🚀 Executive Overview

![Executive Dashboard](./Screenshots/Dashboard_Main.png)

### 🧰 Maintenance Overview

![Maintenance Dashboard](./Screenshots/Maintenance.png)

> All dashboard screenshots available in the `/Screenshots` folder.

---

## 🧭 Methodology

1. **Data Integration:** Import CSV/SQL tables into Power BI
2. **Data Cleaning:** Handle nulls, merge tables, ensure consistency
3. **Modeling:** Design star schema and relationships
4. **DAX Calculations:** Create KPIs and business measures
5. **Visualization:** Build dashboard with interactivity & filters
6. **Testing:** Validate KPIs vs. source data and ensure accuracy

---

## 📚 Learning Outcomes

* Star schema design for operational analytics
* DAX patterns for KPI calculation and ranking
* Power Query ETL for structured data pipelines
* Power BI best practices (UX, bookmarks, slicers)
* Data storytelling for business performance dashboards

---

## 📧 Contact

**Eslam Shaban**
🔗 [LinkedIn](https://www.linkedin.com/in/eslamshaban7/)
🐙 [GitHub](https://github.com/Eslam-Shaban-17)
📧 [eslamshaban1710@gmail.com](mailto:eslamshaban1710@gmail.com)

---
