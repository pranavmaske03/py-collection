import numpy as np 
import pandas as pd 
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def LoanApproval():

    features = []
    labels = []
    border = 60*'-'

    data = pd.read_csv('Loan_Data.csv')
    print(border)
    print("Size of the dataset before cleaning process : ",data.shape)

    data.fillna({'Self_Employed': 'No'},inplace = True)
    data.fillna({'Credit_History': 0},inplace = True)
    data.fillna({'Dependents': '0'},inplace = True)
    
    x = data["LoanAmount"].mean()
    data.fillna({'LoanAmount': x},inplace = True)

    x = data["Loan_Amount_Term"].mean()
    data.fillna({'Loan_Amount_Term': x},inplace = True)

    data = data.drop(['Loan_ID', 'Gender','Married'], axis=1)

    print("DataFrame shate after cleaning process is : ",data.shape)

    print(border)

    labels = data['Loan_Status'].values

    education = data['Education'].values
    self_employed = data['Self_Employed'].values
    property_area = data['Property_Area'].values
    dependents = data['Dependents'].values

    le = preprocessing.LabelEncoder()

    edu_encoding = le.fit_transform(education)
    employ_encoding = le.fit_transform(self_employed)
    property_encoding = le.fit_transform(property_area)
    dependents_encoding = le.fit_transform(dependents)
    label_encoding = le.fit_transform(labels)

    features = list(zip(edu_encoding,employ_encoding,property_encoding,dependents_encoding,data.ApplicantIncome,data.CoapplicantIncome,data.LoanAmount,data.Loan_Amount_Term,data.Credit_History))

    data_train,data_test,target_train,target_test = train_test_split(features,labels,test_size = 0.5)

    model = KNeighborsClassifier(n_neighbors = 5)

    model.fit(data_train,target_train)

    output = model.predict(data_test)

    Accuracy = accuracy_score(target_test,output)

    print("Accuracy of model is : ",Accuracy*100)

    
def main():

    border = 60*'-'
    print("Machine Learning application")
    print(border)
    print("Loan Approval Application using KNN")
    print(border)

    LoanApproval()


if __name__ == "__main__":
    main()