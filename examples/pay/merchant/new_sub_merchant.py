#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging


config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
response = client.new_sub_merchant(
    merchantName="test_merchant",
    merchantType=1,
    merchantMcc="MCC_Code",
    country="GO,NZ",
)
