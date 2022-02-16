#!/usr/bin/env python

import logging
from binance.pay.merchant import Merchant as Client
from binance.pay.lib.utils import config_logging


config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret)
response = client.refund_order(
    refundRequestId="1234", prepayId="1111111", refundAmount="0.1"
)
