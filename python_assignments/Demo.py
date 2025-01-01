from sklearn import preprocessing 
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder
import csv
import pandas as pd

Features = []
Labels = []

file_name = open('WinePredictor.csv','r')
read_csv = pd.read_csv(file_name) # usecols=['Class','Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline'])

print(len(read_csv))

for row in read_csv:
    print(row.head())
