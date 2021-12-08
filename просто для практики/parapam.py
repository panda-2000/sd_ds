import pandas as pd

countries_data = pd.read_csv('data/melb_data.csv', sep=',')
print(countries_data)

print(round(countries_data.loc[3521,'Landsize']/countries_data.loc[1690, 'Landsize']))


