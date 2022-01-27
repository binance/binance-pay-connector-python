#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging
# from binance.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
response = client.transfer_fund(
  "1241", # requestId
  "USDT", # currency
  "1.00", # amount
  "TO_MAIN", # transferType, Only "TO_MAIN" OR "TO_PAY"
)
