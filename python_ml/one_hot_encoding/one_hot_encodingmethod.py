import pandas as pd
df = pd.read_csv('homeprices.csv')
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dfle = df
df['town'] = le.fit_transform(dfle['town'])
# print(df)
x = dfle[['town','area']].values
y = dfle['price']
# using one hot encoding to do everything
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.compose import ColumnTransformer
# to let the program know on which coloumn is the dummy being made
ct = ColumnTransformer(
    transformers=[
        ('encoder',OneHotEncoder(),[0])
    ],
    remainder='passthrough'
)
x = ct.fit_transform(x)
# to not display the 1st coloumn
x = x[:,1:]
# print(x)
# train and predict model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
print(model.predict([[0,0,3400]]))
