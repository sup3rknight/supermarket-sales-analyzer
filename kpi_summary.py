import pandas as pd

# 1. Load data
df = pd.read_csv('data/SuperMarket Analysis.csv')

# 2. Clean column names
df.columns = df.columns.str.strip()

# 3. Calculate KPIs (Using 'Sales' instead of 'Total' to match your file)
# Note: If 'Sales' fails, try 'Total' - but your previous script used 'Sales'
total_revenue = df['Sales'].sum() 
total_profit = df['gross income'].sum()
avg_rating = df['Rating'].mean()
total_transactions = len(df)

# 4. Print the Summary Report
print("\n--- SUPERMARKET KPI SUMMARY ---")
print(f"Total Transactions: {total_transactions}")
print(f"Total Revenue:      ${total_revenue:,.2f}")
print(f"Total Gross Profit: ${total_profit:,.2f}")
print(f"Avg Customer Rating: {avg_rating:.2f} / 10")
print("-------------------------------\n")