import pandas as pd

csv_file = 'coin.csv'
df = pd.read_csv(csv_file)
print(df.columns)
print(df.head(5))
new_df = df.loc[:, "Currency":"Closing Price (USD)"]
print(new_df)

# Number of entries to calculate on -> windows
simple_moving_average = new_df.rolling(window=7, on='Date').mean()
print(simple_moving_average)

