import pandas as pd
import psycopg2
from psycopg2 import extras

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="retail_db",
    user="postgres",
    password="your_password"
)

cursor = conn.cursor()

# Read cleaned data from silver folder
df = pd.read_csv('../silver/cleaned_data.csv')

# Convert dataframe to list of tuples
records = df.values.tolist()

# Insert data into sales table
insert_query = """
INSERT INTO sales 
(Invoice, StockCode, Description, Quantity, InvoiceDate, Price, CustomerID, Country, Revenue)
VALUES %s
"""

extras.execute_values(cursor, insert_query, records)

conn.commit()
cursor.close()
conn.close()

print(f"✅ {len(df)} rows loaded into PostgreSQL successfully!")
