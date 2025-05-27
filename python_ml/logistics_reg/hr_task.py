# Questions
# Now do some exploratory data analysis to figure out which variables have direct and clear impact on employee retention (i.e. whether they leave the company or continue to work)
# Plot bar charts showing impact of employee salaries on retention
# Plot bar charts showing corelation between department and employee retention
# Now build logistic regression model using variables that were narrowed down in step 1
# Measure the accuracy of the model

import pandas as pd
import matplotlib.pyplot as plt

# Show all columns when printing DataFrame
pd.set_option('display.max_columns', None)

# Load the HR dataset
df = pd.read_csv('HR.csv')

# Split data based on employee retention
left = df[df['left']==1]        # Employees who left the company
retained = df[df['left']==0]    # Employees who stayed

# Calculate average values for each column grouped by 'left'
avg = df.groupby('left').mean(numeric_only=True)

# Bar chart: impact of employee salary on retention
pd.crosstab(df['salary'],df['left']).plot(kind='bar')
plt.xlabel('salary')
plt.ylabel('employees')
# plt.show()  # Uncomment to display the chart

# Bar chart: correlation between department and employee retention
pd.crosstab(df['Department'],df['left']).plot(kind='bar')
plt.xlabel('salary')  # (Consider correcting label to "Department")
plt.ylabel('department')
# plt.show()  # Uncomment to display the chart

# Select key variables based on EDA
# Using: satisfaction_level, average_monthly_hours, promotion_last_5years, salary
subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]

# Convert salary categorical variable into dummy/one-hot encoded variables
salary_dummies = pd.get_dummies(subdf['salary'], prefix='salary', dtype=int)

# Combine dummy variables with main dataframe
df_with_dummies = pd.concat([subdf, salary_dummies], axis='columns')

# Drop the original salary column
final_df = df_with_dummies.drop('salary', axis='columns')

# Define feature matrix X and target variable y
x = final_df
y = df['left']

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, train_size=0.8)

# Build and train a Logistic Regression model
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(x_train, y_train)

# Predict and print predictions on test data
print(model.predict(x_test))

# Print model accuracy
print("model accuracy", model.score(x_test, y_test))
