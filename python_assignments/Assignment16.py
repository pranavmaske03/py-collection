import pandas as pd 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def SalesPredictor():

    data = pd.read_csv('Advertising.csv')
    print("Size of the data set ",data.shape)

    X = data[['TV','radio','newspaper']].values
    Y = data.sales.values

    reg = LinearRegression()

    ret = reg.fit(X,Y)

    y_pred = reg.predict(X)

    r2 = reg.score(X,Y)

    print(r2)

    

def main():
    print("----------Supervised Machine Learning----------------")
    print("-----------------------------------------------------")
    print("Multiple Linear Regression")
    print("------------------------------------------------------")

    SalesPredictor()

if __name__ == "__main__":
    main()