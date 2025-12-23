# Supermarket Sales & Profit Analyzer 📊

A Python-based data analysis tool that processes supermarket transaction data to provide actionable business insights. This project calculates key financial metrics and visualizes sales trends across different product categories.

## 📊 Data Source
The dataset used in this project is sourced from Kaggle:
[Supermarket Sales Dataset](https://www.kaggle.com/datasets/faresashraf1001/supermarket-sales)

## 📋 Data Dictionary
The analyzer processes the following attributes for each transaction:
- **Invoice ID:** Unique identifier for each transaction.
- **Branch/City:** Location details (Yangon, Naypyitaw, Mandalay).
- **Product Line:** Category (e.g., Electronic Accessories, Food & Beverages).
- **Unit Price / Quantity:** Pricing and volume details.
- **Total:** Transaction total including 5% tax.
- **COGS:** Cost of Goods Sold (the raw cost of the products).
- **Gross Income:** The actual profit earned from the transaction.
- **Rating:** Customer satisfaction score (out of 10).

## 🚀 Analysis Modules

### 1. Financial KPI Summary (`kpi_summary.py`)
Generates a high-level executive report in the terminal, identifying the "big numbers" for the business.
* **Metrics:** Total Revenue, Total Gross Profit, and Average Customer Satisfaction.

### 2. Category Performance (`sales_by_category.py`)
Identifies which product lines drive the most revenue using a horizontal bar chart.
* **Insight:** Helps determine inventory priority and marketing focus.
* **Output:** `outputs/sales_by_category.png`

### 3. Branch Benchmarking (`branch_analysis.py`)
Compares performance across different store locations (Alex, Cairo, and Giza).
* **Metrics:** Visualizes total profit per branch and compares it against customer ratings.
* **Output:** `outputs/branch_profit.png` & `outputs/branch_rating.png`

### 4. Operational Time Analysis (`time_analysis.py`)
Analyzes transaction timestamps to identify peak shopping hours.
* **Insight:** Informs staffing schedules to improve customer service during rush hours.
* **Output:** `outputs/hourly_traffic.png`

## 🛠️ Tools Used
- **Python 3.13**
- **Pandas:** For data manipulation and aggregation.
- **Matplotlib:** For data visualization.

## 📂 Project Structure
```text
├── kpi_summary.py         # Terminal-based KPI report
├── sales_by_category.py   # Category analysis visualization
├── branch_analysis.py     # Location-based comparison
├── time_analysis.py       # Time-series traffic analysis
├── data/                  # Source CSV: SuperMarket Analysis.csv
└── outputs/               # Saved charts and visualizations
```

## 📊 Sample Output
After running the script, the tool generates a summary like this:
```text
Total Revenue:  $322,966.75
Total Expenses: $307,587.38
Total Profit:   $15,379.37
```

## ⚙️ Setup & Usage
Clone the repo:

```Bash

git clone [https://github.com/sup3rknight/supermarket-sales-analytics.git](https://github.com/sup3rknight/supermarket-sales-analytics.git)
```
Install requirements:
```Bash

pip install pandas matplotlib
```
Run any module:
```Bash

python kpi_summary.py
python sales_by_category.py
python branch_analysis.py
python time_analysis.py
```
