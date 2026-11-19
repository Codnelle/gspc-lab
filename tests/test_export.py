from reportkit.export import export_csv
from reportkit.models import Report


def test_export_one_row():
    report = Report("Q3").add("2026-01-01", 5)
    assert export_csv(report) == "date,amount\n2026-01-01,5\n"


def test_export_many_rows():
    report = Report("Q3").add("2026-01-01", 5).add("2026-01-02", 7)
    assert export_csv(report) == "date,amount\n2026-01-01,5\n2026-01-02,7\n"
