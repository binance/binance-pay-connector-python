#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging

# from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)

parameters = {
    "requestId": "123461",
    "bizScene": "DIRECT_TRANSFER",
    "batchName": "test_batch",
    "currency": "USDT",
    "totalAmount": 0.02,
    "totalNumber": 2,
    "transferDetailList": [
        {
            "merchantSendId": "1",
            "receiveType": "BINANCE_ID",
            "receiver": "88035013",
            "transferAmount": 0.01,
            "transferMethod": "FUNDING_WALLET",
            "remark": "test1",
        },
        {
            "merchantSendId": "2",
            "receiveType": "BINANCE_ID",
            "receiver": "88035013",
            "transferAmount": 0.01,
            "transferMethod": "FUNDING_WALLET",
            "remark": "test2",
        },
    ],
}

response = client.batch_payout(parameters)
print(response)
