from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():

    # Load dataset
    wine = datasets.load_wine()

    #print the names of the features
    print(wine.feature_names)

    # print the label species(class_0,class_1,class_2)
    print(wine.target_names)

    # print the wine data(top 5 records)
    print(wine.data[0:5])

    # print the wine labels (0:class_1,1:class_1,2:class_3)
    print(wine.target)

    #split dataset into trinning set and test set
    x_train,x_test,y_train,y_test = train_test_split(wine.data,wine.target,test_size = 0.3)

    knn = KNeighborsClassifier(n_neighbors = 5)

    knn.fit(x_train,y_train)

    y_pred = knn.predict(x_test)

    print("Accuracy : ",metrics.accuracy_score(y_test,y_pred))

def main():
    print("Machine Learning Application")
    print("-----------------------------------------------")
    print("Wine predictor application using KNN")
    print("--------------------------------------------------")

    WinePredictor()

if __name__ == "__main__":
    main()
