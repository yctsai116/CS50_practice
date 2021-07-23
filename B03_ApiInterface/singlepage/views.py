from django.http import Http404, HttpResponse
from django.shortcuts import render

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

jsonObject={
    "squadName" : "Super hero squad",
    "homeTown" : "Metro City",
    "formed" : 2016,
    "secretBase" : "Super tower",
    "active" : "true",
    "members" : [
      {
        "name" : "Molecule Man",
        "age" : 29,
        "secretIdentity" : "Dan Jukes",
        "powers" : [
          "Radiation resistance",
          "Turning tiny",
          "Radiation blast"
        ]
      },
      {
        "name" : "Madame Uppercut",
        "age" : 39,
        "secretIdentity" : "Jane Wilson",
        "powers" : [
          "Million tonne punch",
          "Damage resistance",
          "Superhuman reflexes"
        ]
      },
      {
        "name" : "Eternal Flame",
        "age" : 1000000,
        "secretIdentity" : "Unknown",
        "powers" : [
          "Immortality",
          "Heat Immunity",
          "Inferno",
          "Teleportation",
          "Interdimensional travel"
        ]
      }
    ]
  }
df = pd.json_normalize(jsonObject, 'members', ['squadName', 'homeTown', 'formed'], 
                    record_prefix='members_')

# Create your views here.
def index(request):
    return render(request, "singlepage/index.html")

texts = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam tortor mauris, maximus semper volutpat vitae, varius placerat dui. Nunc consequat dictum est, at vestibulum est hendrerit at. Mauris suscipit neque ultrices nisl interdum accumsan. Sed euismod, ligula eget tristique semper, lectus est pellentesque dui, sit amet rhoncus leo mi nec orci. Curabitur hendrerit, est in ultricies interdum, lacus lacus aliquam mauris, vel vestibulum magna nisl id arcu. Cras luctus tellus ac convallis venenatis. Cras consequat tempor tincidunt. Proin ultricies purus mauris, non tempor turpis mollis id. Nam iaculis risus mauris, quis ornare neque semper vel.",
        "Praesent euismod auctor quam, id congue tellus malesuada vitae. Ut sed lacinia quam. Sed vitae mattis metus, vel gravida ante. Praesent tincidunt nulla non sapien tincidunt, vitae semper diam faucibus. Nulla venenatis tincidunt efficitur. Integer justo nunc, egestas eget dignissim dignissim, fermentum ac sapien. Suspendisse non libero facilisis, dictum nunc ut, tincidunt diam.",
        "Morbi imperdiet nunc ac quam hendrerit faucibus. Morbi viverra justo est, ut bibendum lacus vehicula at. Fusce eget risus arcu. Quisque dictum porttitor nisl, eget condimentum leo mollis sed. Proin justo nisl, lacinia id erat in, suscipit ultrices nisi. Suspendisse placerat nulla at volutpat interdum. In porttitor condimentum est nec ultricies. Donec nec mollis neque, id dapibus sem."]

def section(request, num):
    if 1 <= num <= 3:
        return HttpResponse(df.iloc[num - 1])
    else:
        raise Http404("No such section")
