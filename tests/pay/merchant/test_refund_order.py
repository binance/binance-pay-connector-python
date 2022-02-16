import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(
    responses.POST, "/binancepay/openapi/order/refund", mock_response, 200
)
def test_refund_order():
    """Tests the API endpoint to refund order"""

    params = {
        "refundRequestId": random_str(),
        "prepayId": random_str(),
        "refundAmount": random_int(),
        "refundReason": random_str(),
    }
    client = Client(key, secret)
    response = client.refund_order(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_refund_order_without_refundRequestId():
    """Tests the API endpoint to refund order without refundRequestId"""

    params = {
        "refundRequestId": "",
        "prepayId": random_str(),
        "refundAmount": random_int(),
        "refundReason": random_str(),
    }
    client = Client(key, secret)
    client.refund_order.when.called_with(**params).should.throw(ParameterRequiredError)


def test_refund_order_without_prepayId():
    """Tests the API endpoint to refund order without prepayId"""

    params = {
        "refundRequestId": random_str(),
        "prepayId": "",
        "refundAmount": random_int(),
        "refundReason": random_str(),
    }
    client = Client(key, secret)
    client.refund_order.when.called_with(**params).should.throw(ParameterRequiredError)


def test_refund_order_without_refundAmount():
    """Tests the API endpoint to refund order without refundAmount"""

    params = {
        "refundRequestId": random_str(),
        "prepayId": random_str(),
        "refundAmount": "",
        "refundReason": random_str(),
    }
    client = Client(key, secret)
    client.refund_order.when.called_with(**params).should.throw(ParameterRequiredError)
