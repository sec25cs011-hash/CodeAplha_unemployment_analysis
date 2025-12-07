import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
df = pd.read_csv(r"C:\Users\hp\OneDrive\Desktop\code alpha\Code Alpha Nov Mon 2\Unemployment_Rate_upto_11_2020.csv")

# 2. Fix column name spaces (VERY IMPORTANT)
df.columns = df.columns.str.strip()

# 3. Show first few rows
print("First 5 rows:")
print(df.head())

# 4. Basic info
print("\nDataset Info:")
print(df.info())

# 5. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 6. Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# 7. Plot Unemployment Trend over Time
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Estimated Unemployment Rate (%)'])
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.title("Unemployment Rate Trend in India")
plt.grid(True)
plt.show()

# 8. State-wise Average Unemployment
state_avg = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(12,6))
state_avg.sort_values().plot(kind='bar')
plt.xlabel("State")
plt.ylabel("Average Unemployment (%)")
plt.title("State-wise Average Unemployment Rate")
plt.grid(True)
plt.show()

# 9. Covid Impact (2020 Data Only)
covid_data = df[df['Date'].dt.year == 2020]

plt.figure(figsize=(10,5))
plt.plot(covid_data['Date'], covid_data['Estimated Unemployment Rate (%)'])
plt.xlabel("Month (2020)")
plt.ylabel("Unemployment Rate (%)")
plt.title("Covid-19 Impact on Unemployment (2020)")
plt.grid(True)
plt.show()
