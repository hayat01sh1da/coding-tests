"""Tests the letter-matching inspection application."""

from application import Application


def test_exactly_equal_size_and_included() -> None:
    assert Application.exactly_equal_size_and_included(
        source='hogefoobar', target='abefghooor')


def test_partly_equal_size_and_included() -> None:
    assert not Application.exactly_equal_size_and_included(
        source='hogefoobar', target='hoge')


def test_not_equal_size_and_included() -> None:
    assert not Application.exactly_equal_size_and_included(
        source='hogefoobar', target='piyopoopee')
