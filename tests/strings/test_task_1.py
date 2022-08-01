import pytest

from tasks.strings.task_1_capitalize import capitalize_string, to_lower_string, to_upper_string


@pytest.mark.parametrize('source, expected', [
    ('', ''),
    ('hello world', 'Hello world'),
])
def test_capitalize_string(source: str, expected: str):
    result = capitalize_string(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('HELLO woRld', 'hello world'),
    ('hello world', 'hello world'),
])
def test_to_lower_string(source: str, expected: str):
    result = to_lower_string(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('HELLO woRld', 'HELLO WORLD'),
    ('HELLO WORLD', 'HELLO WORLD'),
])
def test_to_upper_string(source: str, expected: str):
    result = to_upper_string(source)

    assert result == expected
