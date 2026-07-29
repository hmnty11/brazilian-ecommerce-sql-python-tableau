# Project Overview

This project simulates a real-world data analytics workflow using the Olist Brazilian E-Commerce dataset. The objective is to clean raw, fragmented transactional data, establish relational logic, and visualize key logistics and revenue metrics to support business decision-making.

Dataset link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

**Tech Stack Used**

- **Data Cleaning & Preprocessing:** Python (Pandas, glob, python-dotenv, SQLAlchemy)
- **Relational Database & Aggregation:** SQL ( MySQL)
- **Data Visualization:** Tableau

**Business Questions Addressed**

1. What is the total revenue generated month-over-month?
2. Which geographic regions experience the highest freight costs and delivery delays?
3. Who are the top 5% most valuable customers based on total spending?

## ⚙️ ETL Pipeline & Methodology

1. **Data Extraction & Cleaning:** Raw CSV files were extracted and processed using Python (Pandas). Null values were handled, data types were corrected (especially datetime features), and missing temporal data was imputed logically.
2. **Database Loading:** The cleaned DataFrames were exported to a local **MySQL** database using `SQLAlchemy`.
3. **Data Aggregation:** Complex SQL queries (utilizing `JOIN`s, `GROUP BY`, `DATEDIFF`, and Window Functions like `NTILE`) were executed to aggregate metrics such as delayed deliveries, freight costs, and customer percentiles.
4. **Visualization:** The final aggregated tables were connected to **Tableau** to build an interactive dashboard.

## 📈 Interactive Dashboard

The final output is an interactive Tableau executive dashboard utilizing regional parameters as control filters, designed with a modern Card UI layout.

![Olist Dashboard](https://github.com/user-attachments/assets/c74f37bf-454b-4ec2-af93-5738f8270360)

🔗 **[Click Here to View the Interactive Dashboard on Tableau Public](https://public.tableau.com/views/OLISTSALESLOGISTICSPERFORMANCE/OlistE-CommercePerformanceDashboard_?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)**

## 💡 Key Insights

- **Revenue Trend:** Olist E-commerce is getting more mature financially, and trend for the monthly revenue is uptrend but more likely going to stagnant based on percentage growth(increase marketing funds and expans to other regions or countries)
- **Logistics Bottleneck:** There is some logistics bottlenecks on AP, RR, AM, AC States. The most delayed delivery is 96 Days on AP(Need to change Distribution vendors or find and maintain new distribution partners)
- **Customer Retention:** Top 5% customers is contributing approximately 38% on Olist E-commerce revenue (we need to maintain or increase our customer base to other region)
