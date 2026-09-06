"""
Automated tests for the
Task 14 - Business Data Validation Framework.

Test coverage:
- Required fields
- Email
- Phone
- Customer ID
- Order ID
- Date
- Future date
- Product
- Price
- Quantity
- PIN code
- Status
- Dataset validation
- Duplicate Order ID
"""

from src.validators import (
    validate_required,
    validate_email,
    validate_phone,
    validate_customer_id,
    validate_order_id,
    validate_date,
    validate_not_future_date,
    validate_product,
    validate_price,
    validate_quantity,
    validate_pincode,
    validate_status,
)

from src.validation_engine import (
    validate_record,
    validate_dataset,
)


# ============================================================
# REQUIRED FIELD TESTS
# ============================================================

def test_required_valid_value():
    assert validate_required("Mahima") is True


def test_required_empty_value():
    assert validate_required("") is False


def test_required_none_value():
    assert validate_required(None) is False


# ============================================================
# EMAIL TESTS
# ============================================================

def test_valid_email():
    assert validate_email("mahima@gmail.com") is True


def test_invalid_email_without_at():
    assert validate_email("mahima.gmail.com") is False


def test_invalid_email_without_domain():
    assert validate_email("mahima@") is False


# ============================================================
# PHONE TESTS
# ============================================================

def test_valid_phone():
    assert validate_phone("9876543210") is True


def test_invalid_phone_length():
    assert validate_phone("12345") is False


def test_invalid_phone_start():
    assert validate_phone("1234567890") is False


# ============================================================
# CUSTOMER ID TESTS
# ============================================================

def test_valid_customer_id():
    assert validate_customer_id("CUS1001") is True


def test_invalid_customer_id():
    assert validate_customer_id("CUSTOMER1") is False


# ============================================================
# ORDER ID TESTS
# ============================================================

def test_valid_order_id():
    assert validate_order_id("ORD10001") is True


def test_invalid_order_id():
    assert validate_order_id("ORDER1") is False


# ============================================================
# DATE TESTS
# ============================================================

def test_valid_date():
    assert validate_date("2026-09-05") is True


def test_invalid_date_format():
    assert validate_date("05-09-2026") is False


def test_invalid_date_value():
    assert validate_date("2026-99-99") is False


def test_future_date_rejected():
    assert validate_not_future_date("2999-01-01") is False


# ============================================================
# PRODUCT TESTS
# ============================================================

def test_valid_product():
    assert validate_product("Laptop") is True


def test_valid_product_with_space():
    assert validate_product("Wireless Mouse") is True


def test_empty_product():
    assert validate_product("") is False


# ============================================================
# PRICE TESTS
# ============================================================

def test_valid_price():
    assert validate_price("55000") is True


def test_zero_price():
    assert validate_price("0") is False


def test_negative_price():
    assert validate_price("-500") is False


def test_invalid_price_text():
    assert validate_price("abc") is False


# ============================================================
# QUANTITY TESTS
# ============================================================

def test_valid_quantity():
    assert validate_quantity("2") is True


def test_zero_quantity():
    assert validate_quantity("0") is False


def test_negative_quantity():
    assert validate_quantity("-2") is False


# ============================================================
# PIN CODE TESTS
# ============================================================

def test_valid_pincode():
    assert validate_pincode("560001") is True


def test_invalid_pincode_length():
    assert validate_pincode("56004") is False


def test_invalid_pincode_zero_start():
    assert validate_pincode("056001") is False


# ============================================================
# STATUS TESTS
# ============================================================

def test_valid_status():
    assert validate_status("Delivered") is True


def test_valid_pending_status():
    assert validate_status("Pending") is True


def test_invalid_status():
    assert validate_status("Unknown") is False


# ============================================================
# COMPLETE RECORD TEST
# ============================================================

def test_valid_complete_record():

    record = {
        "order_id": "ORD99999",
        "customer_id": "CUS9999",
        "customer_name": "Test User",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "order_date": "2026-09-01",
        "product": "Laptop",
        "price": "55000",
        "quantity": "1",
        "pincode": "560001",
        "status": "Delivered",
    }

    result = validate_record(record)

    assert result["is_valid"] is True
    assert result["errors"] == []


# ============================================================
# INVALID RECORD TEST
# ============================================================

def test_invalid_complete_record():

    record = {
        "order_id": "INVALID",
        "customer_id": "WRONG",
        "customer_name": "",
        "email": "invalid-email",
        "phone": "123",
        "order_date": "2999-01-01",
        "product": "",
        "price": "-500",
        "quantity": "0",
        "pincode": "123",
        "status": "Unknown",
    }

    result = validate_record(record)

    assert result["is_valid"] is False
    assert len(result["errors"]) > 0


# ============================================================
# DUPLICATE ORDER ID TEST
# ============================================================

def test_duplicate_order_id():

    records = [
        {
            "order_id": "ORD10001",
            "customer_id": "CUS1001",
            "customer_name": "User One",
            "email": "one@gmail.com",
            "phone": "9876543210",
            "order_date": "2026-09-01",
            "product": "Laptop",
            "price": "50000",
            "quantity": "1",
            "pincode": "560001",
            "status": "Delivered",
        },
        {
            "order_id": "ORD10001",
            "customer_id": "CUS1002",
            "customer_name": "User Two",
            "email": "two@gmail.com",
            "phone": "9876543211",
            "order_date": "2026-09-01",
            "product": "Mouse",
            "price": "800",
            "quantity": "1",
            "pincode": "560002",
            "status": "Pending",
        },
    ]

    results = validate_dataset(records)

    assert results[0]["is_valid"] is False
    assert results[1]["is_valid"] is False

    assert any(
        "duplicate order ID" in error
        for error in results[0]["errors"]
    )

    assert any(
        "duplicate order ID" in error
        for error in results[1]["errors"]
    )
    