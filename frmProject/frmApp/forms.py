from django import forms

class EmpApplication(forms.Form):
    name = forms.CharField()
    birthday = forms.DateField()
    applyingTo = forms.CharField()
    salary = forms.IntegerField()