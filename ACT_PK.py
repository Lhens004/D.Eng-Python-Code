# -*- coding: utf-8 -*-
"""


@author: levih
"""

#ACT (I) ACT (F) PK Score

import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the data from the Excel file
df = pd.read_excel("C:/Users/levih/OneDrive/Documents/Praxis Python Folder/Data Sandbox.xlsx")

# Calculate the change in Acquisition Cycle Time
df['Cycle Time Change'] = df['Acquisition Cycle Time Current'] - df['Acquisition Cycle Time Intitial']

# Select the relevant columns for the analysis
features = ['Cycle Time Change']
target = 'Overall Product Knowledge Score'

# Create the feature matrix (X) and target vector (y)
X = df[features]
y = df[target]

# Fit the linear regression model
regressor = LinearRegression()
regressor.fit(X, y)

# Print the coefficients
coefficients = pd.DataFrame({'Feature': features, 'Coefficient': regressor.coef_})
print(coefficients)

# Print the R-squared score
r_squared = regressor.score(X, y)
print(f"\nR-squared Score: {r_squared}")