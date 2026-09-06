"""
Main entry point for the
Task 14 - Business Data Validation Framework.
"""

from src.validation_engine import validate_csv
from src.report_generator import generate_reports


# ============================================================
# CONFIGURATION
# ============================================================

DATA_FILE = "data/customer_orders.csv"


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("=" * 60)
    print("BUSINESS DATA VALIDATION FRAMEWORK")
    print("=" * 60)

    print(f"\nDataset: {DATA_FILE}")

    # --------------------------------------------------------
    # VALIDATE DATASET
    # --------------------------------------------------------

    results = validate_csv(DATA_FILE)

    total_records = len(results)

    valid_records = sum(
        result["is_valid"]
        for result in results
    )

    invalid_records = (
        total_records - valid_records
    )

    # --------------------------------------------------------
    # VALIDATION RATE
    # --------------------------------------------------------

    if total_records > 0:

        validation_rate = (
            valid_records /
            total_records
        ) * 100

    else:

        validation_rate = 0

    # --------------------------------------------------------
    # DISPLAY SUMMARY
    # --------------------------------------------------------

    print("\nVALIDATION SUMMARY")
    print("-" * 60)

    print(
        f"Total records   : {total_records}"
    )

    print(
        f"Valid records   : {valid_records}"
    )

    print(
        f"Invalid records : {invalid_records}"
    )

    print(
        f"Validation rate : {validation_rate:.2f}%"
    )

    # --------------------------------------------------------
    # DISPLAY INVALID RECORDS
    # --------------------------------------------------------

    print("\nINVALID RECORDS")
    print("-" * 60)

    for result in results:

        if not result["is_valid"]:

            print(
                f"{result['order_id']} -> "
                f"{'; '.join(result['errors'])}"
            )

    # --------------------------------------------------------
    # GENERATE REPORTS
    # --------------------------------------------------------

    generate_reports(results)

    print("\nREPORTS GENERATED")
    print("-" * 60)

    print(
        "reports/validation_report.csv"
    )

    print(
        "reports/validation_summary.json"
    )

    print(
        "\nValidation completed successfully."
    )


# ============================================================
# PROGRAM ENTRY
# ============================================================

if __name__ == "__main__":
    main()