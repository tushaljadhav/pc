import os
import pandas as pd

# Practical 1: Text Delimited CSV to HORUS Format
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sInputFileName = os.path.join(BASE_DIR, 'Country_Code.csv')
sOutputFileName = os.path.join(BASE_DIR, 'HORUS-CSV-Country.csv')

# Load input CSV
InputData = pd.read_csv(sInputFileName, encoding="latin-1")

print('Input Data Values ===================================')
print(InputData)
print('=====================================================')

# Process Data: drop unused columns, rename, and set index
ProcessData = InputData.copy()
ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)

ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print('Process Data Values =================================')
print(ProcessData)
print('=====================================================')

# Save to HORUS CSV
ProcessData.to_csv(sOutputFileName, index=False)
print('CSV to HORUS - Done')
