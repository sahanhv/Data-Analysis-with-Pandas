import pandas as pd

df1 = pd.DataFrame({'Name': ['X','Y','Z'],
                    'Age': [17,15,16],
                    'Gender': ['M','F','M']},
                    index = [1,2,3])

df2 = pd.DataFrame({'Name': ['X','Y','Z'],
                    'Age': [17,15,16],
                    'Gender': ['M','F','M']},
                    index = [4,5,6])

df3 = pd.DataFrame({'Name': ['X','Y','Z'],
                    'Age': [17,15,16],
                    'Gender': ['M','F','M']},
                    index = [1,2,3])

#print(df1)
concat = pd.concat([df1,df2])
print(concat)

df4 = df1.append(df2)
print(df4)

s = pd.Series(['A',19,'F'], index = ['Name', 'Age', 'Gender'] )
df5 = df1.append(s, ignore_index = True)

print(df5)
