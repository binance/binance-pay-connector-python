from binance.pay.api import API

class Merchant(API):
  def __init__(self, key=None, secret=None, **kwargs):
    if "base_url" not in kwargs:
      kwargs["base_url"] = "https://bpay.binanceapi.com"
    super().__init__(key, secret, **kwargs)

  def query_order(self, merchantId: str, **kwargs):

    url_path = '/binancepay/openapi/order/query'
    params = {"merchantId": merchantId, **kwargs}
    return self.send_signed_request("POST", url_path, params)
