import pandas as pd
import csv
import requests

data = 'https://lazyprogrammer.me/course_files/all_stocks_5yr.csv'

resp = requests.get(data)
lines = resp.text.splitlines()
reader = csv.reader(lines)
parsed_csv = list(reader)

date_columns = ['date']
numeric_columns = ['open', 'high', 'low', 'close', 'volume']
string_columns = ['Name']
df = pd.DataFrame(parsed_csv[1:],columns=parsed_csv[0])
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col])

for col in date_columns:
    df[col] = pd.to_datetime(df[col])

ibm = df[df['Name'] == 'IBM']
