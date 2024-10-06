"""
Tests for exceptions.
Command to run all the tests: python -m unittest -v
"""

import sys

from io import StringIO
from contextlib import redirect_stdout
from sys import exception

from unittest import TestCase
from exceptions import WidgetException


class TestWidgetExceptions(TestCase):
    """Test for WidgetException class and the children."""

    def test_to_json_valid_json_object(self):
        """Test to_json method return a valid json object."""

        with self.assertRaises(WidgetException) as e:
            raise WidgetException()

        returned_value = e.exception.to_json()

        self.assertIsInstance(returned_value, str)
        self.assertIn('status', returned_value)
        self.assertIn('message', returned_value)

    def test_log_console_output_to_console(self):
        """Test output is realised to the console."""

        with redirect_stdout(StringIO()) as logged_out:
            try:
                raise WidgetException()
            except WidgetException as e:
                e.log_console()
                output = logged_out.getvalue()

                self.assertIn(e.__class__.__name__, output)
                self.assertIn(str(e.http_status), output)
                self.assertIn(e.internal_error_msg, output)
