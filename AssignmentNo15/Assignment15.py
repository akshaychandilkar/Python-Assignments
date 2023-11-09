import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def WineClassifier(data_path):
    # Step 1: Get Data - Load data from the CSV file
    data = pd.read_csv(data_path)

    print(f"Loaded data from {data_path}")
    print("Size of Actual dataset", len(data))

    # Step 2: Clean, Prepare, and Manipulate data
    # Extract features and labels
    features = data.drop('Class', axis=1)  
    labels = data['Class']

    # Standardize the features (scaling)
    scaler = preprocessing.StandardScaler()
    features = scaler.fit_transform(features)

    # Step 3: Train Data
    # Split the data into training (70%) and testing (30%)
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)

    # Train the model using the training dataset
    model.fit(features_train, labels_train)

    # Step 4: Test Data

    class_names = ['Class 1', 'Class 2', 'Class 3']

    for i in range(1, 4):
        test_data = np.array([[14.23, 1.71, 2.43, 15.6, 127, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065]])
        test_data = scaler.transform(test_data)
        predicted = model.predict(test_data)

        result = class_names[i - 1]
        print(f"Predicted Class: {result}")

        if result == 'Class 1':
            print("Result: Yes")
        else:
            print("Result: No")
    
    CheckAccuracy(features, labels)

def CheckAccuracy(features, labels):
    # Split the data into training (70%) and testing (30%)
    features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

    # Initialize a dictionary to store accuracy values for different values of K
    accuracies = {}

    for k in range(3,6):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(features_train, labels_train)
        predictions = model.predict(features_test)
        accuracy = accuracy_score(labels_test, predictions)
        accuracies[k] = accuracy

    print("Accuracies for different values of K:", accuracies)

def main():
    print("-----Marvellous Infosystems by Piyush Khairnar-----")
    print("Machine Learning Application")
    print("Wine Classification using K Nearest Neighbor algorithm")
    
    data_file = "WinePredictor.csv"
    print(f"Using data file: {data_file}")

    WineClassifier(data_file)

if __name__ == "__main__":
    main()
