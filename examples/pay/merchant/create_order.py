#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging
# from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
response = client.create_order(
  "111111",  # merchantTradeNo
  "WEB",  # tradeType
  10.11,  # totalFee
  "USDT",  # currency
  "gift card",  # productType
  "bitcoin gift card",  # productName
  merchantId=123456,
  productDetail="details of bitcoin gift card",
  returnUrl="https://localhost"
)
