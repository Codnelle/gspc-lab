"""Data model: a report is a title plus a list of rows."""

from dataclasses import dataclass, field


@dataclass
class Report:
    title: str
    rows: list = field(default_factory=list)  # each row: {"date": str, "amount": number}

    def add(self, date, amount):
        self.rows.append({"date": date, "amount": amount})
        return self
