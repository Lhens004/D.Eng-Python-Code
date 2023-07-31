import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import re

# Load the data
file_path = "C:\\Users\\levih\\OneDrive\\Documents\\GWU Doctor of Engineering Program\\Praxis\\Data\\Python Path\\Data 2012 - 2023_07-29.xlsx"
data = pd.read_excel(file_path)

# Convert columns with percentage and dollar signs to float
# Convert columns with percentage and dollar signs to float and ignore non-numeric strings
for column in data.columns:
    if data[column].dtype == 'object':
        try:
            data[column] = pd.to_numeric(data[column].replace('[\$,%,]', '', regex=True), errors='coerce')
        except:
            continue


# Filter only integer columns
integer_columns = [col for col in data.columns if pd.api.types.is_integer_dtype(data[col])]

# Separate the target variable 'Sentiment Score'
X = data[integer_columns].drop(columns=['Sentiment Score'])
y = data['Sentiment Score']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes model
model = GaussianNB()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy of Naive Bayes model: {accuracy * 100:.2f}%")
