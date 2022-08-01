import pytest

from tasks.strings.task_5_subsctring import string_starts, string_ends, char_count, top_char, get_firstname, \
    first_chars, end_chars


@pytest.mark.parametrize('source, expected', [
    ('user: name', True),
    ('user: second name', True),
    ('invalid string', False),
])
def test_string_starts(source: str, expected: bool):
    result = string_starts(source, 'user:')

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('user content :end of string', True),
    ('invalid string', False),
])
def test_string_ends(source: str, expected: bool):
    result = string_ends(source, ':end of string')

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('aabbbccccc', 2),
    ('aaaab', 4),
    ('sdsdsdsd', 0),
])
def test_char_count(source: str, expected: int):
    char_for_search = 'a'

    result = char_count(source, char_for_search)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('aabbbccccc', 'c'),
    ('aaaab', 'a'),
    ('', ''),
])
def test_top_char(source: str, expected: str):
    result = top_char(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('first name, last name', 'first name'),
    ('firstname', 'firstname'),
    ('', ''),
])
def test_get_firstname(source: str, expected: str):
    result = get_firstname(source)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('lorem ipsum blablabla', 'lorem'),
    ('lor', 'lor'),
])
def test_first_chars(source: str, expected: str):
    result = first_chars(source, 5)

    assert result == expected


@pytest.mark.parametrize('source, expected', [
    ('lorem ipsum', 'ipsum'),
    ('lor', 'lor'),
])
def test_end_chars(source: str, expected: str):
    result = end_chars(source, 5)

    assert result == expected
