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


api_resj_m = api_resj["resultBody"]["resultJson"][0]["items"]
print(api_resj_m)
