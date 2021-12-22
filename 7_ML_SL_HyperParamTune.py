# -------------- Predict the target variable using ML -----------------------
# data source URL :
# Loan Prediction - https://www.kaggle.com/altruistdelhite04/loan-prediction-problem-dataset

# import packages/libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import cross_val_score
from scipy.stats import randint
from sklearn.model_selection import RandomizedSearchCV
import warnings

# handle warnings
warnings.filterwarnings("ignore")

# 1. Input Data Collection..................................................................

trng_path = "Input Data/Train_LoanPredictionData.csv"  # path for the training data sets
test_path = "Input Data/Test_LoanPredictionData.csv"  # path for the testing data sets

# read train data set csv files as a DataFrame
trng_df = pd.read_csv(trng_path)
trng_df.head()  # explore the first 5 rows

# read test data set csv file as a DataFrame
test_df = pd.read_csv(test_path)
test_df.head()  # explore the first 5 rows
print(f"training set (row, col): {trng_df.shape}\ntesting set (row, col): {test_df.shape}")

# 2. Input Data Preparation/Cleaning..................................................................

# check column information
trng_df.head()
trng_df.describe()
trng_df.info()

# dropping ID column for both data sets as all the values are different which doesn't add any value to the model
trng_df.drop('Loan_ID', axis=1, inplace=True)
test_df.drop('Loan_ID', axis=1, inplace=True)
# checking the new shapes
print(f"\ntraining set (row, col): {trng_df.shape}\ntesting set (row, col): {test_df.shape}")

# check missing values and print in descending order
print(trng_df.isnull().sum().sort_values(ascending=False))

# check most frequent value against missing rows for each column
print("\ncheck no. of rows for unique value of each column\n", "#" * 20, "\n")
null_cols = trng_df.columns[trng_df.isna().any()].tolist()
print("Null Columns : ", null_cols)  # print columns having at least a null value
# null_cols = ['Credit_History', 'Self_Employed', 'LoanAmount', 'Dependents', 'Loan_Amount_Term', 'Gender', 'Married']
for col in null_cols:
    print(f"{col}:\n{trng_df[col].value_counts()}\n", "-" * 20)
    trng_df[col] = trng_df[col].fillna(trng_df[col].dropna().mode().values[0])

# fill the missing value with most frequent value for each column
print("\nNo. of rows for each column after filling missing values\n", "#" * 20, "\n")
for col in null_cols:
    print(f"\n{col}:\n{trng_df[col].value_counts()}\n", "-" * 20)  # f is for formatted string

# verify that data is still have missing values
print(trng_df.isnull().sum().sort_values(ascending=False))
print(test_df.isnull().sum().sort_values(ascending=False))
print(trng_df.info())
print(test_df.info())

# extract cleaned data for verification to Output Data directory
# converting categorical values to numbers
to_numeric = {'3+': 3}
# adding the new numeric values from the to_numeric variable to both datasets
trng_df = trng_df.applymap(lambda label: to_numeric.get(label) if label in to_numeric else label)
test_df = test_df.applymap(lambda label: to_numeric.get(label) if label in to_numeric else label)
# converting the Dependents column
Dependents_ = pd.to_numeric(trng_df.Dependents)
trng_df.to_csv("Output Data/7_ML_LoanAmount_CleanedData.csv")

# 3. Feature engineering and visualizing the data to generate insights.............................................

# let us visualize the data to find Loan status distribution
# split data to categorical and numerical data

num = trng_df.select_dtypes('number').columns.to_list()
print(num)  # print list of all the numeric columns
loan_num = trng_df[num]
cat = trng_df.select_dtypes('object').columns.to_list()
print(cat)  # print list of all the categorical columns
loan_cat = trng_df[cat]

# print loan status distribution
print(trng_df[cat[-1]].value_counts())

# Numerical columns split by histogram
for i in loan_num:
    plt.hist(loan_num[i])
    plt.title(i + ' matplotlib histogram')
    plt.show()

# Categorical columns split by Loan status:
for i in cat[:-1]:
    plt.figure(figsize=(10, 5))
    # plt.subplot(2, 3, 1)
    sns.countplot(x=i, hue='Loan_Status', data=trng_df)
    plt.xlabel(i, fontsize=10)
    plt.title('Seaborn Countplot - Loan status distribution by ' + i)
    plt.show()

# plot seaborn chart - catplot with categorical variables
sns.catplot(x="Gender", y="LoanAmount", hue="Loan_Status", col="Property_Area", data=trng_df, kind="strip", height=4,
            aspect=.7)
# plt.title('catplot matrix')
plt.show()

# plot seaborn chart - pairplot with categorical variables
sns.pairplot(trng_df, vars=['Credit_History', 'ApplicantIncome', 'Loan_Amount_Term'], hue="Loan_Status")
plt.title('Seaborn-Pair plot matrix')
plt.show()

# converting categorical values to numbers
to_numeric = {'Male': 1, 'Female': 2, 'Yes': 1, 'No': 2, 'Graduate': 1, 'Not Graduate': 2, 'Urban': 3, 'Semiurban': 2,
              'Rural': 1, 'Y': 1, 'N': 0, '3+': 3}

# adding the new numeric values from the to_numeric variable to both datasets
trng_df = trng_df.applymap(lambda label: to_numeric.get(label) if label in to_numeric else label)
test_df = test_df.applymap(lambda label: to_numeric.get(label) if label in to_numeric else label)

# converting the Dependents column
Dependents_ = pd.to_numeric(trng_df.Dependents)
Dependents__ = pd.to_numeric(test_df.Dependents)

# dropping the previous Dependents column
trng_df.drop(['Dependents'], axis=1, inplace=True)
test_df.drop(['Dependents'], axis=1, inplace=True)

# concatenation of the new Dependents' column with both datasets
trng_df = pd.concat([trng_df, Dependents_], axis=1)
test_df = pd.concat([test_df, Dependents__], axis=1)

# add total income column as rich feature
trng_df['Total_income'] = trng_df['ApplicantIncome']+trng_df['CoapplicantIncome']
test_df['Total_income'] = test_df['ApplicantIncome']+test_df['CoapplicantIncome']

# checking manipulated dataset for validation
print(f"\ntraining set (row, col): {trng_df.shape}\n\ntesting set (row, col): {test_df.shape}\n")
print(trng_df.info(), "\n\n", test_df.info())

# extract engineered data for verification
trng_df.to_csv("Output Data/7_ML_LoanAmount_EngineeredData.csv")

# plotting the correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(trng_df.corr(), cmap='cubehelix_r')
plt.show()
# correlation table
corr = trng_df.corr()
print(corr)

# Conclusion - We can clearly see that Credit_History has the highest correlation with Loan_Status a positive
# correlation 0.540556. Therefore, our target value is highly dependent on the column 'Credit History'.

#  4. Execute machine learning algorithm by splitting train and test data...................

# Let us divide our dataset into two variables X as the features we defined earlier and y as the Loan_Status the
# target value we want to predict.
# Models we will use to predict the target value : Random Forest, Decision Tree, XGBoost, Logistic Regression

# Create arrays for the features and the response variable
y = trng_df['Loan_Status']
X = trng_df.drop('Loan_Status', axis=1)
# split train and test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


# Create ML algorithm score function.........
def find_algo_score_fn(algo_fn, algo_name):  # Defines a ml function
    ml_model = algo_fn  # # implement random forest ML algorithm
    ml_model.fit(X_train, y_train)  # fit the model
    y_predict = ml_model.predict(X_test)  # predict the target
    print("\n\n")
    print(classification_report(y_test, y_predict))  # print predicted result
    algo_score = accuracy_score(y_predict, y_test)  # find accuracy score
    print(f"{round(algo_score * 100, 2)}% Accurate")  # print accuracy score
    parsed_data = pd.DataFrame({'y_test': y_test, 'prediction': y_predict})
    parsed_data.to_csv("Output Data/" + "7_ML_" + algo_name + ".csv")  # print output to csv
    return algo_score  # return algorithm score


# call algo score function and execute types of ML and find accuracy score
RF_SC = find_algo_score_fn(RandomForestClassifier(), "Random_Forest")  # implement random forest ML algorithm
DT_SC = find_algo_score_fn(DecisionTreeClassifier(), "Decision_Tree")  # implement decision tree ML algorithm
XGB_SC = find_algo_score_fn(XGBClassifier(), "XGBoost")  # implement XGBoost ML algorithm
LR_SC = find_algo_score_fn(LogisticRegression(), "Logistic_Regression")  # implement random forest ML algorithm

# print all ML algorithm's accuracy result
score = [round(RF_SC * 100, 2), round(DT_SC * 100, 2), round(XGB_SC * 100, 2), round(LR_SC * 100, 2)]
Models = pd.DataFrame({
    'ML_algorithm': ["Random Forest", "Decision Tree", "XGBoost", "Logistic Regression"],
    'Score': score})
print("\n\n")
print(Models.sort_values(by='Score', ascending=False))

# cross validation................
# Select subset of predictors
X = trng_df[['Credit_History', 'Education', 'CoapplicantIncome', 'Self_Employed', 'Dependents', 'ApplicantIncome', 'Married', 'Gender', 'Property_Area', 'LoanAmount', 'Loan_Amount_Term']]
y = trng_df['Loan_Status']  # Select target
my_pipeline = Pipeline(
    steps=[('preprocessor', SimpleImputer()), ('model', RandomForestRegressor(n_estimators=50, random_state=0))])
# Multiply by -1 since sklearn calculates *negative* MAE
scores = -1 * cross_val_score(my_pipeline, X, y, cv=5, scoring='neg_mean_absolute_error')
# acc_result = cross_val_score(my_pipeline, X, y, cv=5, scoring='accuracy')
print("\nMAE scores: ", scores)
print("\nAverage MAE score (across experiments): ")
print(scores.mean())

# print("Average accuracy score (across experiments):")
# print(acc_result.mean())


#  5. Hyperparameter tuning........................................................................

# ...............Hyperparameter tuning with GridSearchCV --------------
# Creating the hyper parameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space}
logreg = LogisticRegression()   # Instantiating logistic regression classifier
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)  # Instantiating the GridSearchCV object
y = trng_df['Loan_Status']
X = trng_df.drop('Loan_Status', axis=1)
logreg_cv.fit(X, y)
# Print the tuned parameters and score
print("\nTuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))

# ...............Hyperparameter tuning with RandomizedSearchCV................
# Creating the hyperparameter grid
param_dist = {"max_depth": [3, None], "max_features": randint(1, 9), "min_samples_leaf": randint(1, 9),
              "criterion": ["gini", "entropy"]}
tree = DecisionTreeClassifier()  # Instantiating Decision Tree classifier
tree_cv = RandomizedSearchCV(tree, param_dist, cv=5)    # Instantiating RandomizedSearchCV object
# Create arrays for the features and the response variable
y = trng_df['Loan_Status'].values
X = trng_df.drop('Loan_Status', axis=1).values
tree_cv.fit(X, y)
# Print the tuned parameters and score
print("\nTuned Decision Tree Parameters: {}".format(tree_cv.best_params_))
print("Best score is {}".format(tree_cv.best_score_))

#  6. Insights ...............................................................................
print("\n\n6.1. Credit_History is most important variable due to its high correlation with Loan_Status.")
print("6.2. Most accurate algorithm is 'The Logistic Regression' with approximately 83%.")
print("6.3 seaborn chart - catplot - LoanStatus distribution by gender and property area")
print("6.4 seaborn chart - pairplot - LoanStatus distribution by credit history, applicant income and loan amount term")
