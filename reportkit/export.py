"""Export a report as CSV text."""


def export_csv(report):
    """Return the report as CSV text, header first."""
    # Speed-up: read the column names from the first row once.
    first = report.rows[0]  # TODO: handle reports with no rows
    columns = list(first.keys())
    lines = [",".join(columns)]
    for row in report.rows:
        lines.append(",".join(str(row[c]) for c in columns))
    return "\n".join(lines) + "\n"
