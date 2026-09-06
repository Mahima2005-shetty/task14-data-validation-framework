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


print("DATA VALIDATION FRAMEWORK - BASIC TEST")
print("=" * 45)

print("Required field:", validate_required("Mahima"))
print("Valid email:", validate_email("mahima@gmail.com"))
print("Invalid email:", validate_email("mahima.gmail.com"))

print("Valid phone:", validate_phone("9876543210"))
print("Invalid phone:", validate_phone("12345"))

print("Valid customer ID:", validate_customer_id("CUS1001"))
print("Invalid customer ID:", validate_customer_id("CUSTOMER1"))

print("Valid order ID:", validate_order_id("ORD10001"))
print("Invalid order ID:", validate_order_id("ORDER1"))

print("Valid date:", validate_date("2026-09-05"))
print("Invalid date:", validate_date("2026/09/05"))

print("Past date:", validate_not_future_date("2026-09-01"))
print("Future date:", validate_not_future_date("2026-09-08"))

print("Valid product:", validate_product("Laptop"))
print("Empty product:", validate_product(""))

print("Valid price:", validate_price("55000"))
print("Invalid price:", validate_price("-500"))

print("Valid quantity:", validate_quantity("2"))
print("Invalid quantity:", validate_quantity("0"))

print("Valid PIN:", validate_pincode("560001"))
print("Invalid PIN:", validate_pincode("56004"))

print("Valid status:", validate_status("Delivered"))
print("Invalid status:", validate_status("Unknown"))