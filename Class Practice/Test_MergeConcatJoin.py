import pandas as pd

# #...........concat data.............
# ca_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/CAvideos.csv")
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv")
# print(ca_df.shape, gb_df.shape)

# # concat data basis on rows
# concat_data = pd.concat([ca_df, gb_df])
# print(concat_data.shape)
# # concat data basis on columns
# concat_data = pd.concat([ca_df, gb_df], axis=1)
# print(concat_data.shape)
# print(concat_data["video_id"])
# # will print 2 columns having different values, not making any sense for chart
# # it means we should use concat if we would like to append row vise or provide suffix to distinguish column names.


#............join data.......................
#join data - resolve duplicate column issue - show all data no exclusion like SQL joins

# # join data default....
# a_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/CAvideos.csv")
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv")
# print(ca_df.shape, gb_df.shape)
# #join_data = ca_df.join(gb_df)
# #print(join_data.shape)  # print error due to ambiguous column
# join_data = ca_df.join(gb_df, lsuffix='_CA', rsuffix='_GB') # apply suffix to resolve ambiguity error
# print(join_data.shape, join_data.info())

# # join data with single index....
# ca_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/CAvideos.csv").set_index("video_id")
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv").set_index("video_id")
# print(ca_df.shape, gb_df.shape)
# join_data = ca_df.join(gb_df, lsuffix='_CA', rsuffix='_GB')
# print(join_data.shape, join_data.index)
# print(join_data.shape, join_data.info())  # still video id is not available as column
#
# join_data.reset_index(inplace=True)
# # join_index_data = join_data.reset_index()
# print(join_data.index, join_data.info())  # print video_id only once - unique column from both table


# # join data with multi index....
# ca_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/CAvideos.csv").set_index(['title','trending_date'])
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv").set_index(['title','trending_date'])
# print(ca_df.shape, gb_df.shape)
# join_data = ca_df.join(gb_df, lsuffix='_CAN', rsuffix='_UK')
# print(join_data.shape, join_data.index)
# print(join_data.shape, join_data.info())
#
# join_data.reset_index(inplace=True)
# # join_index_data = join_data.reset_index()
# print(join_data.index, join_data.info())  # print title and trending date only once - unique column from both table

# # ................. Merge data..like sql joins................
# ca_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/CAvideos.csv")
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv")
# print(ca_df.shape, gb_df.shape)
#
# merged_data = pd.merge(ca_df, gb_df, on='video_id')
# print(merged_data.shape, merged_data.info())
# # print(merged_data.shape, join_data.shape)
#
# merged_data = pd.merge(ca_df, gb_df, on='video_id', how='left')
# print(merged_data.shape,merged_data.info())
#
# merged_data = pd.merge(ca_df, gb_df, on='video_id', how='right')
# print(merged_data.shape,merged_data.info())
#
# merged_data = pd.merge(ca_df, gb_df[['video_id,'views','likes','dislikes']], on='video_id', how='right')
# print(merged_data.shape,merged_data.info())
