# import packages
import numpy as np
import pandas as pd
import warnings

# import libraries
import matplotlib.pyplot as plt
import seaborn as sns

# import ML libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score

# import ML models
from xgboost import XGBClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# handle warnings
warnings.filterwarnings("ignore")

# 1. Data Collection..................................................................

trng_path = "Train_LoanPredictionData.csv"  # path for the training data sets
test_path = "Test_LoanPredictionData.csv"  # path for the testing data sets

# read train data set csv files as a DataFrame
trng_df = pd.read_csv(trng_path)
trng_df.head()  # explore the first 5 rows

# read test data set csv file as a DataFrame
test_df = pd.read_csv(test_path)
test_df.head()  # explore the first 5 rows

print(f"training set (row, col): {trng_df.shape}\ntesting set (row, col): {test_df.shape}")

# 2. Data Preparation/Cleaning..................................................................

# check column information
trng_df.head()
trng_df.shape
trng_df.describe()
trng_df.info()

# dropping ID column as not needed for both data sets
trng_df.drop('Loan_ID', axis=1, inplace=True)
test_df.drop('Loan_ID', axis=1, inplace=True)
# checking the new shapes
print(f"training set (row, col): {trng_df.shape}\ntesting set (row, col): {test_df.shape}")

# check missing values and print in descending order
print(trng_df.isnull().sum().sort_values(ascending=False))

# check most frequent value against missing rows for each column
print("check no. of rows for unique value of each column\n", "#" * 20, "\n")
null_cols = ['Credit_History', 'Self_Employed', 'LoanAmount', 'Dependents', 'Loan_Amount_Term', 'Gender', 'Married']
for col in null_cols:
    print(f"{col}:\n{trng_df[col].value_counts()}\n", "-" * 20)
    trng_df[col] = trng_df[col].fillna(trng_df[col].dropna().mode().values[0])

# fill the missing value with most frequent value for each column
print("No. of rows for each column after filling missing values\n", "#" * 20, "\n")
for col in null_cols:
    print(f"\n{col}:\n{trng_df[col].value_counts()}\n", "-" * 20)

# verify that data is still have missing values
print(trng_df.isnull().sum().sort_values(ascending=False))
print(test_df.isnull().sum().sort_values(ascending=False))
print(trng_df.info())
print(test_df.info())

# 3. Feature engineering ..................................................................

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

# plot numeric data
for i in loan_num:
    plt.hist(loan_num[i])
    plt.title(i)
    plt.show()

# Categorical (split by Loan status):
for i in cat[:-1]:
    plt.figure(figsize=(10, 5))
    plt.subplot(2, 3, 1)
    sns.countplot(x=i, hue='Loan_Status', data=trng_df, palette='plasma')
    plt.xlabel(i, fontsize=10)
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

# checking manipulated dataset for validation
print(f"training set (row, col): {trng_df.shape}\n\ntesting set (row, col): {test_df.shape}\n")
print(trng_df.info(), "\n\n", test_df.info())

# plotting the correlation matrix
plt.figure(figsize=(10, 10))
sns.heatmap(trng_df.corr(), cmap='cubehelix_r')
plt.show()
# correlation table
corr = trng_df.corr()
print(corr)

# Conclusion - We can clearly see that Credit_History has the highest correlation with Loan_Status a positive
# correlation 0.540556. Therefore, our target value is highly dependent on the column 'Credit History'.

#  4. Implement machine learning algorithm......................................................

# Let us divide our dataset into two variables X as the features we defined earlier and y as the Loan_Status the
# target value we want to predict.
# Models we will use to predict the target value : Random Forest, XGBoost, Logistic Regression

# split train and test data
y = trng_df['Loan_Status']
X = trng_df.drop('Loan_Status', axis=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# implement decision tree ML algorithm
DT = DecisionTreeClassifier()
DT.fit(X_train, y_train)  # fit the model
y_predict = DT.predict(X_test)  # predict the target
print(classification_report(y_test, y_predict))  # print predicted result
DT_SC = accuracy_score(y_predict, y_test)
print(f"{round(DT_SC * 100, 2)}% Accurate")  # print accuracy score
Decision_Tree = pd.DataFrame({'y_test': y_test, 'prediction': y_predict})
Decision_Tree.to_csv("Decision_Tree.csv")  # print output to csv

# implement random forest ML algorithm
RF = RandomForestClassifier()
RF.fit(X_train, y_train)  # fit the model
y_predict = RF.predict(X_test)  # predict the target
print(classification_report(y_test, y_predict))  # print predicted result
RF_SC = accuracy_score(y_predict, y_test)
print(f"{round(RF_SC * 100, 2)}% Accurate")  # print accuracy score
Random_Forest = pd.DataFrame({'y_test': y_test, 'prediction': y_predict})
Random_Forest.to_csv("Random_Forest.csv")  # print output to csv

# implement XGBoost ML algorithm
XGB = XGBClassifier()
XGB.fit(X_train, y_train)  # fit the model
y_predict = XGB.predict(X_test)  # predict the target
print(classification_report(y_test, y_predict))  # print predicted result
XGB_SC = accuracy_score(y_predict, y_test)
print(f"{round(XGB_SC * 100, 2)}% Accurate")  # print accuracy score
XGBoost = pd.DataFrame({'y_test': y_test, 'prediction': y_predict})
XGBoost.to_csv("XGBoost.csv")  # print output to csv

# implement random forest ML algorithm
LR = LogisticRegression()
LR.fit(X_train, y_train)  # fit the model
y_predict = LR.predict(X_test)  # predict the target
print(classification_report(y_test, y_predict))  # print predicted result
LR_SC = accuracy_score(y_predict, y_test)
print(f"{round(LR_SC * 100, 2)}% Accurate")  # print accuracy score
Logistic_Regression = pd.DataFrame({'y_test': y_test, 'prediction': y_predict})
Logistic_Regression.to_csv("Logistic_Regression.csv")  # print output to csv

# print all ML algorithm's accuracy result
score = [round(DT_SC * 100, 2), round(RF_SC * 100, 2), round(XGB_SC * 100, 2), round(LR_SC * 100, 2)]
Models = pd.DataFrame({
    'ML_algorithm': ["Decision Tree", "Random Forest", "XGBoost", "Logistic Regression"],
    'Score': score})
print(Models.sort_values(by='Score', ascending=False))

#  5. Conclusion ...............................................................................
# 5.1. Credit_History is most important variable due to its high correlation with Loan_Status
# 5.2. Most accurate algorithm is 'The Logistic Regression' with approximately 83%.
