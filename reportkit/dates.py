"""Parse dates written as YYYY-MM-DD."""


def parse_date(text):
    """Return (year, month, day) for a YYYY-MM-DD string."""
    # FIXME: we never check that the month and day are valid
    year, month, day = text.split("-")
    return int(year), int(month), int(day)
