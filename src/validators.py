"""
Reusable validation functions for the Task 14
Business Data Validation Framework.

This module contains independent validation rules.
Each function returns:
    True  -> validation passed
    False -> validation failed
"""

import re
from datetime import datetime, date


# ============================================================
# REGULAR EXPRESSION PATTERNS
# ============================================================

EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

PHONE_PATTERN = r"^[6-9]\d{9}$"

CUSTOMER_ID_PATTERN = r"^CUS\d{4}$"

ORDER_ID_PATTERN = r"^ORD\d{5}$"

PINCODE_PATTERN = r"^\d{6}$"


# ============================================================
# 1. REQUIRED FIELD VALIDATION
# ============================================================

def validate_required(value):
    """
    Check whether a value is present and not empty.
    """
    if value is None:
        return False

    return bool(str(value).strip())


# ============================================================
# 2. EMAIL VALIDATION
# ============================================================

def validate_email(email):
    """
    Validate an email address using regular expressions.
    """
    if not validate_required(email):
        return False

    return bool(re.fullmatch(EMAIL_PATTERN, str(email).strip()))


# ============================================================
# 3. PHONE NUMBER VALIDATION
# ============================================================

def validate_phone(phone):
    """
    Validate a 10-digit Indian mobile number.
    """
    if not validate_required(phone):
        return False

    return bool(re.fullmatch(PHONE_PATTERN, str(phone).strip()))


# ============================================================
# 4. CUSTOMER ID VALIDATION
# ============================================================

def validate_customer_id(customer_id):
    """
    Validate customer ID format.

    Expected format:
    CUS followed by exactly 4 digits.

    Example:
    CUS1001
    """
    if not validate_required(customer_id):
        return False

    return bool(
        re.fullmatch(CUSTOMER_ID_PATTERN, str(customer_id).strip())
    )


# ============================================================
# 5. ORDER ID VALIDATION
# ============================================================

def validate_order_id(order_id):
    """
    Validate order ID format.

    Expected format:
    ORD followed by exactly 5 digits.

    Example:
    ORD10001
    """
    if not validate_required(order_id):
        return False

    return bool(
        re.fullmatch(ORDER_ID_PATTERN, str(order_id).strip())
    )


# ============================================================
# 6. DATE FORMAT VALIDATION
# ============================================================

def validate_date(date_value):
    """
    Validate date using YYYY-MM-DD format.
    """
    if not validate_required(date_value):
        return False

    try:
        datetime.strptime(str(date_value).strip(), "%Y-%m-%d")
        return True
    except ValueError:
        return False


# ============================================================
# 7. FUTURE DATE VALIDATION
# ============================================================

def validate_not_future_date(date_value):
    """
    Check that the date is not later than today's date.
    """
    if not validate_date(date_value):
        return False

    try:
        parsed_date = datetime.strptime(
            str(date_value).strip(),
            "%Y-%m-%d"
        ).date()

        return parsed_date <= date.today()

    except ValueError:
        return False


# ============================================================
# 8. PRODUCT NAME VALIDATION
# ============================================================

def validate_product(product):
    """
    Validate that the product name is present
    and contains meaningful text.
    """
    if not validate_required(product):
        return False

    product_text = str(product).strip()

    return bool(re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9\s\-]{1,49}", product_text))


# ============================================================
# 9. PRICE VALIDATION
# ============================================================

def validate_price(price):
    """
    Validate that price is numeric and greater than zero.
    """
    try:
        value = float(price)
        return value > 0
    except (ValueError, TypeError):
        return False


# ============================================================
# 10. QUANTITY VALIDATION
# ============================================================

def validate_quantity(quantity):
    """
    Validate that quantity is a positive integer.
    """
    try:
        value = int(quantity)
        return value > 0
    except (ValueError, TypeError):
        return False


# ============================================================
# 11. PIN CODE VALIDATION
# ============================================================

def validate_pincode(pincode):
    """
    Validate a six-digit Indian PIN code.
    """
    if not validate_required(pincode):
        return False

    return bool(
        re.fullmatch(PINCODE_PATTERN, str(pincode).strip())
    )


# ============================================================
# 12. ORDER STATUS VALIDATION
# ============================================================

VALID_STATUSES = {
    "Pending",
    "Shipped",
    "Delivered",
    "Cancelled"
}


def validate_status(status):
    """
    Validate order status against the allowed values.
    """
    if not validate_required(status):
        return False

    return str(status).strip() in VALID_STATUSES