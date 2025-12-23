import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data and group by Branch
df = pd.read_csv('data/SuperMarket Analysis.csv')
df.columns = df.columns.str.strip()
stats = df.groupby('Branch').agg({'gross income': 'sum', 'Rating': 'mean'})

# 2. Plot Profit
stats['gross income'].plot(kind='bar', color='skyblue', title='Total Profit by Branch')
plt.ylabel('Profit ($)')
plt.savefig('outputs/branch_profit.png')
plt.clf() # This clears the page for the next chart

# 3. Plot Rating
stats['Rating'].plot(kind='bar', color='salmon', title='Average Rating by Branch')
plt.ylabel('Rating (1-10)')
plt.savefig('outputs/branch_rating.png')

print("Done! Check your outputs folder for branch_profit.png and branch_rating.png")