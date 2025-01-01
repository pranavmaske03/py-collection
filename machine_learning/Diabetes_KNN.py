import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

print("----------Supervised Machine Learning------------")
print("----------Diabetes predictor using K Nearest neighbour----------")

diabetes = pd.read_csv('diabetes.csv')

print("Columns of Dataset")
print(diabetes.columns)

print("First 5 records of dataset")
print(diabetes.head())

print("Dimension of diabetes data : {}".format(diabetes.shape))

x_train,x_test,y_train,y_test = train_test_split(diabetes.loc[:,diabetes.columns != 'Outcome'],diabetes['Outcome'],stratify = diabetes['Outcome'],random_state = 66)

training_accuracy = []
test_accuracy = []

# try n_neighbors from 1 to 10
neighbors_setting = range(1,11)

for n_neighbors in neighbors_setting:
    # build a model 
    knn = KNeighborsClassifier(n_neighbors = n_neighbors)
    knn.fit(x_train,y_train)
    # record training set accuracy
    training_accuracy.append(knn.score(x_train,y_train))
    # Record test set accuracy
    test_accuracy.append(knn.score(x_test,y_test))

plt.plot(neighbors_setting,training_accuracy,label = 'training accuracy')
plt.plot(neighbors_setting,test_accuracy,label = 'test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()
plt.savefig('knn_compare_model')
plt.show() 

knn = KNeighborsClassifier(n_neighbors = 9)
knn.fit(x_train,y_train)

print("Accuracy of K-NN classifier on trainning set : {:.2f}".format(knn.score(x_train,y_train)))
print("Accuracy of K-NN classifier on test set : {:2f}".format(knn.score(x_test,y_test)))