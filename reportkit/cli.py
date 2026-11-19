"""Command line interface: python -m reportkit <command> [options]."""

import sys

from reportkit.export import export_csv
from reportkit.models import Report

FORMATS = {"csv": export_csv}


def _option(argv, name, default):
    if name in argv:
        return argv[argv.index(name) + 1]
    return default


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] in ("-h", "--help"):
        print("usage: reportkit export [--format csv] [--rows N]")
        return 0
    command = argv[0]
    if command == "export":
        fmt = _option(argv, "--format", "csv")
        exporter = FORMATS[fmt]
        count = int(_option(argv, "--rows", "1"))
        report = Report("Sample")
        for i in range(count):
            report.add(f"2026-01-{i + 1:02d}", 5 * (i + 1))
        sys.stdout.write(exporter(report))
        return 0
    print(f"unknown command: {command}", file=sys.stderr)
    return 2
