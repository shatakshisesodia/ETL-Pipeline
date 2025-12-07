import pandas as pd
import numpy as np
from datetime import datetime

# 1.Read data from Rawzone

raw_path = "raw_data.csv"
df = pd.read_csv(raw_path)

print ("RAW DATA LOADED")
print(df.head())



# 2.Data Cleaning

# fill missing names with "unknown"
df['name'] = df['name'].fillna('unknown')

# fill missing age with median age
df['age'] = df['age'].fillna(df['age'].median())

# fill missing country with "not specified"
df['country'] = df['country'].fillna('not specified')

# Fill missing purchase amount with 0
df['purchase_amount'] = df['purchase_amount'].fillna(0)

# Convert purchase_date to datetime
df['purchase_date'] = pd.to_datetime(df['purchase_date'], errors ='coerce')

# Replace null dates with today's date
df['purchase_date'] = df['purchase_date'].fillna(datetime.now())


# 3. Data Transformation

# Add category: High Value or Low Value
df['purchase_amount'] = np.where(df['purchase_amount']>200, "High value", "Low Value")

# Add year column
df['purchase_date'] = df['purchase_date'].dt.year

# 4. WRITE TO STAGING ZONE
staging_path = "staging_output.xlsx"
df.to_excel(staging_path, index=False)

print("\nCLEANED & TRANSFORMED DATA SAVED TO STAGING ZONE")
print(f"File saved as: {staging_path}")


