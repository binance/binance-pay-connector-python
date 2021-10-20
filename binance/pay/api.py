import hmac
import json
import logging
import hashlib
from json import JSONDecodeError
import requests
from .__version__ import __version__
# from binance.error import ClientError, ServerError
from binance.pay.lib.utils import get_timestamp
from binance.pay.lib.utils import random_string
from binance.pay.lib.utils import hashing


class API(object):
    """API base class
    Keyword Args:
        base_url (str, optional): the API base url, useful to switch to testnet, etc. By default it's https://api.binance.com
        timeout (int, optional): the time waiting for server response, number of seconds. https://docs.python-requests.org/en/master/user/advanced/#timeouts
        proxies (obj, optional): Dictionary mapping protocol to the URL of the proxy. e.g. {'https': 'http://1.2.3.4:8080'}
    """

    def __init__(
        self,
        key=None,
        secret=None,
        base_url=None
    ):
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
      payload_to_sign = str(timestamp) + "\n" + nonce + "\n" + json.dumps(payload) + "\n"
      signature = hashing(self.secret, payload_to_sign)
      self.session.headers.update(
        {
          'BinancePay-Timestamp': str(timestamp),
          'BinancePay-Nonce': nonce,
          'BinancePay-Certificate-SN': self.key,
          'BinancePay-Signature': signature
        }
      )
      url = self.base_url + url_path
      params = {"url": url, "data": json.dumps(payload) }
      response = self._dispatch_request(http_method)(**params)
      logging.debug("raw response from server:" + response.text)
      return response.json()

    def _dispatch_request(self, http_method):
      return {
          "GET": self.session.get,
          "DELETE": self.session.delete,
          "PUT": self.session.put,
          "POST": self.session.post,
      }.get(http_method, "GET")
