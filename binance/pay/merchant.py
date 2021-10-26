from binance.pay.api import API

class Merchant(API):
  def __init__(self, key=None, secret=None, **kwargs):
    if "base_url" not in kwargs:
      kwargs["base_url"] = "https://bpay.binanceapi.com"
    super().__init__(key, secret, **kwargs)

  def create_order(self, merchantTradeNo: str, tradeType: str, totalFee: float, currency: str, productType: str, productName: str, **kwargs):
    url_path = '/binancepay/openapi/order'
    params = {
      "merchantTradeNo": merchantTradeNo,
      "tradeType": tradeType,
      "totalFee": totalFee,
      "currency": currency,
      "productType": productType,
      "productName": productName,
      **kwargs
    }
    return self.send_signed_request("POST", url_path, params)
    
  def query_order(self, merchantId: str, **kwargs):

    url_path = '/binancepay/openapi/order/query'
    params = {"merchantId": merchantId, **kwargs}
    return self.send_signed_request("POST", url_path, params)

  def close_order(self, merchantId: str, **kwargs):

    url_path = '/binancepay/openapi/order/close'
    params = {"merchantId": merchantId, **kwargs}
    return self.send_signed_request("POST", url_path, params)

  def transfer_fund(self, requestId: str, merchantId: str, currency: str, amount: float, transferType:str, **kwargs):

    url_path = '/binancepay/openapi/wallet/transfer'
    params = {
      "requestId": requestId,
      "merchantId": merchantId,
      "currency": currency,
      "amount": amount,
      "transferType": transferType,
      **kwargs
    }
    return self.send_signed_request("POST", url_path, params)

  def get_transfer_result(self, tranId: str, **kwargs):

    url_path = '/binancepay/openapi/wallet/transfer/query'
    params = {
      "tranId": tranId,
      **kwargs
    }
    return self.send_signed_request("POST", url_path, params)

  def create_sub_merchant(self, tranId: str, **kwargs):

    url_path = '/binancepay/openapi/wallet/transfer/query'
    params = {
      "tranId": tranId,
      **kwargs
    }
    return self.send_signed_request("POST", url_path, params)
