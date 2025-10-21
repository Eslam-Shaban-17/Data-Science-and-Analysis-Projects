Here’s a clean, professional **README.md** for your Power BI + MySQL project using the **Awesome Chocolates** dataset 👇

---

# 🍫 Awesome Chocolates Sales Analysis

**Power BI + MySQL Data Analytics Project**

## 📊 Project Overview

This project demonstrates how to use **MySQL** as a data source and **Power BI** as a visualization tool to analyze the sales performance of **Awesome Chocolates**, a fictional chocolate company.

Using SQL for data modeling and Power BI for visualization, this analysis uncovers key business insights about **sales, products, teams, and regions**.

---

## 🧠 Objectives

* Analyze sales performance across **regions**, **teams**, and **products**
* Identify **top-performing salespersons** and **best-selling products**
* Track **revenue trends over time**
* Build an **interactive Power BI dashboard** connected directly to the MySQL database

---

## 🏗️ Tech Stack

| Tool         | Purpose                                             |
| ------------ | --------------------------------------------------- |
| **MySQL**    | Data storage, modeling, and queries                 |
| **Power BI** | Data visualization and dashboard creation           |
| **SQL**      | Data extraction, transformation, and joining tables |

---

## 🗃️ Database Schema

The dataset consists of **five related tables**:

| Table        | Description                                                         |
| ------------ | ------------------------------------------------------------------- |
| **geo**      | Contains geographical details (GeoID, Country, Region)              |
| **people**   | Information about salespersons, teams, and locations                |
| **products** | Product details including category, size, and cost per box          |
| **sales**    | Sales transactions (Salesperson, Product, Amount, Boxes, Customers) |

### 🔗 Relationships

* `sales.SPID` → `people.SPID`
* `sales.GeoID` → `geo.GeoID`
* `sales.PID` → `products.PID`

This relational model enables cross-table insights such as “Sales by Region and Product Category” or “Performance by Team.”

---

## ⚙️ Setup Instructions

1. **Create the database in MySQL**

   ```sql
   CREATE DATABASE IF NOT EXISTS `awesome chocolates`;
   USE `awesome chocolates`;
   ```

2. **Import the provided `.sql` script** (included in this repository).
   It creates the schema and inserts sample data for all tables.

3. **Connect Power BI to MySQL**

   * Open Power BI Desktop
   * Go to **Home → Get Data → MySQL Database**
   * Enter your MySQL server credentials and database name
   * Load the tables: `sales`, `products`, `people`, `geo`
   * Use **Power Query Editor** to clean and transform data if needed

4. **Build the Dashboard**

   * Add visuals like:

     * Total Sales & Revenue KPIs
     * Sales by Region (Map)
     * Top 5 Products (Bar Chart)
     * Monthly Sales Trend (Line Chart)
     * Team Performance (Table / Matrix)

---

## 📈 Example Insights

* **Top Region:** APAC generated the highest total sales
* **Best-Selling Product:** “Milk Bars” and “85% Dark Bars” lead the charts
* **Top Salesperson:** Barr Faughny from Team Yummies
* **Peak Month:** December shows the highest revenue across all years

---

## 📁 Files in this Repository

```
📦 awesome-chocolates-analysis
├── README.md
├── awesome_chocolates.sql
├── PowerBI_Report.pbix
├── .gitignore
```

---

## 🧩 Future Enhancements

* Automate daily data refresh in Power BI
* Add forecasting and trend analysis
* Integrate Python or DAX for advanced metrics
* Create dynamic filters for better interactivity

---

## 🧑‍💻 Author

**Eslam Shaban**
📧 [eslamshaban170@gmail.com]
📍 Power BI & Data Analytics Enthusiast

---

Would you like me to make this README more **data analyst portfolio–ready** (with visuals preview section and polished intro for GitHub)? It’ll make it look like a professional portfolio project.
