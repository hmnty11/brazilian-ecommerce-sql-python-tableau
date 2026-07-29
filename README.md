# Brazilian E-Commerce Analytics & ETL Pipeline (Olist)

## 📌 Project Overview
This project simulates a real-world data analytics workflow using the Olist Brazilian E-Commerce dataset. The objective is to clean raw, fragmented transactional data, establish relational logic, and visualize key logistics and revenue metrics to support strategic business decision-making.

**Dataset link:** [Olist Brazilian E-Commerce on Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

## 🛠️ Tech Stack Used
- **Data Cleaning & Preprocessing:** Python (Pandas, glob, python-dotenv, SQLAlchemy)
- **Relational Database & Aggregation:** SQL (MySQL)
- **Data Visualization:** Tableau

## ❓ Business Questions Addressed
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

## 💡 Key Findings & Strategic Recommendations

*   **The Revenue Mirage:** 
    *   *Insight:* While the macro trend shows revenue growth, Month-over-Month (MoM) growth rates are steadily decelerating. Without intervention, the overall revenue is statistically projected to stagnate. 
    *   *Recommendation:* Reallocate marketing funds to aggressively expand customer acquisition in untapped regions or international markets.
*   **Critical Supply Chain Bottlenecks:** 
    *   *Insight:* Delivery operations are facing severe friction in AP, RR, AM, and AC states. The most extreme case is a 96-day delivery delay in the AP state.
    *   *Recommendation:* Restructure regional logistics operations. We need to evaluate current distribution vendors and potentially partner with new, localized logistics providers in those high-friction states.
*   **High Customer Concentration Risk:** 
    *   *Insight:* The Top 5% of customers contribute approximately 38% of the total E-commerce revenue. 
    *   *Recommendation:* While retaining these VIP clients is crucial, the business must mitigate this concentration risk by diversifying the customer base and launching loyalty programs for mid-tier buyers.
