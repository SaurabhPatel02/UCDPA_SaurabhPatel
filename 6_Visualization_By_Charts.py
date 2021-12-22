# -------------- Visualize data with matplotlib and sea born charts -----------------------
# data source URL :
# GBvideos - https://www.kaggle.com/datasnaek/youtube-new
# Loan Prediction - https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset

# Chart reference :
# matplotlib gallery - https://matplotlib.org/stable/gallery/index.html
# seaborn gallery - https://seaborn.pydata.org/examples/index.html
# chart 1 - https://seaborn.pydata.org/examples/scatterplot_categorical.html
# chart 2 - https://seaborn.pydata.org/generated/seaborn.stripplot.html?highlight=stripplot#seaborn.stripplot
# chart 3 - https://seaborn.pydata.org/examples/joint_kde.html
# chart 4 - https://seaborn.pydata.org/examples/scatterplot_matrix.html
# color palette - https://matplotlib.org/stable/gallery/color/named_colors.html
# line styles - https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
# markers - https://matplotlib.org/stable/api/markers_api.html

# import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# .....plot advance chart using loan prediction data set and seaborn gallery.........
sns.set_theme(style="whitegrid", palette="muted")  # set display theme
trng_df = pd.read_csv("Input Data/Train_LoanPredictionData.csv")  # load loan prediction data

# chart 1 - plot Swarmplot with categorical variables.......
fig, ax = plt.subplots(figsize=(10, 10))
ax = sns.swarmplot(data=trng_df, x="LoanAmount", y="Gender", hue="Property_Area")
ax.set(ylabel="")
plt.title('Seaborn-Swarmplot - Gender basis Loan Amount distribution for a property area')
# plt.show()

# chart 2 - plot Stripplot with categorical variables...........
fig, ax = plt.subplots(figsize=(10, 10))
sns.stripplot(x="Gender", y="LoanAmount", hue="Property_Area", data=trng_df)
plt.title('Seaborn-Stripplot - Gender basis Loan Amount distribution for a property area')
# plt.show()

# chart 3 - plot Jointplot with categorical variables...........
# fig, ax = plt.subplots(figsize=(10, 10))
sns.jointplot(
    data=trng_df,
    x="Loan_Amount_Term", y="LoanAmount", hue="Education",
    kind="kde",
                )
plt.title('Seaborn-Joint plot')
# plt.show()

# chart 4 - plot pairplot with categorical variables...........
# fig, ax = plt.subplots(figsize=(10, 10))
sns.pairplot(trng_df, vars=['ApplicantIncome', 'CoapplicantIncome'], hue="Loan_Status",  markers=["o", "s"])
plt.title('Seaborn-Pair plot matrix')
# plt.show()


# ------------ class practice - plot sample charts on dummy data --------------------------
# ...........plot simple charts using GBvideos dataset...............
gb_df = pd.read_csv("Input Data/GBvideos.csv")   # import data set
print(gb_df.shape, gb_df.head())

# chart 12 - plot line chart with matplot lib...........
# determine x and y-axis with top 5 rows
x = gb_df['channel_title'].head(5)
y1 = gb_df['views'].head(5)
y2 = gb_df['likes'].head(5)
# custom plot
# plt.figure(figsize=(10, 10))
fig, ax = plt.subplots(figsize=(10, 10))
plt.plot(x, y1, marker="v", linestyle="--", color="b")
plt.title('Matplotlib chart - views and likes distribution by channel')
# plt.show()

# chart 13 - plot line chart with seaborn lib............
fig, ax = plt.subplots(figsize=(10, 10))
sns.lineplot(x=gb_df['video_id'].head(25), y=gb_df['views'].head(25))
plt.title('Seaborn chart - views distribution by video id')
plt.show()

# # define variable and assign dummy values
# x = [1, 2, 3, 4, 5, 6]
# y = [1, 2, 3, 4, 5, 6]
# z = [2, 4, 6, 8, 10, 12]
# # y2 = [2,4,6,8] to print error in case of missing value
# y3 = [2, 4, None, 8, 10, 12]
#
# # chart 1 - plot blank chart with only axis and figure
# fig, ax = plt.subplots()
# plt.title('Blank Chart - only axis and figure')
# # plt.show()
#
# # chart 2 - plot line chart
# fig, ax = plt.subplots()
# plt.plot(x, y)
# plt.title('Line Chart')
# # plt.show()
#
# # chart 3 - plot bar chart
# fig, ax = plt.subplots()
# plt.bar(x, y)
# plt.title('Bar Chart')
# # plt.show()
#
# # chart 4 - plot scatter chart
# fig, ax = plt.subplots()
# plt.scatter(x, y)
# plt.title('Scatter Plot Chart')
# # plt.show()
#
# # chart 5 - plot line chart with missing values'
# # fig, ax = plt.subplots()
# # plt.plot(x, y2)
# # plt.show()
#
# # chart 6 - plot line chart with null/blank values'
# fig, ax = plt.subplots()
# plt.plot(x, y3)
# plt.title('Line Chart with null value')
# # plt.show()
#
# # chart 7 - plot multiple chart together
# fig, ax = plt.subplots()
# plt.scatter(x, y)
# plt.plot(x, z)
# plt.title('Combine scatter and line Chart')
# # plt.show()
#
# # chart 8 - change line style
# fig, ax = plt.subplots()
# plt.plot(x, z, linestyle="dashed")
# plt.title('Line Chart with dashed line style')
#
# # chart 9 - change marker
# fig, ax = plt.subplots()
# plt.plot(x, z, marker="v")
# plt.title('Line Chart with specific marker')
# # plt.show()
#
# # chart 10 - change color
# fig, ax = plt.subplots()
# plt.plot(x, z, color="r")
# plt.title('Line Chart with red color')
# # plt.show()
#
# # chart 11 - plot all together
# fig, ax = plt.subplots()
# plt.scatter(x, y)
# plt.plot(x, z, linestyle="dashed", marker="o", color="r")
# plt.title('Combine chart with marker, color and style')
# # plt.show()
