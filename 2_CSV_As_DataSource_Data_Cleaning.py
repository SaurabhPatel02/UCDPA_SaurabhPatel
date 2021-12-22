# -------------- Data import and cleaning using CSV as source -----------------------
# data source : https://www.kaggle.com/shivamb/netflix-shows

# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------- netflix data cleaning ---------------------

# import netflix data from Input Data directory
netflix_df = pd.read_csv("Input Data/netflix_titles.csv")
print(netflix_df, netflix_df.info(), netflix_df.describe())

# print missing value
print(netflix_df.isna().sum())

# handle missing values
netflix_df['cast'].replace(np.nan, 'No data', inplace=True)
netflix_df['director'].replace(np.nan, 'No data', inplace=True)
netflix_df['country'] = netflix_df['country'].fillna(netflix_df['country'].mode()[0])
netflix_df.dropna(inplace=True)
print(netflix_df.isna().sum())

# handle duplicates
print(netflix_df.duplicated())
netflix_drop_duplicates = netflix_df.drop_duplicates()
print(netflix_df.shape, netflix_drop_duplicates.shape)

# extract cleaned data for verification to Output Input Data directory
netflix_df.to_csv("Output Data/2_Netflix_Cleaned_Data.csv")

# visualize top 10 countries with most shows on netflix
sns.set(style='whitegrid')
plt.figure(figsize=(15, 10))
chart = sns.countplot(y=netflix_df['country'], order=netflix_df.country.value_counts().index[:10])
plt.title('Countries with most shows on Netflix')
plt.show()

# -------------------data cleaning practice code with netflix data ------------------
# netflix_data = pd.read_csv("Input Data/netflix_titles.csv")
# print(netflix_data)
# print (netflix_data.info())
# print (netflix_data.describe())

# read from local machine different folder
# netdata=pd.read_csv("C:/Users/BYO/PycharmProjects/netflix_titles_other_location.csv")
# print(netdata)
# print(netdata.head())
# print(netdata.shape)

# print missing value
# missing_val = netflix_data.isna()
# print(missing_val)
# missing_val = netflix_data.isna().sum()
# print(missing_val)

# handle missing value
# delete all missing value (default delete from row - axis=0)
# cleaned_data=netflix_data.dropna()
# print(netflix_data.shape,cleaned_data.shape)

# delete all column missing value
# cleaned_data=netflix_data.dropna(axis=1)
# print(netflix_data.shape,cleaned_data.shape)

# handle all missing value by replacing with other value
# cleaned_data=netflix_data.fillna("*")
# print(netflix_data.shape,cleaned_data.shape)
# missing_val= cleaned_data.isna().sum()
# print(cleaned_data["director"])
# print(missing_val)

# handle all missing value by replacing with mean value
# cleaned_data=netflix_data.fillna(netflix_data.mean)
# print(cleaned_data["director"])

# handle all missing value by replacing with next value
# cleaned_data=netflix_data.fillna(method="bfill")
# missing_val= cleaned_data.isna().sum()
# print(cleaned_data)
# print(missing_val)
# print(cleaned_data["director"]#will not work if last value is blank

# handle all missing value by replacing with previous value
# cleaned_data=netflix_data.fillna(method="ffill")
# missing_val= cleaned_data.isna().sum()
# print(cleaned_data)
# print(missing_val)
# print(cleaned_data["director"]) #will not work if first value is blank

# handle all missing value by replacing with next/previous value
# cleaned_data=netflix_data.fillna(method="ffill").fillna(method="bfill")
# missing_val= cleaned_data.isna().sum()
# print(cleaned_data)
# print(missing_val)
# print(cleaned_data["director"])

# drop duplicates
# drop_duplicates=netflix_data.drop_duplicates()
# print(netflix_data.shape,drop_duplicates.shape)

# drop_duplicates=netflix_data.drop_duplicates(subset=["type"])
# print(netflix_data.shape,drop_duplicates.shape)

# drop_duplicates=netflix_data.drop_duplicates(subset=["type","director","cast"])
# print(netflix_data.shape,drop_duplicates.shape)

# print(netflix_data.duplicated())
