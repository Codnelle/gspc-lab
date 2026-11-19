from reportkit.cli import main


def test_export_csv(capsys):
    assert main(["export", "--format", "csv"]) == 0
    assert capsys.readouterr().out.startswith("date,amount\n")
