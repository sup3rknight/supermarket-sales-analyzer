import pandas as pd
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv('data/SuperMarket Analysis.csv')

# 2. Extract hour and count transactions
df['Hour'] = pd.to_datetime(df['Time']).dt.hour
hourly_counts = df.groupby('Hour').size()

# 3. Create a simple line chart
hourly_counts.plot(kind='line', marker='o')

# 4. Label and save
plt.title('Transactions by Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Sales')
plt.savefig('outputs/hourly_traffic.png')

print("✅ Time analysis saved to outputs/hourly_traffic.png")