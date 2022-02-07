import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
params = {"refundRequestId": random_str()}


@mock_http_response(
    responses.POST, "/binancepay/openapi/order/refund/query", mock_response, 200
)
def test_get_refund_order():
    """Tests the API endpoint to get refund order"""

    client = Client(key, secret)
    response = client.get_refund_order(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_get_refund_order_without_refundRequestId():
    """Tests the API endpoint to gget refund order without refundRequestId"""

    client = Client(key, secret)
    client.get_refund_order.when.called_with("").should.throw(ParameterRequiredError)
