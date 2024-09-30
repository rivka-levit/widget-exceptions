# Exception Class Hierarchy - Practice Project
### Overview
This repository contains a practice project that was developed during 
an Object-Oriented Programming (OOP) course. The project focuses on creating 
a hierarchy of exception classes for a hypothetical application. The aim of 
the project is to practice the principles of exception handling, inheritance, 
and custom exception creation in an OOP context.

### Features
- <b>Custom Exception Classes:</b> A set of custom exceptions tailored to 
specific error scenarios in a hypothetical application.
- <b>Exception Hierarchy:</b> Exception classes are organized in a clear and 
logical hierarchy, demonstrating inheritance and specialization.
- <b>WidgetException:</b> A root exception class from which all other custom 
exceptions inherit, ensuring that the exception handling in the application 
can be centralized and easily managed.
- <b>Specialized Exceptions:</b> Derived exception classes that cover specific 
error types, demonstrating how exceptions can be extended and customized for 
various use cases.

### Exception Hierarchy

- WidgetException
  - SupplierException
    - NotManufacturedError
    - ProductionDelayedError
    - ShippingDelayedError
  - CheckoutException
    - InventoryException
      - OutOfStockError
    - PricingException
      - InvalidCouponCodeError
      - NoStackCouponError
      
This structure makes it easy to handle errors at different levels of 
specificity, allowing the program to gracefully recover from or report various 
errors as needed.
