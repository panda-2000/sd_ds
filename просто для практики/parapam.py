import pandas as pd

sp = pd.read_csv('data/melb_data_ps.csv', sep=',')
spc=sp.copy()
spc['Date']=pd.to_datetime(spc['Date'])
ys=(spc['Address'].loc[9001])
print(ys)

