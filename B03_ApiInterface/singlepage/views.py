from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import OperatorInfo
from django.urls import reverse

import pandas as pd

import requests
import json


# ==================================run on AP server=============================
# url = "http://localhost:8443/demandDepositAccountInformation"
# ============================================================
# The sender code, operator code and unit code should be filled via web interface
# ============================================================
# api_reqj={
  # "header":{
  #   "msgNo":"UP0185_20161111195800_001",
  #   "txnCode":"1010101",
  #   "txnTime":"2021-11-11 19:58:00",
  #   "senderCode": "UP0185",
  #   "receiveCode":"up0185",
  #   "operatorCode":"21853",
  #   "unitCode":"C105",
  #   "authorizerCode":"12345"
  # },
  # "requestBody":{
  #   "params":{
  #     "identifyType":"1",
  #     "custId":"",
  #     "custName":"",
  #     "birthDt":"",
  #     "cbCustId":"A123456789",
  #     "ccCustId":""
  #   }
  # }
# }
# ===============================end request data===============
# request api w/ url and request json (run local AP server
# api_reqj = requests.post(url, json=api_reqj).json()

# ==================the expact response==========================================
api_resj={'requestModel':{  
  "header":{
    "msgNo":"UP0185_20161111195800_001",
    "txnCode":"1010101",
    "txnTime":"2021-11-11 19:58:00",
    "senderCode": "UP0185",
    "receiveCode":"up0185",
    "operatorCode":"21853",
    "unitCode":"C105",
    "authorizerCode":"12345"
  },
  "requestBody":{
    "params":{
      "identifyType":"1",
      "custId":"",
      "custName":"",
      "birthDt":"",
      "cbCustId":"A123456789",
      "ccCustId":""
    }
  }},
  'resultCode':'0000',
  'resultDescription':'success',
  "resultBody":{'resultJson':
    [{"verifyCode":"0000",
    "verufyDescription":"success",
    "versionType":"S",
    "isManageNote":"N",
    "items":
      [{"cbCustId":"A123456789",
      "demandDepositAcct":"9216968000449",
      "acctType":"Living Account",
      "curr":"TWD",
      "openAcctDate":"20200811",
      "digitalSavingAcctMark":"NotDigitalAcct",
      "realBlnc":9.0,
      "prodName":"blablablabla",
      "lastMonthAvgAccrNo":None,
      "acctStatus":"normal"},
      {"cbCustId":"A123456789",
      "demandDepositAcct":"9216968000488",
      "acctType":"Saving Account",
      "curr":"TWD",
      "openAcctDate":"20200811",
      "digitalSavingAcctMark":"NotDigitalAcct",
      "realBlnc":131313.0,
      "prodName":"blablablabla",
      "lastMonthAvgAccrNo":None,
      "acctStatus":"normal"},
      {"cbCustId":"A123456789",
      "demandDepositAcct":"9216968000466",
      "acctType":"Saving Account",
      "curr":"TWD",
      "openAcctDate":"20200811",
      "digitalSavingAcctMark":"NotDigitalAcct",
      "realBlnc":5566.0,
      "prodName":"blablablabla",
      "lastMonthAvgAccrNo":None,
      "acctStatus":"normal"},
      {"cbCustId":"A123456789",
      "demandDepositAcct":"9216968000477",
      "acctType":"Saving Account",
      "curr":"TWD",
      "openAcctDate":"20200811",
      "digitalSavingAcctMark":"NotDigitalAcct",
      "realBlnc":778888.0,
      "prodName":"blablablabla",
      "lastMonthAvgAccrNo":None,
      "acctStatus":"normal"}
     ]
    }]  
  }}

# ===============================extract the main part of the api response=============================
api_resj_m = api_resj["resultBody"]["resultJson"][0]["items"]



# Create your views here.
def output(request):
    return render(request, "singlepage/output.html")


def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(pd.DataFrame([api_resj_m[num - 1]],index=None).to_html())
    else:
        raise Http404("No such section")

def operator_info(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = OperatorInfo(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            senderCode = form.cleaned_data['senderCode']
            operatorCode = form.cleaned_data['operatorCode']
            unitCode = form.cleaned_data['unitCode']
            # redirect to a new URL:
            return render(request, 'singlepage/index.html', {
              'senderCode': senderCode,
              'operatorCode':operatorCode,
              'unitCode':unitCode
              })

    # if a GET (or any other method) we'll create a blank form
    else:
        form = OperatorInfo()

    return render(request, 'singlepage/operator_info.html', {'form': form})



