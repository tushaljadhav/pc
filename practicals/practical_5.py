import os
import pandas as pd

# Practical 5: Averaging of Data
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
InputFileName = os.path.join(BASE_DIR, 'IP_DATA_CORE.csv')

IP_DATA_ALL = pd.read_csv(InputFileName, header=0, low_memory=False,
                          usecols=['Country', 'Place Name', 'Latitude', 'Longitude'], encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name': 'Place_Name'}, inplace=True)
AllData = IP_DATA_ALL[['Country', 'Place_Name', 'Latitude']]
print(AllData)
MeanData = AllData.groupby(['Country', 'Place_Name'])['Latitude'].mean()
print(MeanData)
