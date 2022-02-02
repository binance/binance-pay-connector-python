import responses 
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
params = { "merchantTradeNo": str(random_int()) }


@mock_http_response(responses.POST, "/binancepay/openapi/order/close", mock_response, 200)
def test_cancel_order():
    """Tests the API endpoint to cancel order"""

    client = Client(key, secret)
    response = client.cancel_order(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)
