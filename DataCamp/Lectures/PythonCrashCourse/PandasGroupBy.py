#Pandas Group By

import numpy as np
import pandas as pd

data = {'Company':['Google','Google','Google','Amazon','Amazon','Amazon','Facebook','Facebook','Twitter'],
        'Person':['Anvesh','Maximus','Decimus','Meridius','Naruto','Sasuke','Sunio','Nobita','Gian'],
        'Sales':[100,55,44,33,66,78,34,87,45],
        'Age':[22,23,12,34,45,34,33,22,66]}

df = pd.DataFrame(data)

grpby = df.groupby('Company')

print(grpby.describe().transpose()['Amazon'])

print(df.groupby('Company').sum().loc['Google'])
