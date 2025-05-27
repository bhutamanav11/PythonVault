import pandas as pd
df = pd.read_csv('homeprices.csv')
# getting dummy values for town for calculations
dummy = pd.get_dummies(df.town,dtype=int)
# print(dummy)
# joining two dataframes in order to make 1 whole dataframe
merge = pd.concat([df,dummy],axis='columns')
# print(merge)
# drop town as no use of it now 
# if n dummy variables use only n-1 hence here we have 3 using only 2 and dropping 1 coloumn
# this is becasue it leads to multicolinearity values can be derived from each other.
final = merge.drop(['town','west windsor'],axis='columns')
# final dataset to work on
# print(final)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
x = final.drop(['price'],axis='columns')
y = final['price']
#training the model
model.fit(x,y)
# print(model.predict([[3600,0,0]]))
print(model.score(x,y)*100,"percent")
