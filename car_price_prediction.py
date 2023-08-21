# -*- coding: utf-8 -*-
"""car price prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AbrtdOD8qit0sihDD7HiWMDFukOHu2Sg

# **importing requried libraies and datasets**
"""

import numpy as np
import pandas as pd

df=pd.read_csv("car_data.csv")

df.head()

df.shape

df.info()

"""here we came to know there are no null values in our entire datasets"""

df.describe()

"""# **encoding the data**"""

df['fuel'].value_counts()

df['seller_type'].value_counts()

df['transmission'].value_counts()

df['owner'].value_counts()

"""we are going  to split the data set into dependent and independent here selling price we have to predict so this will be consider as dependent col (y)"""

x=df.iloc[:,[1,3,4,6]].values

y=df.iloc[:,2].values

"""the col seller type ,name,owner are not balanced or outliers so we are not going to use them for training purpose as they are reduing our accuracy"""

from sklearn.preprocessing import LabelEncoder
lb1=LabelEncoder()
x[:,2]=lb1.fit_transform(x[:,2])
lb2=LabelEncoder()
x[:,3]=lb2.fit_transform(x[:,3])

"""Label encoding is a technique used in machine learning and data analysis to convert categorical variables into numerical format"""

x

"""# splitting the data into training and testing data sets"""

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.7,random_state=0)

xtrain.shape

from sklearn.ensemble import RandomForestRegressor
model=RandomForestRegressor(n_estimators=500,random_state=0)
model.fit(xtrain,ytrain)

accuracy=model.score(xtest,ytest)
print(accuracy*100,'%')

"""# testing"""

new=[2017,70000,"Petrol","Manual"]

new[2]=lb1.transform([new[2]])[0]
new[3]=lb2.transform([new[3]])[0]

model.predict([new])

