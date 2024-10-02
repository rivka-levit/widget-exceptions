from http import HTTPStatus
from datetime import datetime, timezone

import json


class WidgetException(Exception):
    """Base class for exceptions in this module."""

    http_status = HTTPStatus.INTERNAL_SERVER_ERROR
    internal_error_msg = 'Generic internal server error.'
    user_error_msg = 'We are sorry, but something went wrong on our end.'

    def __init__(self, *args, user_err_msg: str = None) -> None:
        if args:
            self.internal_error_msg = args[0]
            super().__init__(*args)
        else:
            super().__init__(self.internal_error_msg)

        if user_err_msg is not None:
            self.user_error_msg = user_err_msg

    def to_json(self):
        data = {
            'status': self.http_status,
            'message': self.user_error_msg
        }
        return json.dumps(data)

    def log_console(self):
        exception = {
            'type': self.__class__.__name__,
            'status': self.http_status,
            'message': self.args[0] if self.args else self.internal_error_msg,
            'args': self.args[1:] if self.args else None,
        }
        print(
            f'EXCEPTION occurred at '
            f'{datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}:\n'
            f'{exception}'
        )


class SupplierException(WidgetException):
    """Exceptions occurred on the supplier's end."""

    internal_error_msg = "Somthing went wrong on supplier's end."


class NotManufacturedError(SupplierException):
    """Exception raised when a product is not manufactured anymore."""

    internal_error_msg = 'Product is not manufactured anymore.'
    user_error_msg = 'This product is not manufactured anymore.'


class ProductionDelayedError(SupplierException):
    """Exception raised when production is delayed."""

    internal_error_msg = 'Production is delayed.'
    user_error_msg = 'The production of this product is delayed.'


class ShippingDelayedError(SupplierException):
    """Exception raised when shipping is delayed."""

    internal_error_msg = 'Shipping is delayed.'
    user_error_msg = 'The shipping of this product is delayed.'

class CheckoutException(WidgetException):
    """Indicates errors during the checkout process."""

    internal_error_msg = 'Generic checkout exception.'
    user_error_msg = ('We are sorry, but something went wrong in '
                      'the checkout process.')


class InventoryException(CheckoutException):
    """Inventory type exceptions."""

    internal_error_msg = 'Generic inventory exception.'


class OutOfStockError(InventoryException):
    """Indicates that an item is out of stock."""

    internal_error_msg = 'Item is out of stock.'
    user_error_msg = 'This item is out of stock.'

class PricingException(CheckoutException):
    """Pricing exceptions."""

    internal_error_msg = 'Generic pricing exception.'


class InvalidCouponCodeError(PricingException):
    """Indicates that the coupon code is invalid."""

    http_status = HTTPStatus.BAD_REQUEST
    internal_error_msg = 'Coupon code is invalid.'
    user_error_msg = 'We are sorry, but this coupon code is invalid.'


class NoStackCouponError(PricingException):
    """Can not stack coupon exception."""

    http_status = HTTPStatus.BAD_REQUEST
    internal_error_msg = 'Cannot stack coupon.'
    user_error_msg = 'We are sorry, you cannot stack coupon.'
