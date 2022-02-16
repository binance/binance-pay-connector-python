import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


@mock_http_response(
    responses.POST, "/binancepay/openapi/submerchant/add", mock_response, 200
)
def test_new_sub_merchant():
    """Tests the API endpoint to create new sub merchant"""

    params = {
        "merchantName": random_str(),
        "merchantType": 1,
        "merchantMcc": random_str(),
        "country": "GO",
    }
    client = Client(key, secret)
    response = client.new_sub_merchant(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_new_sub_merchant_without_merchantName():
    """Tests the API endpoint to create new sub merchant without merchantName"""

    params = {
        "merchantName": "",
        "merchantType": 1,
        "merchantMcc": random_str(),
        "country": "GO",
    }
    client = Client(key, secret)
    client.new_sub_merchant.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_new_sub_merchant_without_merchantType():
    """Tests the API endpoint to create new sub merchant without merchantType"""

    params = {
        "merchantName": random_str(),
        "merchantType": "",
        "merchantMcc": random_str(),
        "country": "GO",
    }
    client = Client(key, secret)
    client.new_sub_merchant.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_new_sub_merchant_without_merchantMcc():
    """Tests the API endpoint to create new sub merchant without merchantMcc"""

    params = {
        "merchantName": random_str(),
        "merchantType": 1,
        "merchantMcc": "",
        "country": "GO",
    }
    client = Client(key, secret)
    client.new_sub_merchant.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_new_sub_merchant_without_country():
    """Tests the API endpoint to create new sub merchant without country"""

    params = {
        "merchantName": random_str(),
        "merchantType": 1,
        "merchantMcc": random_str(),
        "country": "",
    }
    client = Client(key, secret)
    client.new_sub_merchant.when.called_with(**params).should.throw(
        ParameterRequiredError
    )
