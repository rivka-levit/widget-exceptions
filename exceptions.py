from http import HTTPStatus


class WidgetException(Exception):
    """Base class for exceptions in this module."""


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


class PricingException(CheckoutException):
    """Pricing exceptions."""


class InvalidCouponCodeError(PricingException):
    """Indicates that the coupon code is invalid."""


class NoStackCouponError(PricingException):
    """Can not stack coupon exception."""
