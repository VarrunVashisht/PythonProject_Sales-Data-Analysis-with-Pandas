# Simple Sales Data Analysis with Pandas
# Author: Varrun Vashisht
# Goal: Learn data Loading, cleaning, analysis, and export

import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('sales_data.csv')
print("✅ Data loaded successfully!\n")
print(df.head())  # Print first 5 rows from imported dataset

# Step 2: Basic info about data
print("\n📘 Dataset Info:")
print(df.info())

print("\n📊 Quick Statistics:")
print(df.describe())

# Step 3: Data cleaning (check for missing values)
print("\n🔍 Checking for missing values:")
print(df.isna().sum())

# Step 4: Convert date column to datetime
df["Date"]=pd.to_datetime(df["Date"])

# Step 5: Add a new column for Profit Margin (%)
df['Profit Margin (%)'] = round((df['Profit']/df['Sales'])*100,2)

# Step 6: Filter - show only rows where sales >1000
high_sales = df[df['Sales']>1000]
print("\n💰 High Sales (>1000):")
print(high_sales)

# Step 7: Group by Product and calculate total sales + avg profit
product_summary =  df.groupby(['Product']).agg(Total_Sales = ('Sales','sum'),Avg_Profit=('Profit','mean')).reset_index()
print("\n📦 Total Sales by Product:")
print(product_summary)

# Step 8: Group by Region
region_summary = df.groupby("Region").agg(
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).reset_index()

print("\n🗺️ Sales by Region:")
print(region_summary)

# Step 9: Find the best performing product and region
best_product = product_summary.loc[product_summary["Total_Sales"].idxmax(), "Product"]
best_region = region_summary.loc[region_summary["Total_Sales"].idxmax(), "Region"]

print(f"\n🏆 Best Product: {best_product}")
print(f"🏆 Best Region: {best_region}")

# Step 10: Save summaries to CSV
product_summary.to_csv("product_summary.csv", index=False)
region_summary.to_csv("region_summary.csv", index=False)
high_sales.to_csv("high_sales.csv", index=False)

print("\n💾 Files saved: product_summary.csv, region_summary.csv, high_sales.csv")
print("\n🎉 Analysis Complete! You're now a Pandas Data Analyst 🚀")