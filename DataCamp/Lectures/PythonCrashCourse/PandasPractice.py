#Pandas Tutorials

import numpy as np
import pandas as pd

lbls = ['a','b','c','d','e']
vals = [1,2,3,4,5]
tups = (1,2,3,4,5)
dics = {'a':1,'b':2,'c':3,'d':4,'e':5}

pseries1 = pd.Series(vals,lbls )
pseries2 = pd.Series(lbls)
pseries3 = pd.Series(dics)
'''
print(pseries1)
print(pseries2)
print(pseries3)
print(pseries1 + pseries3)
'''
#DataFrames
np.random.seed(1) #To keep the randn values same for all the runs
df = pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
'''
print(df)
print(df['W'])
print(df[['W','Z']])

#creating a new column in df

df['new'] = df['W'] + df['Y']

print(df)

print(df.drop('new',axis=1)) #it does not actually delete the data

print(df)

#in order to delte the data we have to mention inplace = True and specify the axis as 1 for column

df.drop('new',axis=1,inplace=True)

print(df)

#To drop a row

print(df.drop('E',axis=0))

df.drop('E',axis = 0,inplace=True)

print(df)

#selecting rows
print(df.loc['A'])

print(df.iloc[2])

print(df.loc['B','Y'])


print(df.loc[['A','B'],['W','Y']])

print(df)
print(df.loc['A'])
print(df[(df['W']>0) & (df['Y'] > 1)])


#print(df.reset_index())
newind = 'CA NY WY OR CO'.split()
df['States'] = newind

print(df)

df.set_index('States',inplace=True)

print(df)

'''

#Multilevel Indexing
