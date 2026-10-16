import os
import pandas as pd
import xml.etree.ElementTree as ET

# Practical 3: XML to HORUS Format
# Base directory ensures seamless execution in Python IDLE or terminal
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sInputFileName = os.path.join(BASE_DIR, 'Country_Code.xml')
sOutputFileName = os.path.join(BASE_DIR, 'HORUS-XML-Country.csv')

def xml2df(xml_data):
    root = ET.XML(xml_data)
    all_records = []
    for child in root:
        record = {}
        for subchild in child:
            record[subchild.tag] = subchild.text
        all_records.append(record)
    return pd.DataFrame(all_records)

with open(sInputFileName, 'r', encoding='utf-8') as f:
    InputData = f.read()

print('=====================================================')
print('Input Data Values ===================================')
print('=====================================================')
print(InputData)
print('=====================================================')

# Convert XML to DataFrame and process
ProcessData = xml2df(InputData)

ProcessData.drop('ISO-2-CODE', axis=1, inplace=True)
ProcessData.drop('ISO-3-Code', axis=1, inplace=True)

ProcessData.rename(columns={'Country': 'CountryName'}, inplace=True)
ProcessData.rename(columns={'ISO-M49': 'CountryNumber'}, inplace=True)

ProcessData.set_index('CountryNumber', inplace=True)
ProcessData.sort_values('CountryName', axis=0, ascending=False, inplace=True)

print('=====================================================')
print('Process Data Values =================================')
print('=====================================================')
print(ProcessData)
print('=====================================================')

OutputData = ProcessData
OutputData.to_csv(sOutputFileName, index=False)

print('=====================================================')
print('XML to HORUS - Done')
print('=====================================================')
