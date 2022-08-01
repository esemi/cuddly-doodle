import pytest

from tasks.strings.task_4_clearing import strip_string, replace_string


@pytest.mark.parametrize('source, expected', [
    ('', ''),
    ("\t sdsdsd \t", 'sdsdsd'),
    ("{sdsdsd}", 'sdsdsd'),
])
def test_strip_string(source: str, expected: str):
    result = strip_string(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ("Hello, %USERNAME%", 'Hello, John'),
])
def test_replace_chars(source: str, expected: str):
    result = replace_string(source)

    assert result == expected
