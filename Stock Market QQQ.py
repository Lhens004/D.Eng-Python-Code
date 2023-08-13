import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Load the data from the CSV file
df = pd.read_csv(r"C:\\Users\\levih\\OneDrive\\Desktop\\QQQ.csv")

# Drop 'Date' column
df = df.drop(columns=['Date'])

# Split the data into features and target variable
X = df.drop(columns=['High'])
y = df['High']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train the Random Forest regressor
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Calculate the mean squared error and R^2 score on the test set
mse = mean_squared_error(y_test, rf.predict(X_test))
r2 = r2_score(y_test, rf.predict(X_test))

print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Prompt the user to enter values for the previous day
open_value = float(input("Enter the 'Open' value from the previous day: "))
low_value = float(input("Enter the 'Low' value from the previous day: "))
close_value = float(input("Enter the 'Close' value from the previous day: "))
volume_value = int(input("Enter the 'Volume' from the previous day: "))

# Store the entered values in a dictionary
prev_day_data = {
    'Open': [open_value],
    'Low': [low_value],
    'Close': [close_value],
    'Volume': [volume_value]
}

# Convert to DataFrame
prev_day_df = pd.DataFrame(prev_day_data)

# Use the trained model to predict
predicted_high = rf.predict(prev_day_df)

print("Predicted High for the next day:", predicted_high[0])
