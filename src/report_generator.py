"""
Report generator for the Task 14
Business Data Validation Framework.

Generates:
1. Detailed CSV validation report
2. JSON validation summary
"""

import csv
import json
from pathlib import Path


def generate_csv_report(results, output_file):
    """
    Generate a detailed CSV validation report.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(
        output_path,
        mode="w",
        encoding="utf-8",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Order ID",
            "Validation Status",
            "Error Count",
            "Validation Errors"
        ])

        for result in results:

            status = (
                "VALID"
                if result["is_valid"]
                else "INVALID"
            )

            errors = " | ".join(result["errors"])

            writer.writerow([
                result["order_id"],
                status,
                len(result["errors"]),
                errors
            ])


def generate_json_summary(results, output_file):
    """
    Generate a JSON summary of validation results.
    """

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total_records = len(results)

    valid_records = sum(
        result["is_valid"]
        for result in results
    )

    invalid_records = total_records - valid_records

    validation_rate = (
        (valid_records / total_records) * 100
        if total_records > 0
        else 0
    )

    summary = {
        "project": "Business Data Validation Framework",
        "total_records": total_records,
        "valid_records": valid_records,
        "invalid_records": invalid_records,
        "validation_rate": round(validation_rate, 2)
    }

    with open(
        output_path,
        mode="w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )


def generate_reports(results):
    """
    Generate all validation reports.
    """

    generate_csv_report(
        results,
        "reports/validation_report.csv"
    )

    generate_json_summary(
        results,
        "reports/validation_summary.json"
    )