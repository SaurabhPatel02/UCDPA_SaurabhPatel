# -------------- Merge data frames using concat/join/merge -----------------------
# data source URL : https://www.kaggle.com/datasnaek/youtube-new

# import library
import pandas as pd

# ------------combine data with concat function------------------------
ca_df = pd.read_csv("Input Data/CAvideos.csv")
gb_df = pd.read_csv("Input Data/GBvideos.csv")
print(ca_df.shape, gb_df.shape)

# concat data basis on rows
concat_df = pd.concat([ca_df, gb_df])
print(concat_df.shape)
# concat data basis on columns
concat_df = pd.concat([ca_df, gb_df], axis=1)
print(concat_df.shape)
print(concat_df["video_id"])

# conclusion for concat : this will print 2 columns having different values and will not make meaningful information
# to plot chart it means we should use concat if we would like to append row vise or provide suffix to distinguish
# column names.


# ------------combine data with join function------------------------
# join data - resolve duplicate column issue raised in concat - show all data no exclusion like SQL joins

# join data with default option....
ca_df = pd.read_csv("Input Data/CAvideos.csv")
gb_df = pd.read_csv("Input Data/GBvideos.csv")
print(ca_df.shape, gb_df.shape)
# join_df = ca_df.join(gb_df)
# print(join_df.shape)  # throw error due to ambiguous column
join_df = ca_df.join(gb_df, lsuffix='_CA', rsuffix='_GB')  # apply suffix to resolve ambiguity error
print(join_df.shape, join_df.info())

# join data with single index....
ca_df = pd.read_csv("Input Data/CAvideos.csv").set_index("video_id")
gb_df = pd.read_csv("Input Data/GBvideos.csv").set_index("video_id")
print(ca_df.shape, gb_df.shape)
join_df = ca_df.join(gb_df, lsuffix='_CA', rsuffix='_GB')
print(join_df.shape, join_df.index)
print(join_df.shape, join_df.info())  # still video id is not available as column

join_df.reset_index(inplace=True)
# join_index_df = join_data.reset_index()
print(join_df.index, join_df.info())  # print video_id only once - unique column from both table


# join data with multi index....
ca_df = pd.read_csv("Input Data/CAvideos.csv").set_index(['title', 'trending_date'])
gb_df = pd.read_csv("Input Data/GBvideos.csv").set_index(['title', 'trending_date'])
print(ca_df.shape, gb_df.shape)
join_df = ca_df.join(gb_df, lsuffix='_CAN', rsuffix='_UK')
print(join_df.shape, join_df.index)
print(join_df.shape, join_df.info())

join_df.reset_index(inplace=True)
# join_index_data = join_data.reset_index()
print(join_df.index, join_df.info())  # print title and trending date only once - unique column from both table


# ------------combine data with merge function------------------------
# works as sql join function
ca_df = pd.read_csv("Input Data/CAvideos.csv")
gb_df = pd.read_csv("Input Data/GBvideos.csv")
print(ca_df.shape, gb_df.shape)

# merge data with default option
merged_df = pd.merge(ca_df, gb_df, on='video_id')
print(merged_df.shape, merged_df.info())
# print(merged_data.shape, join_data.shape)

# merge with left join
merged_df = pd.merge(ca_df, gb_df, on='video_id', how='left')
print(merged_df.shape, merged_df.info())

# merge with right join
merged_df = pd.merge(ca_df, gb_df, on='video_id', how='right')
print(merged_df.shape, merged_df.info())

# extract merged data with right join for verification to Output Data directory
merged_df.to_csv("Output Data/5_Merged_CAGBvideos_Data.csv")

# merge with right join with limited set of columns from right table 'GBvideos.csv'
merged_df = pd.merge(ca_df, gb_df[['video_id', 'views', 'likes', 'dislikes']], on='video_id', how='right')
print(merged_df.shape, merged_df.info())
