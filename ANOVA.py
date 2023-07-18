# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 12:59:10 2023

@author: levih
"""

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

# Specify the directory path
directory = r'C:\Users\levih\OneDrive\Documents\Praxis Python Folder'

# List all files in the directory
files = os.listdir(directory)

# Filter files to load only specific file types, e.g., CSV or Excel
allowed_extensions = ['.csv', '.xlsx']
data_files = [file for file in files if os.path.splitext(file)[1] in allowed_extensions]

# Load data from each file into a dictionary
data = {}
for file in data_files:
    file_path = os.path.join(directory, file)
    file_name, file_ext = os.path.splitext(file)
    
    if file_ext == '.csv':
        data[file_name] = pd.read_csv(file_path)
    elif file_ext == '.xlsx':
        data[file_name] = pd.read_excel(file_path)

# Print the loaded data
for file_name, df in data.items():
    print(f"Data from file: {file_name}")
    print(df.head())  # Display the first few rows of each DataFrame
    print("---------------------------------------------")

# Hypothesis Testing

# Load the spreadsheet data into a DataFrame
file_path = r'C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Data Sandbox.xlsx'
data = pd.read_excel(file_path)

# Specify the column titles
group_column = 'Program'
value_columns = ['Overall Product Knowledge Score']

# Perform ANOVA for each value column
for column in value_columns:
    groups = data[group_column].unique()
    data_groups = [data[column][data[group_column] == group] for group in groups]
    statistic, p_value = stats.f_oneway(*data_groups)
    
    # Output the ANOVA results
    print(f"\nANOVA Results for '{column}':")
    print("---------------")
    print("F-statistic:", statistic)
    print("p-value:", p_value)

