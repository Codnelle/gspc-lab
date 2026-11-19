# Architecture

ReportKit is four small modules.

| Module | Job |
| --- | --- |
| `models.py` | `Report`: a title and a list of rows |
| `export.py` | Turns a report into CSV text |
| `dates.py` | Parses `YYYY-MM-DD` strings |
| `money.py` | Totals and formats money amounts |

`cli.py` is the entry point: `python -m reportkit export --format csv`
reads the options, builds a report, and calls the exporter for that format.

Flow for an export:

    command line -> cli.main() -> FORMATS[fmt] -> export_csv(report) -> stdout
