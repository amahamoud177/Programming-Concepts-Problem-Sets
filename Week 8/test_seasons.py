from datetime import date, timedelta
from seasons import calculate_minutes


def test_today():
    today = date.today()
    assert calculate_minutes(today) == 0