import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from warnings import simplefilter 

simplefilter(action = 'ignore', category = FutureWarning)

print("-----Supervised Machine Learning-------")
print("-----Diabetes predictor using Logistic Regression------")

diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

x_train,x_test,y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify = diabetes['Outcome'],random_state = 66)

logret = LogisticRegression()
logret.fit(x_train,y_train)

print("Accuracy on training set : {:.3f}".format(logret.score(x_train,y_train)))
print("Accuracy on testing set : {:.3f}".format(logret.score(x_test,y_test)))

logret001 = LogisticRegression(C = 0.01).fit(x_train,y_train)

print("Accuracy on training set :{:.3f}".format(logret001.score(x_train,y_train)))
print("Accuracy on testing set : {:.3f}".format(logret001.score(x_test,y_test)))