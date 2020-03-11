# These are for practice purpose only.

import pandas as pd
# import xlrd
import numpy as np

initial_workbook = 'data1.xlsx'
another_workbook = 'data2.xlsx'
output_workbook = 'output.xlsx'

df_initial = pd.read_excel(initial_workbook)
df_another = pd.read_excel(another_workbook)


# To check columns in each workbook
print(df_initial.columns)
print(df_another.columns)


# Rename the colum to match looking for index, in this case, ids column should match
df_initial.rename(columns={'code': 'ids'}, inplace=True)
df_mg = pd.merge(df_initial, df_another[['ids', 'id']], on='ids', how='left')
print(df_mg)

# Rename back to the inital column name
df_mg.rename(columns={'ids': 'code'}, inplace=True)

# Replace nan value with empty cells
df_mg = df_mg.replace(np.nan, '', regex=True)
print(df_mg)

# Export data to output_workbook excel file
df_mg.to_excel(output_workbook, index=False)

