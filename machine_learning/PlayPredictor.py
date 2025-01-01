import numpy as np 
import pandas as pd 
from sklearn import preprocessing 
from sklearn.neighbors import KNeighborsClassifier 

def MarvellousPlayPredictor(data_path):

    #step 1: Load data 
    data = pd.read_csv(data_path)

    print(("Size of actual dataset : ",len(data)))

    #X = data['Head Size(cm^3)'].values
    #Y = data['Brain Weight(grams)'].values

    whether = data['Whether'].values
    temprature = data['Temperature'].values
    play = data['Play'].values

    #creating labelEncoder
    le = preprocessing.LabelEncoder()

    #Converting string labels into numbers
    whether_encoded = le.fit_transform(whether)
    print(whether_encoded)

    # converting string labels into numbers
    temp_encoded = le.fit_transform(temprature)
    labels = le.fit_transform(play)

    print(temp_encoded)

    # combining weather and temp into single list of tuples
    features = list(zip(whether_encoded,temp_encoded))

    model = KNeighborsClassifier(n_neighbors = 5)

    model.fit(features,labels)

    predicted = model.predict([[0,2]])
    print(predicted)

def main():
    print("Machine learning application")
    print("-----------------------------------------------------")
    print("Play predictor application using KNN")
    print("-----------------------------------------------------")

    MarvellousPlayPredictor('PlayPredictor.csv')

if __name__ == "__main__":
    main()