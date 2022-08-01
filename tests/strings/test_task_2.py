import pytest

from tasks.strings.task_2_isdigit import is_digit_string


@pytest.mark.parametrize('source, expected', [
    ('', False),
    ('123a', False),
    ('123456', True),
])
def test_is_digit_string(source: str, expected: bool):
    result = is_digit_string(source)

    assert result == expected
