from django import forms

# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

class OperatorInfo(forms.Form):
    senderCode = forms.CharField(label='sender code', max_length=9,required=False)
    operatorCode = forms.CharField(label='operator code', max_length=10,required=False)
    unitCode = forms.CharField(label='unit code', max_length=10)
    identifyType = forms.CharField(label='identify type', max_length=1)
    cbCustId = forms.CharField(label='cb cust id',max_length=20,required=False)
    ccCustId = forms.CharField(label='cc cust id', max_length=20,required=False)
    custId = forms.CharField(label=' cust id',max_length=50,required=False)
    birthDt = forms.CharField(label='birth day',max_length=10,required=False)
    custName = forms.CharField(label='cust name',max_length=200,required=False)
    

class APIname(forms.Form):
    apiName_1 = forms.CharField(label='1st api name',max_length=100)
    apiName_2 = forms.CharField(label='2nd api name',max_length=100,required=False)
    apiName_3 = forms.CharField(label='3rd api name',max_length=100,required=False)
    apiName_4 = forms.CharField(label='4th api name',max_length=100,required=False)
    apiName_5 = forms.CharField(label='5th api name',max_length=100,required=False)
    # favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.Select(choices=FRUIT_CHOICES))