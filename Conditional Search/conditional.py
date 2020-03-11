import numpy as np
import pandas as pd

excel_file = 'condition.xlsx'

# Read  and print contents of excel file
df = pd.read_excel(excel_file)
print(df)


# Filter only the column occupation meets engineer condition
# print(df['Name'].where(df['Occupation'] == 'Engineer'))
# engineers = df['Name'].where(df['Occupation'] == 'Engineer')
# print(engineers.dropna())

# excel_files = ['condition.xlsx', 'condition_copy.xlsx', 'condition_copy2.xlsx']
# for indivisual_excel in excel_files:
#     print(pd.read_excel(indivisual_excel))


# Create an array for 
excel_files = ['condition.xlsx', 'condition_copy.xlsx', 'condition_copy2.xlsx']

for indivisual_excel in excel_files:
    df = pd.read_excel(indivisual_excel)
    engineers = df['Name'].where(df['Occupation'] == 'Engineer').dropna()
    print("Filename :" + indivisual_excel)
    print(engineers)


