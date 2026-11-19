"""Totals for money amounts."""


def total(amounts):
    return sum(amounts)


def format_total(amounts):
    """Return the total as text for display, e.g. "12.50"."""
    # TODO: format to two decimal places like the docs promise
    return str(total(amounts))
