import pandas as pd


StartupFund = pd.read_csv('C:/Users/Anvesh/Desktop/Learning/Kaggle/Datasets/startup_funding.csv')

#d2 = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')

#d2.to_excel('C:/Users/Anvesh/Desktop/Learning/Python/Python_DS_and_ML/Python-for-Data-Analysis/Pandas/Excel_Sample2.xlsx',sheet_name= 'jumanji')
#d3 = pd.DataFrame(d2)

#StartupFund.to_excel('C:/Users/Anvesh/Desktop/Learning/Kaggle/Datasets/startup_fundings.xlsx',sheet_name='Sheet1',index=False)

print(StartupFund.info())
