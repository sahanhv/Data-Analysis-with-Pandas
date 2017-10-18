import pandas as pd

df = pd.read_csv('ZILLOW-Z77006_ZRIFAH.csv')
df.set_index('Date', inplace=True)

df.to_csv('test1.csv')

df = pd.read_csv('test1.csv', index_col=0)
print(df.head())

df.columns = ['Austin']
print(df.head())
