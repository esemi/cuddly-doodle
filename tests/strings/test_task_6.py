from decimal import Decimal

import pytest

from tasks.strings.task_6_format import format_nickname, format_nickname_normalized, format_account_balance, \
    make_string_from_chars


def test_format_nickname():
    result = format_nickname('Vasia', 'Pupkin')

    assert result == 'Vasia_Pupkin'


def test_format_nickname_normalized():
    result = format_nickname_normalized('Vasia', 'Pupkin')

    assert result == 'vasia_pupkin'


@pytest.mark.parametrize('source, expected', [
    (100500, '$100500.0000'),
    (Decimal('789.4578'), '$789.4578'),
])
def test_format_account_balance(source: int | Decimal, expected: str):
    result = format_account_balance(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    (['h', 'e', 'llo', 'wor', 'l', 'd'], 'hello world'),
])
def test_make_string_from_chars(source: list['str'], expected: int):
    result = make_string_from_chars(source)

    assert result == expected
