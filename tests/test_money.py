from reportkit.money import format_total, total


def test_total_whole_numbers():
    assert total([1, 2, 3]) == 6


def test_format_total_whole_numbers():
    assert format_total([10, 5]) == "15"
