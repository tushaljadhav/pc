import os
import pandas as pd

# Practical 7: Retrieve Different Attributes of Data
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(BASE_DIR, "IP_DATA_ALL.csv")

ip_data_all = pd.read_csv(filename)

print("--- Loaded Data ---")
print(ip_data_all)

print("\n--- Data Structure ---")
print(ip_data_all.info())

print("\n--- Statistical Summary ---")
print(ip_data_all.describe())

print("\n--- Column Names ---")
print(list(ip_data_all.columns))
