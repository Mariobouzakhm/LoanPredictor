from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

from model.processing import processed_dataset
from matplotlib import pyplot as plt

import seaborn as sns
import pickle


def logistic_regression(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, Y_train)

    return model


def save_model(model, filename):
    file = open(filename, 'wb')
    pickle.dump(model, file)


def load_model(filename):
    file = open(filename, 'rb')
    model = pickle.load(file)

    return model


def predict_values(model, X):
    return model.predict(X)


def main():
    dataset = processed_dataset(True, 'loan-train.csv')

    Y = dataset.Loan_Status
    X = dataset.drop('Loan_Status', axis=1)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, shuffle=False)

    model = logistic_regression(X_train, Y_train)

    Y_pred = predict_values(model, X_train)
    Y_test_pred = predict_values(model, X_test)

    print("Classification Report for Y_train/Y_Pred")
    print(classification_report(Y_train, Y_pred))

    print("Classification Report for Y_Test/Y_Test_Pred")
    print(classification_report(Y_test, Y_test_pred))

    matrix = confusion_matrix(Y_train, Y_pred)
    sns.heatmap(matrix, annot=True)

    plt.show()

    matrix2 = confusion_matrix(Y_test, Y_test_pred)
    sns.heatmap(matrix2, annot=True)

    plt.show()


if __name__ == "__main__":
    main()