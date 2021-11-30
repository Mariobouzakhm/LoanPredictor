from django.shortcuts import render, redirect
import pandas as pd
from .forms import LoanPredictorForm
import pickle


def home(request):
    form = LoanPredictorForm()
    context = {
        'form': form
    }

    if request.method == 'GET':
        loan_form = LoanPredictorForm(request.GET)

        if loan_form.is_valid():
            gender = 0 if loan_form.cleaned_data.get("gender") == 'Female' else 1
            married = 0 if loan_form.cleaned_data.get("married") == 'No' else 1
            employed = 0 if loan_form.cleaned_data.get("employed") == 'Graduate' else 1
            education = 0 if loan_form.cleaned_data.get("education") == 'No' else 1
            dependants = loan_form.cleaned_data.get("dependants")

            if dependants == '0':
                dependants = [1, 0, 0, 0]
            elif dependants == '1':
                dependants = [0, 1, 0, 0]
            elif dependants == '2':
                dependants = [0, 0, 1, 0]
            else:
                dependants = [0, 0, 0, 1]

            applicantInc = int(loan_form.cleaned_data.get("applicant_Income"))
            coapplicantInc = int(loan_form.cleaned_data.get("coapplicant_Income"))

            loan_Amount = int(loan_form.cleaned_data.get("loan_Amount"))
            loan_Amount_Term = loan_form.cleaned_data.get("loan_Amount_Term")

            creditHistory = 0 if loan_form.cleaned_data.get("credit_History") == 'No' else 1

            property_Type = loan_form.cleaned_data.get("property_Type")

            if property_Type == 'Rural':
                property_Type = [1, 0, 0]
            elif property_Type == 'Semiurban':
                property_Type = [0, 1, 0]
            else:
                property_Type = [0, 0, 1]

            scales = pickle.load(open("C:\\Users\\mario\\Desktop\\Courses\\MAIS202\\project\\data\\scales.sav", 'rb'))
            applicantInc = applicantInc * scales[0]
            coapplicantInc = coapplicantInc * scales[1]
            loan_Amount = loan_Amount * scales[2]
            loan_Amount_Term = loan_Amount_Term * scales[3]

            data_dict = {
                'Gender': [gender],
                'Married': [married],
                'Education': [education],
                'Self_Employed': [employed],
                'ApplicantIncome': [applicantInc],
                'CoapplicantIncome': [coapplicantInc],
                'LoanAmount': [loan_Amount],
                'Loan_Amount_Term': [loan_Amount_Term],
                'Credit_History': [creditHistory],
                'D0': [dependants[0]],
                'D1': [dependants[1]],
                'D2': [dependants[2]],
                'D3': [dependants[3]],
                'P0': [property_Type[0]],
                'P1': [property_Type[1]],
                'P2': [property_Type[2]]
            }

            df = pd.DataFrame.from_dict(data_dict)

            model = pickle.load(open(
                "C:\\Users\\mario\\Desktop\\Courses\\MAIS202\\project\\data\\logistic_regression_model.sav", 'rb'))

            result = model.predict(df)

            if result[0] == 0:
                return redirect('rejected')
            elif result[0] == 1:
                return redirect('approved')
            else:
                return redirect('home')

    return render(request, 'loanpredictor/home.html', context)


def approved(request):
    return render(request, 'loanpredictor/approved_loan.html')


def rejected(request):
    return render(request, 'loanpredictor/rejected_loan.html')
