# 6. Write the code to show the number of rows and columns in data frame. 
import pandas as pd

covid_df = pd.read_csv('italy-covid-daywise.csv')

df=pd.DataFrame(covid_df)
# print(df)

print("Number of Rows:",df.shape[0])
print("Number of Column:",df.shape[1])
