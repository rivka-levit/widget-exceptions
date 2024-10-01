from http import HTTPStatus


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

        if user_err_msg:
            self.user_error_msg = user_err_msg


class SupplierException(WidgetException):
    """Exceptions occurred on the supplier's end."""


class NotManufacturedError(SupplierException):
    """Exception raised when a product is not manufactured anymore."""


class ProductionDelayedError(SupplierException):
    """Exception raised when production is delayed."""


class ShippingDelayedError(SupplierException):
    """Exception raised when shipping is delayed."""


class CheckoutException(WidgetException):
    """Indicates errors during the checkout process."""


class InventoryException(CheckoutException):
    """Inventory type exceptions."""


class OutOfStockError(InventoryException):
    """Indicates that an item is out of stock."""

    internal_error_msg = 'Item is out of stock.'
    user_error_msg = 'This item is out of stock.'

class PricingException(CheckoutException):
    """Pricing exceptions."""


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
