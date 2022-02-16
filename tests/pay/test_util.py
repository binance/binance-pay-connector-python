from binance.pay.error import ParameterRequiredError

from binance.pay.lib.utils import check_required_parameter, check_required_parameters


def test_pass_check_required_parameter():
    check_required_parameter.when.called_with("btcusdt", "symbol").should_not.throw(
        ParameterRequiredError
    )


def test_failed_when_required_parameter_is_none():
    check_required_parameter.when.called_with(None, "symbol").should.throw(
        ParameterRequiredError
    )


def test_failed_when_required_parameter_is_empty():
    check_required_parameter.when.called_with("", "symbol").should.throw(
        ParameterRequiredError
    )


def test_pass_check_required_parameters():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameter_value_0():
    check_required_parameters.when.called_with(
        [[0, "transactionType"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameter_value_1():
    check_required_parameters.when.called_with(
        [[1, "transactionType"]]
    ).should_not.throw(ParameterRequiredError)


def test_pass_check_required_parameters_multi_params():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"], [10, "price"]]
    ).should_not.throw(ParameterRequiredError)


def test_fail_check_required_parameters_single_param():
    check_required_parameters.when.called_with([["", "symbol"]]).should.throw(
        ParameterRequiredError
    )
    check_required_parameters.when.called_with([[None, "symbol"]]).should.throw(
        ParameterRequiredError
    )


def test_fail_check_required_parameters_multi_params():
    check_required_parameters.when.called_with(
        [["btcusdt", "symbol"], [None, "price"]]
    ).should.throw(ParameterRequiredError)
    check_required_parameters.when.called_with(
        [["", "symbol"], [10, "price"]]
    ).should.throw(ParameterRequiredError)
