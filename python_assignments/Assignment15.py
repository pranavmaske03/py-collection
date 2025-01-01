import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def K_NearestNeighbor():
    border = '_'*50

    Features = []
    Labels = []

    file_name = open('WinePredictor.csv','r')
    read_csv = pd.read_csv(file_name)

    Labels = read_csv['Class'].tolist()

    F1 = read_csv['Alcohol'].tolist()
    F2 = read_csv['Malic acid'].tolist()
    F3 = read_csv['Ash'].tolist()
    F4 = read_csv['Alcalinity of ash'].tolist()
    F5 = read_csv['Magnesium'].tolist()
    F6 = read_csv['Total phenols'].tolist()
    F7 = read_csv['Flavanoids'].tolist()
    F8 = read_csv['Nonflavanoid phenols'].tolist()
    F9 = read_csv['Proanthocyanins'].tolist()
    F10 = read_csv['Color intensity'].tolist()
    F11 = read_csv['Hue'].tolist()
    F12 = read_csv['OD280/OD315 of diluted wines'].tolist()
    F13 = read_csv['Proline'].tolist()

    for i in range(len(read_csv)):
        Features.append([F1[i],F2[i],F3[i],F4[i],F5[i],F6[i],F7[i],F8[i],F9[i],F10[i],F11[i],F12[i],F13[i]])

    
    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(Labels)):
        print("ID : %d, Label : %s, Features : %s"%(i+1,Labels[i],Features[i]))
    print("Size of actual data set is : %d"%(i+1))

    data_train,data_test,target_train,target_test = train_test_split(Features,Labels,test_size = 0.5)


    print(border)
    print("Training data set ")
    print(border)

    for i in range(len(data_test)):
        print("ID : %d, Label : %s, Features : %s"%(i+1,target_test[i],data_test[i]))
    print("Size of Test data set is : %d"%(i+1))
    print(border)

    obj = KNeighborsClassifier(n_neighbors=7)
    obj.fit(data_train,target_train)

    predictions = obj.predict(data_test)

    Accuracy = accuracy_score(target_test,predictions)
    return Accuracy

def main():
    Accuracy = K_NearestNeighbor()
    print("Accuracy is : ",Accuracy*100,"%")   

if __name__ == "__main__":
    main()