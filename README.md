# Reusable Business Data Validation Framework

A Python-based data validation framework that validates customer order records using regular expressions, rule-based validation, automated testing, and report generation.

## 📌 Task 14 – Data Validation Framework

### Objective

Build a reusable Python validation framework capable of checking business data against multiple validation rules.

The framework:

- Reads customer order data from a CSV file
- Applies multiple validation rules
- Uses Regular Expressions for pattern-based validation
- Detects duplicate Order IDs
- Identifies invalid records and explains the errors
- Generates CSV and JSON validation reports
- Includes automated test cases using Pytest

---

## 🎯 Project Highlights

- ✅ 13 independent validation rules
- ✅ Custom dataset with valid and intentionally invalid records
- ✅ Regular Expression based validation
- ✅ Reusable validation functions
- ✅ Centralized validation engine
- ✅ Duplicate record detection
- ✅ Automated testing with Pytest
- ✅ Detailed CSV validation report
- ✅ JSON validation summary
- ✅ Modular project structure
- ✅ Command-line execution

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core implementation |
| Regular Expressions | Pattern-based validation |
| CSV | Input dataset and detailed report |
| JSON | Validation summary |
| Pytest | Automated testing |
| Git & GitHub | Version control |

---

## 📋 Validation Rules

The framework currently implements the following validation rules:

| # | Validation Rule | Description |
|---|-----------------|-------------|
| 1 | Required Field | Checks whether mandatory fields contain values |
| 2 | Email | Validates email address format |
| 3 | Phone | Validates 10-digit Indian mobile numbers |
| 4 | Customer ID | Validates CUS followed by 4 digits |
| 5 | Order ID | Validates ORD followed by 5 digits |
| 6 | Date Format | Validates YYYY-MM-DD date format |
| 7 | Future Date | Prevents order dates from being in the future |
| 8 | Product Name | Validates product names using a pattern |
| 9 | Price | Ensures price is greater than zero |
| 10 | Quantity | Ensures quantity is a positive integer |
| 11 | PIN Code | Validates a 6-digit Indian PIN code |
| 12 | Order Status | Allows only predefined order statuses |
| 13 | Duplicate Order ID | Detects repeated Order IDs |

---

## 🏗️ System Architecture

```text
                    customer_orders.csv
                           |
                           v
                  +-------------------+
                  | Validation Engine |
                  |                   |
                  | validation_engine |
                  |       .py         |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Validation Rules  |
                  |                   |
                  |  validators.py    |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Validation Results|
                  +---------+---------+
                            |
                 +----------+----------+
                 |                     |
                 v                     v
       +------------------+   +------------------+
       | CSV Report       |   | JSON Summary     |
       |                  |   |                  |
       | validation_      |   | validation_      |
       | report.csv       |   | summary.json     |
       +------------------+   +------------------+
📊 Dataset

The project uses a custom customer order dataset:

data/customer_orders.csv
Dataset Fields
order_id
customer_id
customer_name
email
phone
order_date
product
price
quantity
pincode
status

The dataset contains 20 customer order records.

It intentionally includes both valid and invalid records to demonstrate the effectiveness of the validation framework.

Examples of Invalid Data
Incorrect email addresses
Invalid phone numbers
Missing customer names
Negative prices
Zero quantities
Invalid order statuses
Duplicate Order IDs
Invalid PIN codes
Missing product names
Future order dates
🚀 Installation
1. Clone the Repository
git clone https://github.com/Mahima2005-shetty/task14-data-validation-framework.git
2. Navigate to the Project
cd task14-data-validation-framework
3. Install Dependencies
python -m pip install -r requirements.txt
▶️ Run the Validation Framework

Execute:

python run_validation.py

The program reads the dataset, validates every record, displays invalid records, and generates reports.

🧪 Run Automated Tests

The project includes a comprehensive automated test suite using Pytest.

Run:

python -m pytest -v
Test Result
36 passed in 0.37s

The tests cover:

Required fields
Email validation
Phone validation
Customer IDs
Order IDs
Date validation
Future dates
Product names
Prices
Quantities
PIN codes
Order statuses
Complete valid records
Invalid records
Duplicate Order IDs
📈 Validation Result

The current dataset produces the following validation summary:

Total records   : 20
Valid records   : 2
Invalid records : 18
Validation rate : 10.00%

The framework also displays the specific validation errors associated with each invalid record.

📄 Generated Reports
1. Detailed CSV Report
reports/validation_report.csv

The report contains:

Order ID
Validation Status
Error Count
Validation Errors

Example:

ORD10003 | INVALID | 1 | email: invalid email address
2. JSON Summary
reports/validation_summary.json

Example:

{
    "project": "Business Data Validation Framework",
    "total_records": 20,
    "valid_records": 2,
    "invalid_records": 18,
    "validation_rate": 10.0
}
🔍 Regular Expression Validation

Regular expressions are used to validate structured fields.

Email
EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
Phone
PHONE_PATTERN = r"^[6-9]\d{9}$"
Customer ID
CUSTOMER_ID_PATTERN = r"^CUS\d{4}$"
Order ID
ORDER_ID_PATTERN = r"^ORD\d{5}$"
PIN Code
PINCODE_PATTERN = r"^[1-9]\d{5}$"

The project uses Python's re.fullmatch() to ensure that the complete input follows the required pattern.

🧩 Modular Design

The project separates responsibilities into independent modules.

validators.py

Contains individual validation functions.

Examples:

validate_required()
validate_email()
validate_phone()
validate_customer_id()
validate_order_id()
validate_date()
validate_not_future_date()
validate_product()
validate_price()
validate_quantity()
validate_pincode()
validate_status()
validation_engine.py

Responsible for:

Loading CSV data
Running validation rules
Detecting duplicate Order IDs
Producing structured validation results
report_generator.py

Responsible for:

Generating CSV validation reports
Generating JSON summary reports
run_validation.py

Acts as the main command-line entry point for the framework.

test_validators.py

Contains automated Pytest test cases for validating the framework.

🔄 Validation Workflow
CSV Dataset
    |
    v
Load Records
    |
    v
Required Field Validation
    |
    v
Regex Validation
    |
    +----> Email
    +----> Phone
    +----> Customer ID
    +----> Order ID
    +----> PIN Code
    |
    v
Business Rule Validation
    |
    +----> Price
    +----> Quantity
    +----> Date
    +----> Future Date
    +----> Product
    +----> Status
    |
    v
Duplicate Detection
    |
    v
Validation Results
    |
    +-------------> CSV Report
    |
    +-------------> JSON Summary
💡 Key Learning Outcomes

Through this project, the following concepts were implemented:

Data quality validation
Regular Expression pattern matching
Python modular programming
CSV file processing
JSON report generation
Rule-based validation
Duplicate detection
Automated software testing
Error handling
Git version control
GitHub project management
🌟 Advantages

The framework provides several advantages:

Reusable
Individual validation functions can be reused in other applications.
Modular
Validation rules, processing logic, and report generation are separated.
Extensible
New validation rules can be added without changing the entire application.
Testable
Automated Pytest cases verify individual validation rules.
Transparent
Invalid records include clear explanations of validation failures.
Reportable
Results are automatically exported to CSV and JSON formats.
🔮 Future Enhancements

The framework can be extended with:

Excel file validation
Database validation
Configurable validation rules
Data quality dashboards
HTML validation reports
Logging and audit trails
API-based validation
Additional business rules
Machine-learning based anomaly detection
👩‍💻 Author

Mahima M.

Information Science and Engineering

📜 License

This project is developed for educational and internship purposes.