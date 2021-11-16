from django.forms import Form
from django import forms


class LoanPredictorForm(Form):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female")
    )

    MARRIED_STATUS = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    EMPLOYED_STATUS = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    EDUCATION = (
        ("Graduate", "Graduate"),
        ("Non Graduate", "Non Graduate")
    )

    DEPENDANTS_COUNT = (
        ("0", "0"),
        ("1", "1"),
        ("2", "2"),
        ("3+", "3+")
    )

    PROPERTY_TYPE = (
        ("Rural", "Rural"),
        ("Urban", "Urban"),
        ("Semi-Urban", "Semi-Urban")
    )

    CREDIT_HISTORY = (
        ("Yes", "Yes"),
        ("No", "No")
    )

    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    married = forms.ChoiceField(choices=MARRIED_STATUS, required=True)
    employed = forms.ChoiceField(choices=EMPLOYED_STATUS, required=True)
    education = forms.ChoiceField(choices=EDUCATION, required=True)
    dependants = forms.ChoiceField(choices=DEPENDANTS_COUNT, required=True)

    applicant_Income = forms.IntegerField(min_value=0)
    coapplicant_Income = forms.IntegerField(min_value=0)

    loan_Amount = forms.IntegerField(min_value=0)
    loan_Amount_Term = forms.IntegerField(min_value=0)

    credit_History = forms.ChoiceField(choices=CREDIT_HISTORY, required=True)
    property_Type = forms.ChoiceField(choices=PROPERTY_TYPE, required=True)
