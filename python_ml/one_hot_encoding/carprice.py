import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('carprices.csv')
# x = df['Mileage']
# y = df['Sell Price($)']
# plt.scatter(x,y)
# plt.xlabel("Mileage")
# plt.ylabel("Sell Price")
# plt.show()
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
le = LabelEncoder()
dfle = df.copy()
df['Car Model'] = le.fit_transform(dfle['Car Model'])
# print(df)
x = dfle[['Car Model','Mileage','Age(yrs)']].values
y = dfle['Sell Price($)']
ct = ColumnTransformer(
    transformers=[
       ('encoder',OneHotEncoder(),[0]) 
    ],
    remainder='passthrough'
)
x = ct.fit_transform(x)
x = x[:,1:]
# print(x)
model = LinearRegression()
model.fit(x,y)
print(model.predict([[1,0,86000,7]]),"BMW X5 7 years old 86000 miles")
print(model.score(x,y),"score")