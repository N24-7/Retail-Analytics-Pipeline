import pandas as pd

# Read raw data from bronze folder
df = pd.read_csv('../bronze/online_retail_II.csv')

# Check shape before cleaning
print(f"Before cleaning: {df.shape}")

# Remove rows where Customer ID is missing
df = df.dropna(subset=['Customer ID'])

# Remove cancelled orders (negative quantity)
df = df[df['Quantity'] > 0]

# Remove rows where price is zero or negative
df = df[df['Price'] > 0]

# Remove rows where product description is missing
df = df.dropna(subset=['Description'])

# Convert InvoiceDate from string to proper datetime format
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Convert Customer ID from float to integer
df['Customer ID'] = df['Customer ID'].astype(int)

# Create new column Revenue = Quantity * Price
df['Revenue'] = df['Quantity'] * df['Price']

# Check shape after cleaning
print(f"After cleaning: {df.shape}")

# Check if any missing values remain
print("\n=== MISSING VALUES AFTER CLEANING ===")
print(df.isnull().sum())

# Preview first 5 rows
print("\n=== FIRST 5 ROWS ===")
print(df.head())

# Save cleaned data to silver folder
df.to_csv('../silver/cleaned_data.csv', index=False)

print("\n✅ Cleaned data saved to silver/cleaned_data.csv")