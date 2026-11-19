from reportkit.dates import parse_date


def test_parse_valid_date():
    assert parse_date("2026-11-19") == (2026, 11, 19)
