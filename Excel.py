# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 06:44:23 2023

@author: levih
"""

import pandas as pd

def compare_excel_sheets(file1_path, file2_path):
    # Load excel files
    df1 = pd.read_excel(file1_path, sheet_name="Sheet1")
    df2 = pd.read_excel(file2_path, sheet_name="Sheet1")

    # Ensure both sheets have the same columns (This may be adjusted based on your needs)
    if list(df1.columns) != list(df2.columns):
        return "The columns in the two sheets are different. Please ensure they have the same structure."

    changes = []
    
    # Compare rows
    for index, row in df1.iterrows():
        try:
            row2 = df2.iloc[index]
        except IndexError:
            changes.append(f"Row {index + 1} from {file1_path} is not present in {file2_path}.")
            continue
        
        if not row.equals(row2):
            changes.append(f"Row {index + 1} is different between the files.")
    
    # Check for extra rows in the second file
    if len(df2) > len(df1):
        for index in range(len(df1), len(df2)):
            changes.append(f"Row {index + 1} from {file2_path} is not present in {file1_path}.")

    return changes

# Usage
file1_path = 'path_to_first_excel_file.xlsx'
file2_path = 'path_to_second_excel_file.xlsx'
changes_report = compare_excel_sheets(file1_path, file2_path)
for change in changes_report:
    print(change)
