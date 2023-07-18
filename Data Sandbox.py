import pandas as pd

# Load the Excel file into a pandas DataFrame
data = pd.read_excel(r"C:\Users\levih\OneDrive\Documents\Praxis Python Folder\Data Sandbox.xlsx")

# Extract the relevant columns
product_knowledge = data['Overall Product Knowledge Score']
cycle_time_initial = data['Acquisition Cycle Time Intitial']
cycle_time_current = data['Acquisition Cycle Time Current']
cost_initial = data['Total Program Cost (I)']

# Check if 'Total Program Cost (C)' column exists in the DataFrame
if 'Total Program Cost (C)' in data.columns:
    cost_current = data['Total Program Cost (C)']
else:
    cost_current = None
    print("Column 'Total Program Cost (C)' not found. Correlation with program costs cannot be calculated.")

# Calculate the change in acquisition cycle time and total program costs
cycle_time_change = cycle_time_current - cycle_time_initial
cost_change = cost_current - cost_initial if cost_current is not None else None

# Calculate the correlation coefficients
correlation_product_knowledge_cycle_time = product_knowledge.corr(cycle_time_change)
correlation_product_knowledge_cost = product_knowledge.corr(cost_change) if cost_change is not None else None
correlation_cycle_time_cost = cycle_time_change.corr(cost_change) if cost_change is not None else None

# Print the correlation coefficients
print("Correlation between Overall Product Knowledge Score and Change in Acquisition Cycle Time:", correlation_product_knowledge_cycle_time)
if correlation_product_knowledge_cost is not None:
    print("Correlation between Overall Product Knowledge Score and Change in Total Program Costs:", correlation_product_knowledge_cost)
if correlation_cycle_time_cost is not None:
    print("Correlation between Change in Acquisition Cycle Time and Change in Total Program Costs:", correlation_cycle_time_cost)
