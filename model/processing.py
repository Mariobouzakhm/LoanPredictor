import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import pickle

from sklearn import preprocessing


def processed_dataset(train, name):
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    file_path = os.path.join(parent_directory + '\\data\\'+name)

    data = pd.read_csv(file_path)

    # Dropping the id column
    data.drop('Loan_ID', axis=1, inplace=True)

    # Dropping all the rows with missing values
    data = data.dropna()
    data.index = pd.RangeIndex(1, len(data) +1)

    # Replace all the string values with numbers that represent the categories.
    label_encoder = preprocessing.LabelEncoder()
    one_hot_encoder = preprocessing.OneHotEncoder()

    data['Gender'] = label_encoder.fit_transform(data['Gender'])
    print(label_encoder.classes_)

    data['Married'] = label_encoder.fit_transform(data['Married'])
    print(label_encoder.classes_)

    data['Education'] = label_encoder.fit_transform(data['Education'])
    print(label_encoder.classes_)

    data['Self_Employed'] = label_encoder.fit_transform(data['Self_Employed'])
    print(label_encoder.classes_)

    data['Property_Area'] = label_encoder.fit_transform(data['Property_Area'])
    print(label_encoder.classes_)

    data['Dependents'] = label_encoder.fit_transform(data['Dependents'])
    print(label_encoder.classes_)

    data.index.names = ['id']

    enc1_df = pd.DataFrame(one_hot_encoder.fit_transform(data[['Dependents']]).toarray())
    enc1_df.index = pd.RangeIndex(1, len(enc1_df) + 1)
    enc1_df.index.names = ['id']

    data = data.join(enc1_df, on="id")
    data.drop('Dependents', axis=1, inplace=True)
    data.columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
                    'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area', 'Loan_Status', 'D0', 'D1', 'D2',
                    'D3']

    enc2_df = pd.DataFrame(one_hot_encoder.fit_transform(data[['Property_Area']]).toarray())
    enc2_df.index = pd.RangeIndex(1, len(enc2_df) + 1)
    enc2_df.index.names = ['id']

    data = data.join(enc2_df, on='id')
    data.drop('Property_Area', axis=1, inplace=True)

    data.columns = ['Gender', 'Married', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
                    'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Loan_Status', 'D0', 'D1',
                    'D2', 'D3', 'P0', 'P1', 'P2']

    data = data[['Gender', 'Married', 'Education', 'Self_Employed', 'ApplicantIncome', 'CoapplicantIncome',
                    'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'D0', 'D1',
                    'D2', 'D3', 'P0', 'P1', 'P2', 'Loan_Status']]


    # Scaling values to give them all the same weight
    scaler = preprocessing.MinMaxScaler()
    ranges = []

    data['ApplicantIncome'] = scaler.fit_transform(data[['ApplicantIncome']])
    ranges.append(scaler.scale_[0])
    data['CoapplicantIncome'] = scaler.fit_transform(data[['CoapplicantIncome']])
    ranges.append(scaler.scale_[0])
    data['LoanAmount'] = scaler.fit_transform(data[['LoanAmount']])
    ranges.append(scaler.scale_[0])
    data['Loan_Amount_Term'] = scaler.fit_transform(data[['Loan_Amount_Term']])
    ranges.append(scaler.scale_[0])

    save_scales(ranges, "..\\data\\scales.sav")

    data['Loan_Status'] = label_encoder.fit_transform(data['Loan_Status'])
    print(label_encoder.classes_)

    return data


def plot_gender_data(data):
    sns.countplot('Gender', data=data)
    plt.show()


def plot_gender_vs_loan_status(data):
    sns.countplot(x='Loan_Status', hue='Gender', data=data)
    plt.show()


def plot_dependents_vs_loan_status(data):
    grouped = data.groupby(['Dependents', 'Loan_Status']).Loan_Status.count()
    print(grouped)

    sns.countplot(x='Loan_Status', hue='Dependents', data=data)
    plt.show()


def correlation_matrix(data):
    corr_matrix = data.corr()
    sns.heatmap(corr_matrix, annot=True)
    plt.show()


def save_scales(scale_list, filename):
    file = open(filename, 'wb')
    pickle.dump(scale_list, file)


def load_scales(filename):
    file = open(filename, 'rb')
    return pickle.load(file)


if __name__ == "__main__":
    dataset = processed_dataset(True, 'loan-train.csv')
    print(dataset)