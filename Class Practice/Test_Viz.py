import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#
# # plot blank chart
# fig, ax= plt.subplots()
# #plt.show()
#
# # define values
# x = [1,2,3,4,5,6]
# y = [1,2,3,4,5,6]
# z = [2,4,6,8,10,12]
#
# # plot line chart
# plt.plot(x,y)
# #plt.show()
# # plot bar chart
# plt.bar(x,y)
# #plt.show()
# # plot scatter chart
# plt.scatter(x,y)
# #plt.show()
# # plot multiple chart together
# plt.scatter(x,y)
# plt.plot(x,z)
# #plt.show()
# # change line style
# # https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# plt.plot(x,z, linestyle="dashed")
# #plt.show()
# # change marker
# # https://matplotlib.org/stable/api/markers_api.html
# plt.plot(x,z, marker="v")
# #plt.show()
# # change color
# # https://matplotlib.org/stable/gallery/color/named_colors.html
# plt.plot(x,z, color="r")
# #plt.show()
# # plot all together
# plt.plot(x,z, linestyle="dashed",marker="o",color="r")
# #plt.show()
#
# # ............implement chart from real time data ......................
# # import data set
# gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBVideos.csv")
# #gb_df = pd.read_csv("Data/GBvideos.csv") -- getting error with content root path
# print(gb_df.shape)
# print(gb_df.head())
#
# # chart with matplot lib
# # determine x and y-axis with top 5 rows
# x = gb_df['channel_title'].head(5)
# y1 = gb_df['views'].head(5)
# y2 = gb_df['likes'].head(5)
# # plot axis
# ax.plot(x, y1)
# #plt.show()
# ax.plot(x, y2)
# #plt.show()
# # custom plot
# ax.plot(x, y1, marker="v", linestyle="--", color="b")
# #plt.show()
#
# # chart with seaborn lib
# sns.lineplot(x=gb_df['video_id'].head(25),
# y=gb_df['views'].head(25))
# #plt.show()
#
# # https://matplotlib.org/stable/gallery/index.html
#
# ..........implement chart from seaborn gallary..........................
# https://seaborn.pydata.org/examples/index.html

# chart 1 - Scatterplot with categorical variables.......
# https://seaborn.pydata.org/examples/scatterplot_categorical.html
sns.set_theme(style="whitegrid", palette="muted") # set display theme
# load load prediction data
trng_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/Train_LoanPredictionData.csv")
# draw a categorical scatterplot to show each observation
ax = sns.swarmplot(data=trng_df, x="LoanAmount", y="Gender", hue="Property_Area")
ax.set(ylabel="")
plt.show()

# chart 2 - Stripplot with categorical variables...........
# https://seaborn.pydata.org/generated/seaborn.stripplot.html?highlight=stripplot#seaborn.stripplot
# draw a categorical stripplot to show each observation
ax = sns.stripplot(x="Gender", y="LoanAmount", hue="Property_Area", data=trng_df)
plt.show()