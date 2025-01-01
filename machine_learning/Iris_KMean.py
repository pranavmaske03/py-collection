import numpy as np 
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split

def main():
    border = 60*'-'

    print(border)
    print("Unsupervised Machine Learning")
    print(border)
    print("----------Iris Case study using Unsupervised Machine Learning------------------")

    _iris = load_iris()
    data = _iris.data

    kmeans = KMeans(n_clusters = 3, random_state = 2)
    kmeans.fit(data)

    pred = kmeans.fit_predict(data)

    centers = kmeans.cluster_centers_
    print(centers)

if __name__ == "__main__":
    main()