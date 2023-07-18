# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 13:25:36 2023

@author: levih
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load the data from the Excel file
data = pd.read_excel("C:/Users/levih/OneDrive/Documents/Praxis Python Folder/Data Sandbox.xlsx")

# Select the relevant columns for analysis
columns = ["Total Program Cost (I)", "Total Program Cost (C)", "Overall Product Knowledge Score"]
df = data[columns]

# Perform one-hot encoding for the categorical variable
df_encoded = pd.get_dummies(df, columns=["Overall Product Knowledge Score"], drop_first=True)

# Split the dataset into features (X) and target variable (y)
X = df_encoded.drop("Overall Product Knowledge Score_8", axis=1)  # All columns except the highest score
y = df_encoded["Overall Product Knowledge Score_8"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predict the Overall Product Knowledge Score using the total costs
y_pred = regressor.predict(X_test)

# Print the coefficients (weights) of the linear regression model
coefficients = pd.DataFrame({'Feature': X.columns, 'Coefficient': regressor.coef_})
print(coefficients)

# Evaluate the model performance (optional)
r2_score = regressor.score(X_test, y_test)
print(f"R-squared Score: {r2_score}")




