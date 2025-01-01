#Linear Regression using inbuild algorigham

import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def MarvellousHeadBrainPredictor():
    
    # Load data
    data = pd.read_csv('MarvellousHeadBrain.csv')

    print("Size of the data set",data.shape)

    X = data['Head Size(cm^3)'].values
    Y = data['Brain Weight(grams)'].values

    X = X.reshape((-1,1))
    n = len(X)

    reg = LinearRegression()

    ret = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)

def main():
    print("----------Supervised Machine Learning----------------")
    print("-----------------------------------------------------")
    print("Linear Regression on head and brain size data set")
    print("------------------------------------------------------")

    MarvellousHeadBrainPredictor()

if __name__ == "__main__":
    main()