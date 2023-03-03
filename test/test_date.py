from datetime import date

import pytest

from notion_extensions.utils.date import get_new_date


def test_get_new_date():
    today = date(2023, 3, 1)
    assert get_new_date(-1, 5, today=today).day == 3
    assert get_new_date(-1, 6, today=today).day == 4
    assert get_new_date(-1, 7, today=today).day == 5
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 1
    assert get_new_date(0, 4, today=today).day == 2
    assert get_new_date(0, 5, today=today).day == 10
    assert get_new_date(0, 6, today=today).day == 11
    assert get_new_date(0, 7, today=today).day == 12

    today = date(2023, 3, 2)
    assert get_new_date(-1, 5, today=today).day == 3
    assert get_new_date(-1, 6, today=today).day == 4
    assert get_new_date(-1, 7, today=today).day == 5
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 2
    assert get_new_date(0, 5, today=today).day == 10
    assert get_new_date(0, 6, today=today).day == 11
    assert get_new_date(0, 7, today=today).day == 12

    today = date(2023, 3, 3)
    assert get_new_date(-1, 5, today=today).day == 3
    assert get_new_date(-1, 6, today=today).day == 4
    assert get_new_date(-1, 7, today=today).day == 5
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 10
    assert get_new_date(0, 6, today=today).day == 11
    assert get_new_date(0, 7, today=today).day == 12

    today = date(2023, 3, 4)
    assert get_new_date(-1, 5, today=today).day == 10
    assert get_new_date(-1, 6, today=today).day == 4
    assert get_new_date(-1, 7, today=today).day == 5
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 10
    assert get_new_date(0, 6, today=today).day == 11
    assert get_new_date(0, 7, today=today).day == 12

    today = date(2023, 3, 5)
    assert get_new_date(-1, 5, today=today).day == 10
    assert get_new_date(-1, 6, today=today).day == 11
    assert get_new_date(-1, 7, today=today).day == 5
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 10
    assert get_new_date(0, 6, today=today).day == 11
    assert get_new_date(0, 7, today=today).day == 12

    today = date(2023, 3, 6)
    assert get_new_date(-1, 5, today=today).day == 10
    assert get_new_date(-1, 6, today=today).day == 11
    assert get_new_date(-1, 7, today=today).day == 12
    assert get_new_date(0, 1, today=today).day == 6
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 17
    assert get_new_date(0, 6, today=today).day == 18
    assert get_new_date(0, 7, today=today).day == 19

    today = date(2023, 3, 7)
    assert get_new_date(-1, 5, today=today).day == 10
    assert get_new_date(-1, 6, today=today).day == 11
    assert get_new_date(-1, 7, today=today).day == 12
    assert get_new_date(0, 1, today=today).day == 13
    assert get_new_date(0, 2, today=today).day == 7
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 17
    assert get_new_date(0, 6, today=today).day == 18
    assert get_new_date(0, 7, today=today).day == 19

    today = date(2023, 3, 8)
    assert get_new_date(-1, 5, today=today).day == 10
    assert get_new_date(-1, 6, today=today).day == 11
    assert get_new_date(-1, 7, today=today).day == 12
    assert get_new_date(0, 1, today=today).day == 13
    assert get_new_date(0, 2, today=today).day == 14
    assert get_new_date(0, 3, today=today).day == 8
    assert get_new_date(0, 4, today=today).day == 9
    assert get_new_date(0, 5, today=today).day == 17
    assert get_new_date(0, 6, today=today).day == 18
    assert get_new_date(0, 7, today=today).day == 19
    