"""
Validation engine for the Task 14
Business Data Validation Framework.

This module:
1. Reads customer order records from CSV
2. Applies all validation rules
3. Detects duplicate order IDs
4. Returns structured validation results
"""

import csv

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


def validate_record(record, duplicate_order_ids=None):
    """Validate a single customer order record."""

    if duplicate_order_ids is None:
        duplicate_order_ids = set()

    errors = []

    required_fields = [
        "order_id",
        "customer_id",
        "customer_name",
        "email",
        "phone",
        "order_date",
        "product",
        "price",
        "quantity",
        "pincode",
        "status",
    ]

    # Required fields
    for field in required_fields:
        if not validate_required(record.get(field)):
            errors.append(f"{field}: required field is missing")

    # Order ID
    if validate_required(record.get("order_id")):
        if not validate_order_id(record["order_id"]):
            errors.append("order_id: invalid format")

        if record["order_id"] in duplicate_order_ids:
            errors.append("order_id: duplicate order ID")

    # Customer ID
    if validate_required(record.get("customer_id")):
        if not validate_customer_id(record["customer_id"]):
            errors.append("customer_id: invalid format")

    # Email
    if validate_required(record.get("email")):
        if not validate_email(record["email"]):
            errors.append("email: invalid email address")

    # Phone
    if validate_required(record.get("phone")):
        if not validate_phone(record["phone"]):
            errors.append("phone: invalid phone number")

    # Date
    if validate_required(record.get("order_date")):

        if not validate_date(record["order_date"]):
            errors.append("order_date: invalid date format")

        elif not validate_not_future_date(record["order_date"]):
            errors.append("order_date: future date is not allowed")

    # Product
    if validate_required(record.get("product")):
        if not validate_product(record["product"]):
            errors.append("product: invalid product name")

    # Price
    if validate_required(record.get("price")):
        if not validate_price(record["price"]):
            errors.append("price: must be greater than zero")

    # Quantity
    if validate_required(record.get("quantity")):
        if not validate_quantity(record["quantity"]):
            errors.append("quantity: must be a positive integer")

    # PIN
    if validate_required(record.get("pincode")):
        if not validate_pincode(record["pincode"]):
            errors.append("pincode: must contain exactly 6 digits")

    # Status
    if validate_required(record.get("status")):
        if not validate_status(record["status"]):
            errors.append("status: invalid order status")

    return {
        "order_id": record.get("order_id", ""),
        "is_valid": len(errors) == 0,
        "errors": errors,
    }


def validate_dataset(records):
    """Validate all records and detect duplicate order IDs."""

    order_id_counts = {}

    for record in records:
        order_id = record.get("order_id", "").strip()

        if order_id:
            order_id_counts[order_id] = (
                order_id_counts.get(order_id, 0) + 1
            )

    duplicate_order_ids = {
        order_id
        for order_id, count in order_id_counts.items()
        if count > 1
    }

    results = []

    for record in records:
        result = validate_record(
            record,
            duplicate_order_ids
        )

        results.append(result)

    return results


def load_csv(file_path):
    """Load CSV data as a list of dictionaries."""

    with open(
        file_path,
        mode="r",
        encoding="utf-8",
        newline=""
    ) as file:

        reader = csv.DictReader(file)

        return list(reader)


def validate_csv(file_path):
    """Load and validate a CSV dataset."""

    records = load_csv(file_path)

    return validate_dataset(records)