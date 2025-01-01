from sklearn import tree
from scipy.spatial import distance
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def euc(a,b):
    return distance.euclidean(a,b)

class MarvellousKNN:
    
    def fit(self,training_data,training_target):
        self.training_data = training_data
        self.training_target = training_target
    
    def predict(self,test_data):
        predictions = []
        for row in test_data:
            lebel = self.closest(row)
            predictions.append(lebel)
        return predictions
    
    def closest(self,row):
        best_distance = euc(row,self.training_data[0])
        best_index = 0
        for i in range(1,len(self.training_data)):
            dist = euc(row,self.training_data[i])
            if dist < best_distance:
                best_distance = dist
                best_index = i 
        return self.training_target[best_index]

def K_NearestNeighbor():
    border = '_'*50

    iris = load_iris()

    data = iris.data
    target = iris.target

    print(border)
    print("Actual data set")
    print(border)

    for i in range(len(iris.target)):
        print("ID : %d,Label : %s, Feature : %s"%(i,iris.data[i],iris.target[i]))
    print("Size of actual data set is : %d"%(i+1))

    data_train,data_test,target_train,target_test = train_test_split(data,target,test_size = 0.5)

    print(border)
    print("Training data set ")
    print(border)
    
    for i in range(len(data_test)):
        print("ID : %d, Label : %s, Feature : %s"%(i,data_test[i],target_test[i]))
    print("Size of Test data set is : %d"%(i+1))
    print(border)

    classifier = MarvellousKNN()
    classifier.fit(data_train,target_train)

    predictions = classifier.predict(data_test)

    Accuracy = accuracy_score(target_test,predictions)
    return Accuracy


def main():
    Accuracy = K_NearestNeighbor()
    print("Accuracy of classification algoritham with k Neighbor cassifier is : ",Accuracy*100,"%")


if __name__ == "__main__":
    main()

