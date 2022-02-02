import responses 
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()


mock_error_response = {
    "status": "FAIL",
    "code": "400100",
    "errorMessage": "A mandatory parameter was not sent, was empty/null, or malformed."
}


@mock_http_response(responses.POST, "/binancepay/openapi/wallet/transfer", mock_response, 200)
def test_transfer_fund():
    """Tests the API endpoint to transfer funds"""

    params = { 
        "requestId": random_str(),
        "currency": "BUSD",
        "amount": str(random_int()),
        "transferType": "TO_MAIN",
    }
    client = Client(key, secret)
    response = client.transfer_fund(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_transfer_fund_without_requestId():
    """Tests the API endpoint to transfer funds without requestId"""

    params = { 
        "requestId": "",
        "currency": "BUSD",
        "amount": str(random_int()),
        "transferType": "TO_MAIN",
    }
    client = Client(key, secret)
    client.transfer_fund.when.called_with(**params).should.throw(ParameterRequiredError)


def test_transfer_fund_without_currency():
    """Tests the API endpoint to transfer funds without currency"""

    params = { 
        "requestId": random_str(),
        "currency": "",
        "amount": str(random_int()),
        "transferType": "TO_MAIN",
    }
    client = Client(key, secret)
    client.transfer_fund.when.called_with(**params).should.throw(ParameterRequiredError)


def test_transfer_fund_without_amount():
    """Tests the API endpoint to transfer funds without amount"""

    params = { 
        "requestId": random_str(),
        "currency": "BUSD",
        "amount": "",
        "transferType": "TO_MAIN",
    }
    client = Client(key, secret)
    client.transfer_fund.when.called_with(**params).should.throw(ParameterRequiredError)


def test_transfer_fund_without_transferType():
    """Tests the API endpoint to transfer funds without transferType"""

    params = { 
        "requestId": random_str(),
        "currency": "BUSD",
        "amount": str(random_int()),
        "transferType": "",
    }
    client = Client(key, secret)
    client.transfer_fund.when.called_with(**params).should.throw(ParameterRequiredError)
