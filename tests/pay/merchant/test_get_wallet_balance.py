import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
params = {"wallet": "FUNDING_WALLET", "currency": "BUSD"}


@mock_http_response(responses.POST, "/binancepay/openapi/balance", mock_response, 200)
def test_get_wallet_balance():
    """Tests the API endpoint to get wallet balance"""

    client = Client(key, secret)
    response = client.get_wallet_balance(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_get_wallet_balance_without_wallet():
    """Tests the API endpoint to get wallet balance without wallet"""

    params = {"wallet": "", "currency": "BUSD"}

    client = Client(key, secret)
    client.get_wallet_balance.when.called_with(**params).should.throw(
        ParameterRequiredError
    )


def test_get_wallet_balance_without_currency():
    """Tests the API endpoint to get wallet balance without currency"""

    params = {"wallet": "FUNDING_WALLET", "currency": ""}

    client = Client(key, secret)
    client.get_wallet_balance.when.called_with(**params).should.throw(
        ParameterRequiredError
    )
