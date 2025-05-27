import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
df = pd.read_csv("homeprices.csv")
# print(df)
# to fill nan values
import math
bedroom_median = math.floor(df['bedrooms'].median())
df['bedrooms'] = df['bedrooms'].fillna(bedroom_median)
print("Filling NaN values")
# print(df) 
rg = linear_model.LinearRegression()
rg.fit(df[['area','bedrooms','age']],df['price'])
print(rg.predict([[3000,3,40]]))
print(rg.predict([[2500,4,5]]))