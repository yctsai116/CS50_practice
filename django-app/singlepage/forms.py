from django import forms


class OperatorInfo(forms.Form):
    senderCode = forms.CharField(max_length=9,
                                 widget=forms.TextInput(attrs={'class': "form-control", 'id': "senderCode"}),required=False)
    operatorCode = forms.CharField(label='operator code', max_length=10,
                                   widget=forms.TextInput(attrs={'class': "form-control", 'id': "operatorCode"}),required=False)
    unitCode = forms.CharField(label='unit code', max_length=10,
                               widget=forms.TextInput(attrs={'class': "form-control", 'id': "unitCode"}),required=True)
    identityType = forms.CharField(label='identify type', max_length=1,
                                   widget=forms.TextInput(attrs={'class': "form-control", 'id': "identifyType"}),required=True)
    cbCustId = forms.CharField(label='cb cust id', max_length=20,
                               widget=forms.TextInput(attrs={'class': "form-control", 'id': "cbCustId"}),required=False)
    ccCustId = forms.CharField(label='cc cust id', max_length=20,
                               widget=forms.TextInput(attrs={'class': "form-control", 'id': "ccCustId"}),required=False)
    custId = forms.CharField(label=' cust id', max_length=50,
                             widget=forms.TextInput(attrs={'class': "form-control", 'id': "custId"}),required=False)
    birthDt = forms.CharField(label='birth day',
                              widget=forms.TextInput(attrs={'class': "form-control", 'id': "birthDt", 'type': "date"}),required=False)
    custName = forms.CharField(label='cust name', max_length=200,
                               widget=forms.TextInput(attrs={'class': "form-control", 'id': "custName"}),required=False)

    msgNo = forms.CharField(label='cust name', max_length=200,
                            widget=forms.TextInput(attrs={'class': "form-control", 'id': "msgNo"}),required=False)

    txnCode = forms.CharField(label='cust name', max_length=200,
                              widget=forms.TextInput(attrs={'class': "form-control", 'id': "txnCode"}),required=False)

    txnTime = forms.CharField(label='cust name', max_length=200,
                              widget=forms.TextInput(attrs={'class': "form-control", 'id': "txnTime", "type": "date"}),required=False)

    receiveCode = forms.CharField(label='cust name', max_length=200,
                                  widget=forms.TextInput(attrs={'class': "form-control", 'id': "receiveCode"}),required=False)

    authorizerCode = forms.CharField(label='cust name', max_length=200,
                                     widget=forms.TextInput(attrs={'class': "form-control", 'id': "authorizerCode"}),required=False)


class RequestDetailsForm(forms.Form):
    api_content = forms.CharField(label='api_content', max_length=200,
                                     widget=forms.TextInput(attrs={'class': "form-control", 'id': "apiContent"}))
    notes = forms.CharField(label='api_content', max_length=200,
                                  widget=forms.Textarea(attrs={'class': "form-control", 'id': "notes", "rows": 6}))
