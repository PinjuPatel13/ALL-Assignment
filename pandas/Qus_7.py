# 7. How might you show the first few rows of data frame? 
import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

df=pd.DataFrame(covid_df)
print(df.head())