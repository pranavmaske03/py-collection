import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

def LoanApproval():

    #Load Data
    data = pd.read_csv(r'C:\Users\91779\Desktop\Python2\CSV\Loan_Data.csv')
    #print(type(data))  dataframe
    #print("Data before cleaning : \n",data)
    print("Shape of data before cleaning : ",data.shape)

    data.drop(['Loan_ID','Gender','Married','Education','Dependents','Self_Employed'], axis=1,inplace = True)

    #loan_amount_term if NaN set to 360
    data.fillna({'Loan_Amount_Term' : 360},inplace = True)
    x = int(data['LoanAmount'].mean(axis = 0))
    data.fillna({'LoanAmount' : x},inplace = True)

    #if credit history null and loan_status N then set 0 else 1
    for x in data.index:
        y = data.loc[x,'Credit_History']
        if np.isnan(y) and data.loc[x,'Loan_Status'] == 'Y':
            data.loc[x,'Credit_History'] = 1
        else:
            data.loc[x,'Credit_History'] = 0

    #data.drop_duplicates(inplace = True)   drops duplicates here none
    data.dropna(inplace = True)

    #print("Data after cleaning : \n",data)
    print("Shape of data after cleaning: ",data.shape)
    


    #Data Encoding
    le = LabelEncoder()

    Y = data['Loan_Status'].values
    Y = le.fit_transform(Y)
    data.drop(['Loan_Status'],inplace = True,axis = 1)
    data["Property_Area"] = le.fit_transform(data["Property_Area"])

    Features = list(zip(data.ApplicantIncome,data.CoapplicantIncome,data.LoanAmount,data.Loan_Amount_Term,data.Credit_History,data.Property_Area))


    print("Features after encoding : ")
    print(Features)
    print("Labels after encoding : ")
    print(Y)




def main():
    separator = "-"*50
    print(separator)
    print("Supervised Machine Learning")
    print(separator)
    print("Loan Approval using KNN Algorithm")
    print(separator)

    LoanApproval()

if __name__ == "__main__":
    main()