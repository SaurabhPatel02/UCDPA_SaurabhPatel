# import data

import pandas as pd
netflix_data = pd.read_csv("netflix_titles.csv")
print(netflix_data)
netflix_data.info()
print(netflix_data.describe())  
