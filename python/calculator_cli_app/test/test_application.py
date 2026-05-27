import pytest

from application import Application


def test_run_success(capsys: pytest.CaptureFixture[str]) -> None:
    Application.run(args=['foo', '4'])
    captured = capsys.readouterr()
    assert captured.out == '348\n'
