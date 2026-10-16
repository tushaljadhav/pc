import os
import pandas as pd

# Practical 6: Create Sample Dataset
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(BASE_DIR, "IP_DATA_ALL.csv")

ip_data_sample = pd.DataFrame({
    'ID': ["ID001", "ID002", "ID003", "ID004", "ID005"],
    'IP_Address': ["192.168.1.1", "203.0.113.10", "10.0.0.5", "172.16.31.40", "198.51.100.22"],
    'Country': ["USA", "Germany", "Canada", "USA", "Japan"],
    'Latitude': [40.7128, 52.5200, 43.6532, 41.8781, 35.6895],
    'Longitude': [-74.0060, 13.4050, -79.3832, -87.6298, 139.6917],
    'Place Name': ["New York", "Berlin", "Toronto", "Chicago", "Tokyo"],
    'Test IP Number': [3232235777, 3405803786, 167772165, 2886755112, 3325256726],
    'Last IP Number': [3232235778, 3405803787, 167772166, 2886755113, 3325256727]
})

ip_data_sample.to_csv(output_file, index=False)
print("Sample file 'IP_DATA_ALL.csv' has been created successfully.")
