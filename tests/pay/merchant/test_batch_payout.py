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
    responses.POST, "/binancepay/openapi/payout/transfer", mock_response, 200
)
def test_batch_payout():
    """Tests the API endpoint to batch payout"""

    params = {
        "requestId": random_str(),
        "batchName": random_str(),
        "currency": random_str(),
        "totalAmount": random_int(),
        "totalNumber": random_int(),
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }
    client = Client(key, secret)
    response = client.batch_payout(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_batch_payout_without_requestId():
    """Tests the API endpoint to batch payout without requestId"""

    params = {
        "requestId": "",
        "batchName": random_str(),
        "currency": random_str(),
        "totalAmount": random_int(),
        "totalNumber": random_int(),
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)


def test_batch_payout_without_batchName():
    """Tests the API endpoint to batch payout without batchName"""

    params = {
        "requestId": random_str(),
        "batchName": "",
        "currency": random_str(),
        "totalAmount": random_int(),
        "totalNumber": random_int(),
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)


def test_batch_payout_without_currency():
    """Tests the API endpoint to batch payout without currency"""

    params = {
        "requestId": random_str(),
        "batchName": random_str(),
        "currency": "",
        "totalAmount": random_int(),
        "totalNumber": random_int(),
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)


def test_batch_payout_without_totalAmount():
    """Tests the API endpoint to batch payout without totalAmount"""

    params = {
        "requestId": random_str(),
        "batchName": random_str(),
        "currency": random_str(),
        "totalAmount": "",
        "totalNumber": random_int(),
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)


def test_batch_payout_without_totalNumber():
    """Tests the API endpoint to batch payout without totalNumber"""

    params = {
        "requestId": random_str(),
        "batchName": random_str(),
        "currency": random_str(),
        "totalAmount": random_int(),
        "totalNumber": "",
        "transferDetailList": {
            "merchantSendId": random_str(),
            "receiveType": "PAY_ID",
            "receiver": random_str(),
            "transferAmount": random_int(),
            "transferMethod": "FUNDING_WALLET",
        },
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)


def test_batch_payout_without_transferDetailList():
    """Tests the API endpoint to batch payout without transferDetailList"""

    params = {
        "requestId": random_str(),
        "batchName": random_str(),
        "currency": random_str(),
        "totalAmount": random_int(),
        "totalNumber": random_int(),
        "transferDetailList": "",
    }

    client = Client(key, secret)
    client.batch_payout.when.called_with(**params).should.throw(ParameterRequiredError)
