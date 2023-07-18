# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:00:36 2023

@author: levih
"""
#Loading Data from Folder
import os
import pandas as pd

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

#Hypothisis Testing

import pandas as pd
from scipy import stats

# Load the spreadsheet data into a DataFrame
file_path = r'C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Data 2012 - 2022.xlsx'
data = pd.read_excel(file_path)

# Specify the column titles
group_column = 'Program'
value_columns = ['PK Score (A)', 'PK Score (B)', 'PK Score (C)']

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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set the file path
data_path = r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Data 2012 - 2022.xlsx"

# Load the data into a DataFrame
df = pd.read_excel(data_path)

# Define the list of columns
columns = ['Year', 'Program', 'Prime', 'Branch', 'Program Start Date', 'Dev (c)', 'Proc(c)', 'TQ(F)',
           '%Complete', 'Acquisition Cycle Time Intitial', 'Acquisition Cycle Time Current', '%Chg',
           'Software Development Method', 'Avg Software Deliveries', 'Software Percentage of Total Cost',
           'COTS', 'Modified COTS', 'Custom Software', 'Development Cost Initial', 'Development Cost Present',
           '%Chg Development Cost', 'Procurement Cost Initial', 'Procurement Cost Current', '% Change Procurement Cost',
           'Unit Cost Initial', 'Unit Cost Current', '% Change Unit Cost', 'Total Quantity', 'Total Quantity Current',
           '% Change Total Quantity', 'PK Score (A)', 'PK Score (B)', 'PK Score (C)', 'Total']

# Data cleaning: Handling outliers
outliers = {}

# Detect and handle outliers for each column
for col in columns:
    # Detect outliers using z-score
    z_scores = np.abs(stats.zscore(df[col]))
    z_threshold = 3
    outliers_z = df[z_scores > z_threshold]
    outliers[col + '_zscore'] = outliers_z
    
    # Detect outliers using modified z-score
    median = np.median(df[col])
    median_absolute_deviation = np.median(np.abs(df[col] - median))
    modified_z_scores = np.abs(0.6745 * (df[col] - median) / median_absolute_deviation)
    modified_z_threshold = 3
    outliers_modified_z = df[modified_z_scores > modified_z_threshold]
    outliers[col + '_modified_zscore'] = outliers_modified_z
    
    # Create box plots
    plt.figure(figsize=(8, 6))
    sns.boxplot(x=df[col])
    plt.title(f"Box Plot: {col}")
    plt.xlabel(col)
    plt.show()

# Handle outliers (e.g., removal, transformation, winsorization)
# For demonstration purposes, let's remove outliers

# Remove outliers from the DataFrame
df_cleaned = df.copy()
for col in outliers:
    df_cleaned = df_cleaned.drop(outliers[col].index)

# Print the cleaned DataFrame
print("Cleaned DataFrame:")
print(df_cleaned.head())

# Save the cleaned data to a new Excel file
cleaned_data_path = r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Cleaned_Data.xlsx"
df_cleaned.to_excel(cleaned_data_path, index=False)
print(f"Cleaned data saved to {cleaned_data_path}")

import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Set the file path
data_path = r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Cleaned_Data.xlsx"

# Load the cleaned data into a DataFrame
df = pd.read_excel(data_path)

# Define the list of columns to be scaled
columns_to_scale = ['Dev (c)', 'Proc(c)', 'TQ(F)', '%Complete', 'Acquisition Cycle Time Intitial',
                    'Acquisition Cycle Time Current', '%Chg', 'Avg Software Deliveries',
                    'Software Percentage of Total Cost', 'COTS', 'Modified COTS', 'Custom Software',
                    'Development Cost Initial', 'Development Cost Present', '%Chg Development Cost',
                    'Procurement Cost Initial', 'Procurement Cost Current', '% Change Procurement Cost',
                    'Unit Cost Initial', 'Unit Cost Current', '% Change Unit Cost', 'Total Quantity',
                    'Total Quantity Current', '% Change Total Quantity', 'PK Score (A)', 'PK Score (B)',
                    'PK Score (C)', 'Total']

# Perform feature scaling

# Standardization
scaler = StandardScaler()
df_scaled_standardized = pd.DataFrame(scaler.fit_transform(df[columns_to_scale]), columns=columns_to_scale)

# Normalization (MinMax Scaling)
scaler = MinMaxScaler()
df_scaled_normalized = pd.DataFrame(scaler.fit_transform(df[columns_to_scale]), columns=columns_to_scale)

# Print the scaled DataFrames
print("Standardized Data:")
print(df_scaled_standardized.head())

print("\nNormalized Data:")
print(df_scaled_normalized.head())

#data visualization

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the file path
data_path = r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Cleaned_Data.xlsx"

# Load the cleaned data into a DataFrame
df = pd.read_excel(data_path)

# Define the list of columns for visualization
columns_to_visualize = ['Dev (c)', 'Proc(c)', 'TQ(F)', '%Complete', 'Acquisition Cycle Time Intitial',
                        'Acquisition Cycle Time Current', '%Chg', 'Avg Software Deliveries',
                        'Software Percentage of Total Cost', 'COTS', 'Modified COTS', 'Custom Software',
                        'Development Cost Initial', 'Development Cost Present', '%Chg Development Cost',
                        'Procurement Cost Initial', 'Procurement Cost Current', '% Change Procurement Cost',
                        'Unit Cost Initial', 'Unit Cost Current', '% Change Unit Cost', 'Total Quantity',
                        'Total Quantity Current', '% Change Total Quantity', 'PK Score (A)', 'PK Score (B)',
                        'PK Score (C)', 'Total']

# Visualize feature relationships

# Scatter plot matrix
sns.pairplot(df[columns_to_visualize])
plt.show()

# Box plots
df_box = df[columns_to_visualize].melt(var_name="Features")
plt.figure(figsize=(12, 6))
sns.boxplot(data=df_box, x="Features", y="value")
plt.xticks(rotation=90)
plt.show()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(df[columns_to_visualize].corr(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation Heatmap")
plt.show()


