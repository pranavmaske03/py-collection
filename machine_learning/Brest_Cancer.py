##########################################################################
# Required Python Packages
##########################################################################
import pandas as pd 
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 

##########################################################################
# File Paths
##########################################################################
INPUT_PATH = "breast-cancer-wisconsin.data"
OUTPUT_PATH = "breast-cancer-wisconsin.csv"

##########################################################################
# Headers
##########################################################################

HEADERS = ['CodeNumber','ClumpThickness','UniformityCellSize','UniformityCellShape','MarginalAdhesion','SingleEpithelialCellSize','BareNuclei','BlandChromatin','NormalNucleoli','Mitoses','CancerType']

##########################################################################
# Function Name : read_data
# Description : Read the data into pandas dataframe
# Input : path of CSV file
# Output : Gives the data
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def read_data(path):
    data = pd.read_csv(path)
    return data 

##########################################################################
# Function Name : get_headers
# Description : dataset headers
# Input : dataset
# Output : Returns the header
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def get_headers(dataset):
    return dataset.columns.values

##########################################################################
# Function Name : add_headers
# Description : Add the headers to the dataset
# Input : dataset
# Output : Updated dataset
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def add_headers(dataset,headers):
    dataset.columns = headers
    return dataset

##########################################################################
# Function Name : data_file_to_csv
# Input : Nothing
# Output : Write the data to CSV
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def data_file_to_csv():
    #Headers
    headers  = ['CodeNumber','ClumpThickness','UniformityCellSize','UniformityCellShape','MarginalAdhesion','SingleEpithelialCellSize','BareNuclei','BlandChromatin','NormalNucleoli','Mitoses','CancerType']

    # Load the data into pandas data frame
    dataset = read_data(INPUT_PATH)

    # Add the headers to the loaded dataset
    dataset = add_headers(dataset,headers)

    # Save the loaded dataset into csv format
    dataset.to_csv(OUTPUT_PATH,index = False)
    print("File Saved...!")

##########################################################################
# Function Name : split_dataset
# Description : Split the dataset with train perentage
# Input : dataset with related information
# Output : Dataset after splitting
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def split_dataset(dataset,train_percentage,feature_headers,target_header):
    # split dataset into train and test dataset

    train_x,test_x,train_y,test_y = train_test_split(dataset[feature_headers],dataset[target_header],train_size = train_percentage)
    return train_x,test_x,train_y,test_y

#########################################################################
# Function Name : Handle missing values
# Description : Filter missing values from the dataset
# Input : Dataset with missing values
# Output : Dataset by removing missing values
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def handel_missing_values(dataset,missing_values_header,missing_label):
    return dataset[dataset[missing_values_header] != missing_label]

#########################################################################
# Function Name : random_forest_classifier
# Description : To train the random forest classifier with features and target data
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def random_forest_classifier(features,target):
    clf = RandomForestClassifier()
    clf.fit(features,target)
    return clf

#########################################################################
# Function Name : dataset_statistics
# Description : Basic statistics of the dataset
# Input : Dataset
# Output : Description of dataset
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def dataset_statistics(dataset):
    print(dataset.describe())

#########################################################################
# Function Name : main
# Description : Main function from where execution starts
# Author : Pranav Maske
# Date : 07/07/2024
##########################################################################
def main():
    # Load the csv file into pandas dataframe
    dataset = pd.read_csv(OUTPUT_PATH)

    # Get basic statics of the loaded dataset
    dataset_statistics(dataset)

    # Filter missing vlues
    dataset = handel_missing_values(dataset,HEADERS[6],'?')
    train_x,test_x,train_y,test_y = split_dataset(dataset,0.7,HEADERS[1:-1],HEADERS[-1])

    # Train and Test dataset size details
    print("Train_x Shape :: ",train_x.shape)
    print("Train_y Shape :: ",train_y.shape)
    print("Test_x Shape :: ",test_x.shape)
    print("Test_y Shape :: ",test_y.shape)

    # Create fandom forest classifier instance
    trained_model = random_forest_classifier(train_x,train_y)
    print("Trained model :: ",trained_model)
    predict = trained_model.predict(test_x)

    for i in range(0,205):
        print("Actual outcome :: {} and Predicted outcome :: {}".format(list(test_y)[i],predict[i]))
        
    print("Train Accuracy ",accuracy_score(train_y,trained_model.predict(train_x)))
    print("Test accuracy :: ",accuracy_score(test_y,predict))
    print("Cuonfusion matrix ",confusion_matrix(test_y,predict))

##########################################################################
# Application starter
##########################################################################
if __name__ == "__main__":
    main()