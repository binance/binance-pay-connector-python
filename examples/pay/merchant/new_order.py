#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging


config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)

parameters = {
    "env": {"terminalType": "MINI_PROGRAM"},
    "merchantTradeNo": "2223",
    "orderAmount": 1.00,
    "currency": "USDT",
    "goods": {
        "goodsType": "01",
        "goodsCategory": "0000",
        "referenceGoodsId": "abc001",
        "goodsName": "apple",
        "goodsUnitAmount": {"currency": "USDT", "amount": 1.00},
    },
    "shipping": {
        "shippingName": {"firstName": "Joe", "lastName": "Don"},
        "shippingAddress": {"region": "NZ"},
    },
    "buyer": {"buyerName": {"firstName": "cz", "lastName": "zhao"}},
}

response = client.new_order(parameters)
print(response)
