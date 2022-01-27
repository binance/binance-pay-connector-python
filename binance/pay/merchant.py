from binance.pay.api import API

class Merchant(API):
  def __init__(self, key=None, secret=None, **kwargs):
    if "base_url" not in kwargs:
      kwargs["base_url"] = "https://bpay.binanceapi.com"
    super().__init__(key, secret, **kwargs)

  def new_order(self, params):
    """ Create Order

    POST /binancepay/openapi/v2/order

    Create order API Version 2 used for merchant/partner to initiate acquiring order.
    https://developers.binance.com/docs/binance-pay/api-order-create-v2
  
    Keyword Args:
      merchant
        subMerchantId (string, optional)
      env
        terminalType (string)
        osType (string, optional)
        orderClientIp (string, optional)
        cookieId (string, optional)
      merchantTradeNo (string)
      orderAmount (float)
      currency (string)
      goods
        goodsType (string)
        goodsCategory (string)
        referenceGoodsId (string)
        goodsName (string)
        goodsDetail (string)
        goodsUnitAmount
          currency (string)
          amount (float)
        goodsQuantity (string, optional)
      shipping 
        shippingName
          firstName (string)
          middleName (string, optional)
          lastName (string)
        shippingAddress
          region (string)
          state (string, optional)
          city (string, optional)
          address (string, optional)
          zipCode (string, optional)
          shippingAddressType (string, optional)
        shippingPhoneNo (string, optional)
      buyer
        referenceBuyerId (string, optional)
        buyerName
          firstName (string)
          middleName (string, optional)
          lastName (string)
        buyerPhoneCountryCode (string, optional)
        buyerPhoneNo (string, optional)
        buyerEmail (string, optional)
        buyerRegistrationTime (string, optional)
        buyerBrowserLanguage (string, optional)
      returnUrl (string, optional)
      cancelUrl (string, optional)
      orderExpireTime (integer, optional)
      supportPayCurrency (string, optional)
      appId (string, optional)
    """
    return self.send_signed_request("POST", '/binancepay/openapi/v2/order', params)
    
  def get_order(self, **kwargs):
    """Query Order

    Query order API used for merchant/partner to query order status

    GET /binancepay/openapi/v2/order/query

    https://developers.binance.com/docs/binance-pay/api-order-query-v2

    Keyword Args:
      prepayId (string, optional)
      merchantTradeNo (string, optional)
    """
    return self.send_signed_request("POST", '/binancepay/openapi/v2/order/query', kwargs)

  def cancel_order(self, **kwargs):
    """Close Order

    Close order API used for merchant/partner to close order without any prior payment activities triggered by user. The successful close result will be notified asynchronously through Order Notification Webhook with bizStatus = "PAY_CLOSED"

    POST /binancepay/openapi/order/close

    https://developers.binance.com/docs/binance-pay/api-order-close

    Keyword Args:
      prepayId (string, optional)
      merchantTradeNo (string, optional)
    """

    return self.send_signed_request("POST", '/binancepay/openapi/order/close', kwargs)

  def transfer_fund(self, requestId: str, currency: str, amount: str, transferType: str, **kwargs):

    """Transfer Fund

    Fund transfer API used for merchant/partner to initiate Fund transfer between wallets.

    POST /binancepay/openapi/wallet/transfer

    https://developers.binance.com/docs/binance-pay/api-wallet-transfer

    Args:
      requestId (str)
      currency (str)
      amount (str)
      transferType (str) : Only "TO_MAIN" OR "TO_PAY"
    """

    params = {
      "requestId": requestId,
      "currency": currency,
      "amount": amount,
      "transferType": transferType,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/wallet/transfer', params)

  def get_transfer_result(self, tranId: str, **kwargs):
    """Query Transfer Result

    Query Transfer Result API used for merchant/partner to query transfer result.

    POST /binancepay/openapi/wallet/transfer/query

    https://developers.binance.com/docs/binance-pay/api-wallet-transfer-query

    Args:
      tranId (str) : the value of requestId of provoking Transfer Fund API
    """

    params = {
      "tranId": tranId,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/wallet/transfer/query', params)

  def new_sub_merchant(self, merchantName: str,  merchantType: int, merchantMcc: str, country: str, **kwargs):
    """Create SubMerchant

    Create Sub-merchant API used for merchant/partner.

    POST /binancepay/openapi/submerchant/add

    https://developers.binance.com/docs/binance-pay/api-submerchant-add

    Args:
      merchantName (string)
      merchantType (integer) : 1=Personal(Individual)、2=solo proprietor、 3=Partnership、4=Private company、5=Others company
      merchantMcc (string) : MCC Code, get from Binance
      country (string)
    Keyword Args:
      brandLogo (string, optional)
      address (string, optional)
      companyName (string, optional)
      registrationNumber (string, optional)
      registrationCountry (string, optional)
      registrationAddress (string, optional)
      incorporationDate (integer, optional)
      storeType (integer, optional)
      siteType (integer, optional)
      siteUrl (string, optional)
      siteName (string, optional)
      certificateType (integer, optional) : 1=ID 2=Passport, Required if merchantType is Individual
      certificateCountry (string, optional)
      certificateNumber (string, optional)
      certificateValidDate (integer, optional)
      contractTimeIsv (integer, optional)
    """

    params = {
      "merchantName": merchantName,
      "merchantType": merchantType,
      "merchantMcc": merchantMcc,
      "country": country,
      **kwargs
    }

    return self.send_signed_request("POST", '/binancepay/openapi/submerchant/add', params)

  def refund_order(self, refundRequestId: str, prepayId: str, refundAmount: float,  **kwargs):
    """Refund Order

    Refund order API used for Marchant/Partner to refund for a successful payment.

    POST /binancepay/openapi/order/refund

    https://developers.binance.com/docs/binance-pay/api-order-refund

    Args:
      refundRequestId (str)
      prepayId (str)
      refundAmount (float)
    Keyword Args:
      refundReason (string, optional)
    """

    params = {
      "refundRequestId": refundRequestId,
      "prepayId": prepayId,
      "refundAmount": refundAmount,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/order/refund', params)


  def get_refund_order(self, refundRequestId: str, **kwargs):
    """Query Refund Order

    Refund order API used for Marchant/Partner to refund for a successful payment.

    POST /binancepay/openapi/order/refund/query

    https://developers.binance.com/docs/binance-pay/api-order-refund

    Args:
      refundRequestId (str): The unique ID assigned by the merchant to identify a refund request.
    """

    params = {
      "refundRequestId": refundRequestId,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/order/refund/query', params)


  def batch_payout(self, params):
    """Batch Payout

    Payout API used for Merchant/Partner to make transfers in batch.

    POST /binancepay/openapi/payout/transfer

    https://developers.binance.com/docs/binance-pay/api-payout

    Args:
      requestId (str): The unique ID assigned by the merchant to identify a payout request.
      bizScene (str, optional)
      batchName (str)
      currency (str): Crypto token only, fiat NOT supported. All characters must be in uppercase
      totalAmount (float)
      totalNumber (integer)
      transferDetailList
        merchantSendId (str)
        receiveType (str)
        receiver (str)
        transferAmount (float)
        transferMethod (str) : FUNDING_WALLET, SPOT_WALLET
        remark (str)
    """
    return self.send_signed_request("POST", '/binancepay/openapi/payout/transfer', params)

  def get_wallet_balance(self, wallet: str, currency: str, **kwargs):
    """Wallet Balance Query

    query wallet balance.

    POST /binancepay/openapi/balance

    https://developers.binance.com/docs/binance-pay/api-balance-query

    Args:
      wallet (str): FUNDING_WALLET, SPOT_WALLET
      currency (str): Currency to query, e.g, "BUSD"
    """

    params = {
      "wallet": wallet,
      "currency": currency,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/balance', params)


  def get_payout(self, requestId: str, **kwargs):
    """Payout Query

    Payout query API used for Merchant/Partner to query transfer status.

    POST /binancepay/openapi/payout/query

    https://developers.binance.com/docs/binance-pay/api-payout-query

    Args:
      requestId (str): The unique ID assigned by the merchant to identify a payout request.
    Keyword Args:
      detailStatus (str)
    """

    params = {
      "requestId": requestId,
      **kwargs
    }
    return self.send_signed_request("POST", '/binancepay/openapi/payout/query', params)
