import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
import math
df = pd.read_csv("hiring.csv")
df['experience'] = df['experience'].apply(lambda x:w2n.word_to_num(x) if isinstance(x,str) else x)
df['experience'] = df['experience'].fillna(math.floor(df['experience'].median()))
df['test_score(out of 10)'] = df['test_score(out of 10)'].fillna(math.floor(df['test_score(out of 10)'].median()))
# print(df)
rg = linear_model.LinearRegression()
rg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])
print(rg.predict([[2,9,6]]))
print(rg.predict([[12,10,10]]))
