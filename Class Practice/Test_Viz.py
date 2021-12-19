import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# chart 1 - plot blank chart with only axis and figure
fig, ax = plt.subplots()
# plt.show()

# define variable and assign dummy values
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5, 6]
z = [2, 4, 6, 8, 10, 12]
# y2 = [2,4,6,8] to print error in case of missing value
y3 = [2, 4, None, 8, 10, 12]

# chart 2 - plot line chart
fig, ax = plt.subplots()
plt.plot(x, y)
# plt.show()

# chart 3 - plot bar chart
fig, ax = plt.subplots()
plt.bar(x, y)
# plt.show()

# chart 4 - plot scatter chart
fig, ax = plt.subplots()
plt.scatter(x, y)
# plt.show()

# chart 5 - plot multiple chart together
fig, ax = plt.subplots()
plt.scatter(x, y)
plt.plot(x, z)
# plt.show()

# chart 6 - change line style
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
fig, ax = plt.subplots()
plt.plot(x, z, linestyle="dashed")

# chart 7 - change marker
# https://matplotlib.org/stable/api/markers_api.html
fig, ax = plt.subplots()
plt.plot(x, z, marker="v")
# plt.show()

# chart 8 - change color
# https://matplotlib.org/stable/gallery/color/named_colors.html
fig, ax = plt.subplots()
plt.plot(x, z, color="r")
# plt.show()

# chart 9 - plot line chart with missing values'
# fig, ax = plt.subplots()
# plt.plot(x, y2)
# plt.show()

# chart 10 - plot line chart with null/blank values
fig, ax = plt.subplots()
plt.plot(x, y3)
# plt.show()

# chart 11 - plot all together
fig, ax = plt.subplots()
plt.scatter(x, y)
plt.plot(x, z, linestyle="dashed", marker="o", color="r")
# plt.show()

# ............implement chart from real time data ......................
# import data set
gb_df = pd.read_csv("C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/GBvideos.csv")
# gb_df = pd.read_csv("Data/GBvideos.csv") #-- getting error with content root path
print(gb_df.shape)
print(gb_df.head())

# chart with matplot lib.......................
# chart 12 - matplot lib based chart
# determine x and y-axis with top 5 rows
x = gb_df['channel_title'].head(5)
y1 = gb_df['views'].head(5)
y2 = gb_df['likes'].head(5)
# custom plot
fig, ax = plt.subplots()
ax.plot(x, y1, marker="v", linestyle="--", color="b")
# plt.show()

# chart with seaborn lib....................
# chart 13 - seaborn lib based chart
fig, ax = plt.subplots()
sns.lineplot(x=gb_df['video_id'].head(25), y=gb_df['views'].head(25))
plt.show()

# ....chart will be displayed here individually...please wait for 3secs after all above chart print....
# https://matplotlib.org/stable/gallery/index.html
# ..........implement chart 14x from seaborn gallery..........................
# https://seaborn.pydata.org/examples/index.html
sns.set_theme(style="whitegrid", palette="muted")  # set display theme
trng_df = pd.read_csv(
    "C:/Users/BYO/PycharmProjects/UCDPA_SaurabhPatel/Data/Train_LoanPredictionData.csv")  # load load prediction data

# chart 14.1 - Scatterplot with categorical variables.......
# https://seaborn.pydata.org/examples/scatterplot_categorical.html
# draw a categorical scatterplot to show each observation
ax = sns.swarmplot(data=trng_df, x="LoanAmount", y="Gender", hue="Property_Area")
ax.set(ylabel="")
plt.show()

# chart 14.2 - Stripplot with categorical variables...........
# https://seaborn.pydata.org/generated/seaborn.stripplot.html?highlight=stripplot#seaborn.stripplot
# draw a categorical stripplot to show each observation
ax = sns.stripplot(x="Gender", y="LoanAmount", hue="Property_Area", data=trng_df)
plt.show()

# chart 14.3 - Joint plot with categorical variables...........
# draw a categorical joint plot to show each observation
# https://seaborn.pydata.org/examples/joint_kde.html
g = sns.jointplot(
    data=trng_df,
    x="Loan_Amount_Term", y="LoanAmount", hue="Education",
    kind="kde",
)
plt.show()

# chart 14.4 - pair plot with categorical variables...........
# draw a categorical pair plot to show each observation
# https://seaborn.pydata.org/examples/scatterplot_matrix.html
sns.pairplot(trng_df, vars=['ApplicantIncome', 'CoapplicantIncome'], hue="Loan_Status", markers=["o", "s"])
plt.show()
