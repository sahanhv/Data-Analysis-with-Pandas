import quandl
import pandas as pd
import html5lib

api = '1NNAby9LKg-Wwsjk3txG'

df = quandl.get('FMAC/HPI_AK', authtoken = api)

print(df.head())

states = pd.read_html('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')

print(states[0][1])

for abbv in states[0][1][1:]:
    print('FMAC/HPI'+str(abbv))
