#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging


config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
response = client.cancel_order(prepayId="122490746078691329")
