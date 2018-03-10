# Dealing with Missing data iin Pandas

import numpy as np
import pandas as pd

population = [[1999,2344,1233,np.nan,np.nan,3455],
              [np.nan,np.nan,4567,4343,5676,np.nan],
              [3456,7654,9876,8766,4545,2111],
              [np.nan,np.nan,np.nan,4322,2322],
              [3422,1212,2222,2344,np.nan,np.nan],
              [np.nan,1234,np.nan,3456,np.nan,3434]]

years = [2000,2001,2002,2003,2004,2005]

countries = ['USA','China','India','Russia','Japan','Pakistan']

data = pd.DataFrame(data= population, index=countries, columns =years)

print(data)
