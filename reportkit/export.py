"""Export a report as CSV text."""

HEADER = ["date", "amount"]


def export_csv(report):
    """Return the report as CSV text, header first."""
    lines = [",".join(HEADER)]
    for row in report.rows:
        lines.append(f"{row['date']},{row['amount']}")
    return "\n".join(lines) + "\n"
