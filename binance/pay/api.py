import json
import logging
import requests
from .__version__ import __version__

from binance.pay.lib.utils import get_timestamp
from binance.pay.lib.utils import random_string
from binance.pay.lib.utils import hashing


class API(object):
    """API base class"""

    def __init__(self, key=None, secret=None, base_url=None):
        self.key = key
        self.secret = secret
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8",
                "User-Agent": "binance-pay-connector/" + __version__,
            }
        )
        return

    def send_signed_request(self, http_method, url_path, payload={}):
        timestamp = get_timestamp()
        nonce = random_string()
        payload_to_sign = (
            str(timestamp) + "\n" + nonce + "\n" + json.dumps(payload) + "\n"
        )
        signature = hashing(self.secret, payload_to_sign)
        self.session.headers.update(
            {
                "BinancePay-Timestamp": str(timestamp),
                "BinancePay-Nonce": nonce,
                "BinancePay-Certificate-SN": self.key,
                "BinancePay-Signature": signature,
            }
        )
        url = self.base_url + url_path
        params = {"url": url, "data": json.dumps(payload)}
        logging.debug("payload:" + json.dumps(payload))
        response = self._dispatch_request(http_method)(**params)
        logging.debug("raw response from server:" + response.text)
        try:
            data = response.json()
        except ValueError:
            data = response.text

        return data

    def _dispatch_request(self, http_method):
        return {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "PUT": self.session.put,
            "POST": self.session.post,
        }.get(http_method, "GET")
