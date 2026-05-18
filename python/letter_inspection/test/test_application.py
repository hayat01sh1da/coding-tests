import pytest

from application import Application


@pytest.mark.parametrize(
    ('str_1', 'str_2', 'expected'),
    [
        ('hogefoobar', 'abefghooor', True),
        ('hogefoobar', 'hoge', False),
        ('hogefoobar', 'piyopoopee', False),
    ],
)
def test_exactly_equal_size_and_included(
        str_1: str, str_2: str, expected: bool) -> None:
    assert Application(
        str_1=str_1,
        str_2=str_2).exactly_equal_size_and_included() is expected
