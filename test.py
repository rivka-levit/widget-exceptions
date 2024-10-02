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
