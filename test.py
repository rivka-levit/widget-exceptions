"""
Tests for exceptions.
Command to run all the tests: python -m unittest -v
"""

import traceback

from io import StringIO
from contextlib import redirect_stdout
from sys import exception

from unittest import TestCase
from exceptions import (WidgetException,
                        SupplierException,
                        NotManufacturedError,
                        ProductionDelayedError,
                        ShippingDelayedError,
                        CheckoutException,
                        InventoryException,
                        OutOfStockError,
                        PricingException,
                        InvalidCouponCodeError,
                        NoStackCouponError)


class TestWidgetExceptions(TestCase):
    """Test for WidgetException class and the children."""

    def setUp(self):
        def check_log_console(exc: type) -> None:
            with (redirect_stdout(StringIO()) as logged_out):
                try:
                    raise exc()
                except exc as e:
                    tb = ''.join(traceback.format_exception(e))
                    e.log_console()
                    output = logged_out.getvalue()

                    self.assertIn(e.__class__.__name__, output)
                    self.assertIn(str(e.http_status), output)
                    self.assertIn(e.internal_error_msg, output)
                    self.assertIn(tb, output)

        self.check_log_console = check_log_console
        self.exceptions = [
            WidgetException,
            SupplierException,
            NotManufacturedError,
            ProductionDelayedError,
            ShippingDelayedError,
            CheckoutException,
            InventoryException,
            OutOfStockError,
            PricingException,
            InvalidCouponCodeError,
            NoStackCouponError
        ]

    def test_to_json_valid_json_object(self):
        """Test to_json method return a valid json object."""

        with self.assertRaises(WidgetException) as e:
            raise WidgetException()

        returned_value = e.exception.to_json()

        self.assertIsInstance(returned_value, str)
        self.assertIn('status', returned_value)
        self.assertIn('message', returned_value)

    def test_log_console_output_to_console(self):
        """Test output is realised to the console for base class."""

        self.check_log_console(WidgetException)

    def test_log_console_subclasses(self):
        """Test log_console works correctly with subclasses."""

        for ex in self.exceptions:
            self.check_log_console(ex)
