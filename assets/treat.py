import pandas as pd


excel_file = 'MEDICAMENTS.xlsx'
df = pd.read_excel(excel_file)
print(df.head())
print(df.columns)
