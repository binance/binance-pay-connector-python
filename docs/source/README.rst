.. role:: raw-html-m2r(raw)
   :format: html


Binance Pay Public API Connector Python
=======================================


.. image:: https://img.shields.io/badge/python-3.6+-blue.svg
   :target: https://www.python.org/downloads/release/python-360/
   :alt: Python 3.6


.. image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: License: MIT


This is a lightweight library that works as a connector to `Binance pay public API <https://developers.binance.com/docs/binance-pay/introduction>`_

Installation
------------

.. code-block:: bash

   pip install binance-pay-connector

Documentation
-------------

`https://binance-pay-connector.readthedocs.io <https://binance-connector.readthedocs.io>`_

RESTful APIs
------------

Usage examples:

.. code-block:: python

   from binance.pay.merchant import Merchant as Client


   # Setup merchant API from https://merchant.binance.com/en/dashboard/developers

   client = Client(key='<api_key>', secret='<api_secret>')
   response = client.get_order(merchantTradeNo="<trade_no>")

   # Get an order details
   print(response)

Please find `examples <https://github.com/binance/binance-pay-connector-python/tree/master/examples/pay/merchant>`_ folder to check for more endpoints.

Optional parameters
^^^^^^^^^^^^^^^^^^^

PEP8 suggests *lowercase with words separated by underscores*\ , but for this connector,
the methods' optional parameters should follow their exact naming as in the API documentation.

.. code-block:: python

   # Recognised parameter name
   response = client.get_order(merchantTradeNo="2223")

   # Unrecognised parameter name
   response = client.get_order(merchant_trade_no="2223")

Display logs
^^^^^^^^^^^^

Setting the log level to ``DEBUG`` will log the request URL, payload and response text.

Error
^^^^^

If a request has a parameter that is not provided but required from server, this library will throw an exception ``binance.pay.error.ParameterRequiredError``\ , except the endpoint that is for creating order.  ``POST /binancepay/openapi/v2/order`` that used to create order has complicate parameter strucuture, the library doesn't any mandatory parameter. Please see the example file for how to place an order.

Test Case
---------

.. code-block:: python

   # In case packages are not installed yet
   pip install -r requirements-test.txt

   pytest

Contributing
------------

Contributions are welcome.\ :raw-html-m2r:`<br/>`
If you've found a bug within this project, please open an issue to discuss what you would like to change.\ :raw-html-m2r:`<br/>`
If it's an issue with the API, please open a topic at `Binance Developer Community <https://dev.binance.vision>`_
