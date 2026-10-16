import os
import re
import pandas as pd

# Practical 8: Identify and Fix Data Patterns (Problematic Column Names)
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(BASE_DIR, "IP_DATA_ALL.csv")

ip_data_all = pd.read_csv(filename)

print("--- (a) Column Data Types & Specifications ---")
print(ip_data_all.dtypes)
print("\nOriginal Column Names with spaces/formatting:")
print(list(ip_data_all.columns))

def clean_col_name(col):
    col = col.strip().lower()
    col = re.sub(r'[^a-zA-Z0-9_]+', '_', col)
    return col

ip_data_all_clean = ip_data_all.copy()
ip_data_all_clean.columns = [clean_col_name(c) for c in ip_data_all_clean.columns]

print("\n\n--- Cleaned Column Names ---")
print(list(ip_data_all_clean.columns))

print("\n\n--- Data Frame with Cleaned Names ---")
print(ip_data_all_clean)
