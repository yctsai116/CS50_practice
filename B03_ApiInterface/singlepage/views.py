from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import OperatorInfo, APIname
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

api_input={
  'senderCode':"",
  'operatorCode':"",
  'unitCode':"",
  'identifyType':"",
  'cbCustId':"",
  'ccCustId':"",
  'custId':"",
  'birthDt':"",
  'custName':""
}

api_name={
        'apiName_1':"",
        'apiName_2':"",
        'apiName_3':"",
        'apiName_4':"",
        'apiName_5':""
        }


def dummy_func(unitcode,id,api_name):
  return {'dummy_func':unitcode+id+api_name}


# Create your views here.
def index(request):
  if request.method == 'POST':
    dummy_response=dummy_func(api_input['unitCode'],api_input['custId'],api_name['apiName_1'])
    return render(request, "singlepage/index_new.html",{'api_input':api_input,'api_name':api_name,'dummy_response':dummy_response})
  else:
    return render(request, "singlepage/index.html",{'api_input':api_input,'api_name':api_name})

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
        form1 = OperatorInfo(request.POST)
        # check whether it's valid:
        if form1.is_valid():
            # process the data in form.cleaned_data as required
            api_input['senderCode'] = form1.cleaned_data['senderCode']
            api_input['operatorCode'] = form1.cleaned_data['operatorCode']
            api_input['unitCode'] = form1.cleaned_data['unitCode']
            api_input['identifyType'] = form1.cleaned_data['identifyType']
            api_input['cbCustId'] = form1.cleaned_data['cbCustId']
            api_input['ccCustId'] = form1.cleaned_data['ccCustId']
            api_input['custId'] = form1.cleaned_data['custId']
            api_input['birthDt'] = form1.cleaned_data['birthDt']
            api_input['custName'] = form1.cleaned_data['custName']  
            

            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("singlepage:addapi"))
            # return render(request, 'singlepage/index.html', {
            #   'senderCode': senderCode,
            #   'operatorCode':operatorCode,
            #   'unitCode':unitCode
            #   })

    # if a GET (or any other method) we'll create a blank form
    else:
        form1 = OperatorInfo()

    return render(request, 'singlepage/operator_info.html', {'form1': form1})

def add_api(request):
    
    if request.method == "POST":
        form2 = APIname(request.POST)
        if form2.is_valid():
            api_name['apiName_1'] = form2.cleaned_data["apiName_1"]
            api_name['apiName_2'] = form2.cleaned_data["apiName_2"]
            api_name['apiName_3'] = form2.cleaned_data["apiName_3"]
            api_name['apiName_4'] = form2.cleaned_data["apiName_4"]
            api_name['apiName_5'] = form2.cleaned_data["apiName_5"]
            return HttpResponseRedirect(reverse("singlepage:index"))
    else:
        form2 = APIname()


    return render(request, "singlepage/add_api.html",{
        'form2': form2
    })