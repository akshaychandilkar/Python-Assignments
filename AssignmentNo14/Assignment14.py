import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def MarvellousPlayPredictor(data_path):
    # Step 1: Load data
    data = pd.read_csv(data_path, index_col=0)

    print(f"Loaded data from {data_path}")

    print("Size of Actual dataset", len(data))

    # Step 2: Clean, Prepare, and manipulate data
    feature_names = ['Whether', 'Temperature']

    print("Names of Features", feature_names)

    whether = data['Whether']
    Temperature = data['Temperature']
    play = data['Play']

    # Creating labelEncoder
    le = preprocessing.LabelEncoder()

    # Converting string labels into numbers
    whether_encoded = le.fit_transform(whether)
    temp_encoded = le.fit_transform(Temperature)
    label = le.fit_transform(play)

    # Combining weather and temp into a single list of tuples
    features = list(zip(whether_encoded, temp_encoded))

    # Step 3: Train Data
    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the entire dataset
    model.fit(features, label)

    # Step 4: Test Data
    test_data = [[0, 2]] 
    predicted = model.predict(test_data)
    result = 'Yes' if predicted[0] == 1 else 'No'
    print(f"Result: {result}")

    # Step 5: Calculate Accuracy
    CheckAccuracy(features, label)

def CheckAccuracy(features, label):
    # Split the data into training and testing sets
    features_train, features_test, labels_train, labels_test = train_test_split(features, label, test_size=0.5, random_state=42)

    # Initialize a dictionary to store accuracy values for different values of K
    accuracies = {}

    # Calculate accuracy for different values of K
    for k in range(3, 6):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(features_train, labels_train)
        predictions = model.predict(features_test)
        accuracy = accuracy_score(labels_test, predictions)
        accuracies[k] = accuracy

    print("Accuracies for different values of K:", accuracies)

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")
    print("Machine Learning Application")
    print("Play predictor application using K Nearest Neighbor algorithm")

    data_file = "MarvellousInfosystems_PlayPredictor.csv"  
    print(f"Using data file: {data_file}")

    MarvellousPlayPredictor(data_file)

if __name__ == "__main__":
    main()
