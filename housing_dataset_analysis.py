# -*- coding: utf-8 -*-
"""Housing_Dataset_Analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1saW9aCfcQj79V6FNPXzHxZ-QaH4C-L6v
"""

#Step 1: Import all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')


#Step 2: Load the dataset
data = pd.read_csv('/content/HousingData  - HousingData.csv')
print(data.head())

#Step 3: Understand the data
print(data.info())
print(data.describe())

#Step 4: Deal with the missing values if any

# Check for missing values
print(data.isnull().sum())

# Fill missing values with the mean of the column
data = data.apply(lambda x: x.fillna(x.mean()),axis=0)
print(data.isnull().sum())

#Step 5: Visualization
# Histograms
data.hist(bins=30, figsize=(20,15), edgecolor='black')
plt.suptitle('Histogram of Each Feature', fontsize=20)
plt.show()

# Boxplots
plt.figure(figsize=(20, 10))
data.boxplot()
plt.title('Boxplot of Each Feature', fontsize=20)
plt.xticks(rotation=45)
plt.show()

# Pairplot
sns.pairplot(data)
plt.suptitle('Pairplot of Dataset', y=1.02, fontsize=20)
plt.show()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap', fontsize=20)
plt.show()

# Scatter plots for some important relationships
plt.figure(figsize=(20, 10))

plt.subplot(2, 3, 1)
plt.scatter(data['RM'], data['MEDV'], edgecolor='w')
plt.title('RM vs MEDV', fontsize=15)
plt.xlabel('Average Number of Rooms per Dwelling (RM)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.subplot(2, 3, 2)
plt.scatter(data['LSTAT'], data['MEDV'], edgecolor='w')
plt.title('LSTAT vs MEDV', fontsize=15)
plt.xlabel('% Lower Status Population (LSTAT)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.subplot(2, 3, 3)
plt.scatter(data['PTRATIO'], data['MEDV'], edgecolor='w')
plt.title('PTRATIO vs MEDV', fontsize=15)
plt.xlabel('Pupil-Teacher Ratio (PTRATIO)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.subplot(2, 3, 4)
plt.scatter(data['TAX'], data['MEDV'], edgecolor='w')
plt.title('TAX vs MEDV', fontsize=15)
plt.xlabel('Property Tax Rate (TAX)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.subplot(2, 3, 5)
plt.scatter(data['INDUS'], data['MEDV'], edgecolor='w')
plt.title('INDUS vs MEDV', fontsize=15)
plt.xlabel('Proportion of Non-Retail Business Acres (INDUS)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.subplot(2, 3, 6)
plt.scatter(data['NOX'], data['MEDV'], edgecolor='w')
plt.title('NOX vs MEDV', fontsize=15)
plt.xlabel('Nitric Oxide Concentration (NOX)')
plt.ylabel('Median Value of Homes (MEDV)')

plt.tight_layout()
plt.show()

#Step 6: Divide the dataset into training and test datasets

X = data.drop('MEDV', axis=1)
y = data['MEDV']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Step 7:Build Linear Regression model
model = LinearRegression()

#Step 8: Fit the model on the training dataset
model.fit(X_train, y_train)

# Predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Model evaluation
print(f"Train R2 Score: {r2_score(y_train, y_train_pred)}")
print(f"Test R2 Score: {r2_score(y_test, y_test_pred)}")
print(f"Train RMSE: {np.sqrt(mean_squared_error(y_train, y_train_pred))}")
print(f"Test RMSE: {np.sqrt(mean_squared_error(y_test, y_test_pred))}")