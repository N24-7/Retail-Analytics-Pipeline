import pandas as pd

# Read cleaned data from silver folder
df = pd.read_csv('../silver/cleaned_data.csv')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Extract month and year from InvoiceDate
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# ── GOLD TABLE 1 ──
# Total revenue by country
country_revenue = df.groupby('Country')['Revenue'].sum().reset_index()
country_revenue.columns = ['Country', 'Total_Revenue']
country_revenue = country_revenue.sort_values('Total_Revenue', ascending=False)
country_revenue.to_csv('../gold/country_revenue.csv', index=False)
print("✅ country_revenue.csv saved")

# ── GOLD TABLE 2 ──
# Top 10 products by revenue
top_products = df.groupby('Description')['Revenue'].sum().reset_index()
top_products.columns = ['Product', 'Total_Revenue']
top_products = top_products.sort_values('Total_Revenue', ascending=False).head(10)
top_products.to_csv('../gold/top_products.csv', index=False)
print("✅ top_products.csv saved")

# ── GOLD TABLE 3 ──
# Monthly sales trend
monthly_sales = df.groupby('Month')['Revenue'].sum().reset_index()
monthly_sales.columns = ['Month', 'Total_Revenue']
monthly_sales['Month'] = monthly_sales['Month'].astype(str)
monthly_sales.to_csv('../gold/monthly_sales.csv', index=False)
print("✅ monthly_sales.csv saved")

# ── GOLD TABLE 4 ──
# Top 10 customers by revenue
top_customers = df.groupby('Customer ID')['Revenue'].sum().reset_index()
top_customers.columns = ['Customer_ID', 'Total_Revenue']
top_customers = top_customers.sort_values('Total_Revenue', ascending=False).head(10)
top_customers.to_csv('../gold/top_customers.csv', index=False)
print("✅ top_customers.csv saved")

print("\n🏆 Gold layer complete!")