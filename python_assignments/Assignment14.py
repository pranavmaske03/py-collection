from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
import csv


def K_NearestNeighbor():
    border = '_'*50

    Features = []
    Labels = []

    file = open('PlayPredictor.csv','r')
    readcsv = csv.reader(file)

    for data in readcsv:
        Features.append([data[0],data[1]])
        Labels.append(data[2])

    label_encoder = LabelEncoder()
    feature_encoder = OrdinalEncoder()

    label_encoder.fit(Labels)
    feature_encoder.fit(Features)

    encoded_labels = label_encoder.transform(Labels)
    encoded_features = feature_encoder.transform(Features)

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(encoded_labels)):
        print("ID : %d, Label : %s, Features : %s"%(i,encoded_labels[i],encoded_features[i]))
    print("Size of actual data set is : %d"%(i+1))

    data_train,data_test,target_train,target_test = train_test_split(encoded_features,encoded_labels,test_size = 0.5)

    print(border)
    print("Training data set ")
    print(border)

    for i in range(len(data_test)):
        print("ID : %d, Label : %s, Features : %s"%(i,target_test[i],data_test[i]))
    print("Size of Test data set is : %d"%(i+1))
    print(border)

    obj = KNeighborsClassifier(n_neighbors=3)
    obj.fit(data_train,target_train)

    predictions = obj.predict(data_test)

    print(predictions)

    Accuracy = accuracy_score(target_test,predictions)
    return Accuracy

def main():
    
    Accuracy = K_NearestNeighbor()
    print("Accuracy is : ",Accuracy*100,"%")


if __name__ == "__main__":
    main()