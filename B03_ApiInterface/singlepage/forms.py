from django import forms

class OperatorInfo(forms.Form):
    senderCode = forms.CharField(label='sender code', max_length=9)
    operatorCode = forms.CharField(label='operator code', max_length=10)
    unitCode = forms.CharField(label='unit code', max_length=10)