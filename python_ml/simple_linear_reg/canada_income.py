import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv("canada_per_capita_income.csv")
# print(df)
plt.scatter(df['per capita income (US$)'],df['year'],color='blue')
plt.xlabel("Income")
plt.ylabel("Year")
# plt.show()
rg = linear_model.LinearRegression()
rg.fit(df[['year']],df['per capita income (US$)'])
predicted_data = rg.predict([[2020]])
# plt.plot(df['year'],predicted_data,color='red')
# plt.show()
print("Predicted per capital income for 2020",predicted_data)
