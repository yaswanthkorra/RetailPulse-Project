 RetailPulse - AI-Powered Customer Analytics & Demand Forecasting
 Project Overview
This project analyzes retail sales data to find customer patterns, 
predict churn, and optimize inventory using machine learning.
Built as part of Zidio Development Data Science Internship - March 2026.
 What This Project Does
- Sales analysis by category, gender, and age group
- Customer segmentation into Bronze, Silver, Gold groups using KMeans
- Churn prediction using Random Forest classifier (100% accuracy)
- Inventory optimization with reorder points and recommended stock
- 7 interactive charts and visualizations

 Tech Stack Used
| Tool | Purpose |
|------|---------|
| Python | Main programming language |
| Pandas, NumPy | Data manipulation |
| Scikit-learn | KMeans clustering, Random Forest |
| Matplotlib, Seaborn | Charts and visualizations |
| Jupyter Notebook | Development environment |

 Dataset
- 1000 retail transactions (2023-2025)
- Columns: Transaction ID, Date, Customer ID, Gender, Age,
  Product Category, Quantity, Price per Unit, Total Amount

 Key Results
- Total Records: 1000
- Total Customers: 1000
- Total Revenue: $757,500
- Top Category: Beauty
- Top Gender: Female (69.3% of sales)
- Customer Segments: Bronze (500), Gold (250), Silver (250)
- Churn Model Accuracy: 100%
- Inventory Reorder Point: 17-18 units per category

 Project Structure
RetailPulse/

│

├── retail_sales_dataset.csv    # Dataset

├── Retail-Sales-Project.ipynb  # Main notebook

├── sales_category.png          # Chart 1

├── gender_analysis.png         # Chart 2

├── age_group.png               # Chart 3

├── monthly_trend.png           # Chart 4

├── heatmap.png                 # Chart 5

├── segmentation.png            # Chart 6

├── inventory.png               # Chart 7

└── README.md                   # This file
 RetailPulse - AI-Powered Customer Analytics
Project Overview
This project analyzes retail sales data to find
customer patterns, predict churn, and optimize
inventory using machine learning.

What This Project Does
- Sales analysis by category, gender, age group
- Customer segmentation (Bronze, Silver, Gold)
- Churn prediction using Random Forest (100% accuracy)
- Inventory optimization with reorder points
- 7 interactive charts and visualizations

Tech Stack Used
- Python, Pandas, NumPy
- Scikit-learn (KMeans, RandomForest)
- Matplotlib, Seaborn
- Jupyter Notebook

Dataset
- 1000 retail transactions
- Columns: Date, Customer ID, Gender, Age,
  Product Category, Quantity, Price, Total Amount

Key Results
- Total Revenue: $757,500
- Top Category: Beauty
- Top Gender: Female (69.3% of sales)
- Customer Segments: Bronze(500), Gold(250), Silver(250)
- Churn Model Accuracy: 100%

How to Run
1. Clone this repository
2. Install requirements: pip install pandas numpy
   matplotlib seaborn scikit-learn
3. Open RetailPulse.ipynb in Jupyter Notebook
4. Run all cells
Author
Yaswanth Korra — Zidio Development Internship
March 2026