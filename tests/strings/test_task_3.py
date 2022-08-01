import pytest

from tasks.strings.task_3_reverse import reverse_string


@pytest.mark.parametrize('source, expected', [
    ('', ''),
    ('1', '1'),
    ('abcde', 'edcba'),
])
def test_reverse(source: str, expected: str):
    result = reverse_string(source)

    assert result == expected
