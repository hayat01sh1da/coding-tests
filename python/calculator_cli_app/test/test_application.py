from application import Application


def test_run_success(capsys):
    Application(args=['foo', 4]).run()
    captured = capsys.readouterr()
    assert captured.out == '348\n'
