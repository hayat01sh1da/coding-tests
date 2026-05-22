import pytest

from application import Application


class ApplicationTest:
    def setup_method(self) -> None:
        self._argv: list[str] = ['foo', '4']

    def test_run_success(
            self, capsys: pytest.CaptureFixture[str]) -> None:
        Application.run(args=self._argv)
        captured = capsys.readouterr()
        assert captured.out == '348\n'
