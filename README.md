# Project Overview
This project simulates a real-world data analytics workflow using the Olist Brazilian E-Commerce dataset. The objective is to clean raw, fragmented transactional data, establish relational logic, and visualize key logistics and revenue metrics to support business decision-making.

Dataset link: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

**Tech Stack Used**

* **Data Cleaning & Preprocessing:** Python (Pandas, NumPy, seaborn/matplotlib, SQLAlchemy)
* **Relational Database & Aggregation:** SQL ( MySQL)
* **Data Visualization:** Tableau

**Business Questions Addressed**

1. What is the total revenue generated month-over-month?
2. Which geographic regions experience the highest freight costs and delivery delays?
3. Who are the top 5% most valuable customers based on total spending?

## ⚙️ ETL Pipeline & Methodology
1. **Data Extraction & Cleaning:** Raw CSV files were extracted and processed using Python (Pandas). Null values were handled, data types were corrected (especially datetime features), and missing temporal data was imputed logically. 
2. **Database Loading:** The cleaned DataFrames were exported to a local **MySQL** database using `SQLAlchemy`. 
3. **Data Aggregation:** Complex SQL queries (utilizing `JOIN`s, `GROUP BY`, `DATEDIFF`, and Window Functions like `NTILE`) were executed to aggregate metrics such as delayed deliveries, freight costs, and customer percentiles.
4. **Visualization:** The final aggregated tables were connected to **Tableau** to build an interactive dashboard.
