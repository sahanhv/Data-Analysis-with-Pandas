import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[42,34,56,74,23,12],
             'Bounce_rates':[66,72,34,56,78,66]}

df = pd.DataFrame(web_stats)

#df.set_index('Day', inplace=True)
#print(df.head())

#print(df.Visitors)
print(np.array(df[['Visitors', 'Bounce_rates']]))
df2 = pd.DataFrame(np.array(df[['Visitors', 'Bounce_rates']]))
print(df2)
