# 5. take csv file contains at least 10,000 rows and 12 columns which numerical and text values 
# according to that continue following steps.

import pandas as pd
covid_df = pd.read_csv('italy-covid-daywise.csv')
print(covid_df)

