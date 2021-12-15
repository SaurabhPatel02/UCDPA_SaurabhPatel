import pandas as pd

netflixdata=pd.read_csv("netflix_titles.csv")
#print(netflixdata)
#print (netflixdata.info())
#print (netflixdata.describe())

#read from local machine different folder
#netdata=pd.read_csv("C:/Users/BYO/PycharmProjects/netflix_titles_diffloc.csv")
#print(netdata)
#print(netdata.head())
#print(netdata.shape)

#print missing value
#missingval = netflixdata.isna()
#print(missingval)
#missingval = netflixdata.isna().sum()
#print(missingval)

#handle missing value
#delete all missing value (default delete from row - axis=0)
#cleaned_data=netflixdata.dropna()
#print(netflixdata.shape,cleaned_data.shape)

#delete all column missing value
#cleaned_data=netflixdata.dropna(axis=1)
#print(netflixdata.shape,cleaned_data.shape)

#delete all missing value by replacing with other value
#cleaned_data=netflixdata.fillna("*")
#print(netflixdata.shape,cleaned_data.shape)
#missingval= cleaned_data.isna().sum()
#print(cleaned_data["director"])
#print(missingval)

#delete all missing value by replacing with mean value
#cleaned_data=netflixdata.fillna(netflixdata.mean)
#print(cleaned_data["director"])

#delete all missing value by replacing with next value
#cleaned_data=netflixdata.fillna(method="bfill")
#missingval= cleaned_data.isna().sum()
#print(cleaned_data)
#print(missingval)
#print(cleaned_data["director"]#will not work if last value is blank

#delete all missing value by replacing with previous value
#cleaned_data=netflixdata.fillna(method="ffill")
#missingval= cleaned_data.isna().sum()
#print(cleaned_data)
#print(missingval)
#print(cleaned_data["director"]) #will not work if first value is blank

#delete all missing value by replacing with next/previous value
#cleaned_data=netflixdata.fillna(method="ffill").fillna(method="bfill")
#missingval= cleaned_data.isna().sum()
#print(cleaned_data)
#print(missingval)
#print(cleaned_data["director"])

#drop duplicates
#drop_duplicates=netflixdata.drop_duplicates()
#print(netflixdata.shape,drop_duplicates.shape)

#drop_duplicates=netflixdata.drop_duplicates(subset=["type"])
#print(netflixdata.shape,drop_duplicates.shape)

#drop_duplicates=netflixdata.drop_duplicates(subset=["type","director","cast"])
#print(netflixdata.shape,drop_duplicates.shape)

print(netflixdata.duplicated())
