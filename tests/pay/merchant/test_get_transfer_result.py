import responses
import json
from binance.pay.merchant import Merchant as Client
from tests.util import mock_http_response
from tests.util import random_str, random_int
from binance.pay.error import ParameterRequiredError

mock_response = {"key_1": "value_1", "key_2": "value_2"}
key = random_str()
secret = random_str()
params = {"tranId": str(random_int())}


@mock_http_response(
    responses.POST, "/binancepay/openapi/wallet/transfer/query", mock_response, 200
)
def test_get_transfer_result():
    """Tests the API endpoint to get transfer result"""

    client = Client(key, secret)
    response = client.get_transfer_result(**params)
    request_body = json.loads(responses.calls[0].request.body)
    request_body.should.equal(params)
    response.should.equal(mock_response)


def test_get_transfer_result_without_tranId():
    """Tests the API endpoint to get transfer result without tranId"""

    client = Client(key, secret)
    client.get_transfer_result.when.called_with("").should.throw(ParameterRequiredError)
