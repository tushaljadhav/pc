import os
import io
import pandas as pd

# Practical 10: Error Management on Data using Pandas
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(BASE_DIR, 'sample1.csv')

print("--- Practical 10: Error Management with Pandas ---")

try:
    df = pd.read_csv(csv_file)
    print("Original Data:")
    print(df)
    print("\nData Info (before cleaning):")
    df.info()
except FileNotFoundError:
    print("Error: 'sample1.csv' not found. Please create it first.")
    data = """user_id,name,age,email,signup_date
1,Alice,25,alice@email.com,2022-01-10
2,Bob,30,bob@email.com,2022-01-11
3,Charlie,NaN,charlie@email.com,2022-01-12
4,David,'twenty-eight',david@email.com,2022-01-13
5,Alice,25,alice@email.com,2022-01-10
6,Eve,,eve@email.com,2022-01-14
"""
    df = pd.read_csv(io.StringIO(data))
    print("\nLoaded fallback data for demonstration.")
    print(df)

df_cleaned = df.copy()

print("\n--- Starting Data Cleaning Process ---")

# Step 1: Handling Missing Values
if 'age' in df_cleaned.columns:
    df_cleaned['age'] = pd.to_numeric(df_cleaned['age'], errors='coerce')
    median_age = df_cleaned['age'].median()
    df_cleaned['age'] = df_cleaned['age'].fillna(median_age)
    print(f"\nStep 1: Filled missing 'age' values with median age ({median_age}).")

# Step 2: Correcting Data Types
df_cleaned['age'] = df_cleaned['age'].astype(int)
df_cleaned['signup_date'] = pd.to_datetime(df_cleaned['signup_date'], errors='coerce')
print("Step 2: Corrected data types for 'age' (to int) and 'signup_date' (to datetime).")

# Step 3: Removing Duplicate Rows
initial_rows = len(df_cleaned)
df_cleaned.drop_duplicates(inplace=True)
final_rows = len(df_cleaned)
print(f"Step 3: Removed {initial_rows - final_rows} duplicate row(s).")

print("\n--- Data After Cleaning ---")
print(df_cleaned)
print("\nCleaned Data Info:")
df_cleaned.info()

print("\n--- Error Management Practical Complete ---")
