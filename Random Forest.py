import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load the data from the Excel file
data_path = r'C:\Users\levih\OneDrive\Documents\GWU Doctor of Engineering Program\Praxis\Data\Python Path\Data 2012 - 2023_07-29.xlsx'
data = pd.read_excel(data_path)

# Convert percentage columns to float
percentage_columns = ["AC %Chg", "DC %Chg", "PC % Change", "UC % Change ", "TQ % Change"]
for col in percentage_columns:
    if data[col].dtype == 'object':
        data[col] = data[col].str.rstrip('%').astype('float') / 100

# Convert dollar columns to float
dollar_columns = [
    "Total Program Cost Intial", "Total Program Cost Current", "Development Cost Initial", "Development Cost Present",
    "Procurment Cost Initial", "Procurment Cost Current", "Unit Cost Initial", "Unit Cost Current"
]
for col in dollar_columns:
    if data[col].dtype == 'object':
        data[col] = data[col].replace('[\$,]', '', regex=True).astype(float)

# Define the features to be used
features = ["Acquisition Cycle Time Intitial", "Unit Cost Initial", "Unit Cost Current", "AC %Chg", "Total Quanty",
            "Total Quantity Current", "Sentiment Score"]

# Select the prediction target
y = data["Acquisition Cycle Time Current"]

# Select the features
X = data[features]

# Split the data into training and validation sets
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)

# Define the Random Forest Model
forest_model = RandomForestRegressor(random_state=1)

# Fit the model
forest_model.fit(train_X, train_y)

# Make predictions
val_predictions = forest_model.predict(val_X)

# Print mean absolute error
print("Mean Absolute Error: ", mean_absolute_error(val_y, val_predictions))
