# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 15:09:19 2023

@author: levih
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the data from Excel
file_path = r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Data Sandbox.xlsx"
df = pd.read_excel(file_path)

# Extract the relevant columns
cost_change = df['Total Program Cost (C)'] - df['Total Program Cost (I)']
time_change = df['Acquisition Cycle Time Current'] - df['Acquisition Cycle Time Intitial']

# Perform linear regression
regressor = LinearRegression()
regressor.fit(time_change.values.reshape(-1, 1), cost_change)

# Calculate the predicted values
predicted_cost_change = regressor.predict(time_change.values.reshape(-1, 1))

# Plot the data and regression line
plt.scatter(time_change, cost_change, color='blue', label='Actual Data')
plt.plot(time_change, predicted_cost_change, color='red', label='Regression Line')
plt.xlabel('Change in Acquisition Cycle Time')
plt.ylabel('Change in Total Program Cost')
plt.title('Linear Regression: Change in Total Program Cost vs. Change in Acquisition Cycle Time')
plt.legend()
plt.show()

# Print the coefficient and intercept
print("Coefficient:", regressor.coef_[0])
print("Intercept:", regressor.intercept_)

