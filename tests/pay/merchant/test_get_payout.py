import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
params = {"requestId": random_str()}


@mock_http_response(
    responses.POST, "/binancepay/openapi/payout/query", mock_response, 200
)
def test_get_payout():
    """Tests the API endpoint to get payout"""

    client = Client(key, secret)
    response = client.get_payout(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_get_payout_without_requestId():
    """Tests the API endpoint to get payout without requestId"""

    client = Client(key, secret)
    client.get_payout.when.called_with("").should.throw(ParameterRequiredError)
