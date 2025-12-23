import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load the file
# We use a simple name. Make sure the CSV is in the same folder as this script!
file_name = 'data/SuperMarket Analysis.csv'

if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print("✅ File loaded successfully!")
else:
    print(f"❌ Error: Could not find '{file_name}' in this folder.")
    exit()

# 2. Calculate Totals
total_sales = df['Sales'].sum()
total_expenses = df['cogs'].sum()
total_profit = df['gross income'].sum()

# Print results to the terminal
print(f"Total Revenue:  ${total_sales:,.2f}")
print(f"Total Expenses: ${total_expenses:,.2f}")
print(f"Total Profit:   ${total_profit:,.2f}")

# 3. Grouping the data
category_sales = df.groupby('Product line')['Sales'].sum().sort_values(ascending=True)

# 4. Creating and SAVING the Bar Chart
plt.figure(figsize=(10, 6))
category_sales.plot(kind='barh', color='skyblue')

plt.title('Total Sales by Product Category')
plt.xlabel('Sales ($)')
plt.ylabel('Product Line')
plt.tight_layout() # Prevents labels from getting cut off

# This saves the chart to your folder as a PNG file
plt.savefig(os.path.join('outputs', 'sales_by_category.png'))
print("✅ Chart saved inside 'outputs/sales_by_category.png'")


plt.show()