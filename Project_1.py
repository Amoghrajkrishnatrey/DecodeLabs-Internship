import os
import pandas as pd

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "Dataset for Data Analytics - Sheet1.csv")

df = pd.read_csv(file_path)

print("Initial dataset shape:", df.shape)

df['CouponCode'] = df['CouponCode'].fillna('NONE')

initial_count = len(df)
df = df.drop_duplicates(subset=['OrderID'], keep='first')
print(f"Removed {initial_count - len(df)} duplicate records.")

df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

text_cols = ['Product', 'PaymentMethod', 'OrderStatus', 'ReferralSource']
for col in text_cols:
    df[col] = df[col].astype(str).str.strip().str.title()

df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = (df['Quantity'] * df['UnitPrice']).round(2)

cleaned_file_path = os.path.join(script_dir, "Cleaned_Dataset_Project1.csv")
df.to_csv(cleaned_file_path, index=False)
print("Data cleaning completed. Saved as:", cleaned_file_path)
