# Loan Approval Predictor

I plan to use a logistic regression model to predict whether a financial institution is likely to approve a particular loan based on multiple inputs for a client.
The model will be trained using the following dataset: https://www.kaggle.com/vikasukani/loan-eligibility-prediction-machine-learning/

This is a capstone project developed as part of the MAIS 202 Bootcamp organized by the McGill Artificial Intelligence Society.

# Running the app
To run the web app, install all packages in requirements.txt. Then, change into the main directory of this repository and run
`python manage.py runserver`
Open a browser and navigate to http://127.0.0.1:8000/

# Repository organization
The repository contains all the script that were used to pre-process the data, train the model and build the website.
1. reports/
    - contains all the reports that were submitted for deliverables 1-2-3
2. data/
    - contains the datasets that were used to train and test the model
    - contains pickle version of the saved model and weights
3. images/
    - contains all the images that were submitted as part of the deliverable reports
4. loanpredictor/
    - contains all the files necessary for the django main app
5. model/
    - contains all the python scripts that were used to clean the data and train the model
6. website/
    - contains all the django web app setting files
7. manage.py
    - Main script used to run the django web app
8. requirements.txt
    - File containing all the requirements needed to run this project
    
