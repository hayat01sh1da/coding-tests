import importlib.util
import os
import sys
from types import ModuleType

from invoke import Context, Exit, task

_ROOT = os.path.dirname(os.path.abspath(__file__))

PROJECTS = (
    'calculator_cli_app',
    'fibonacci_sequence',
    'fizzbuzz',
    'letter_matching_inspection',
    'nabeatsu',
)


def _load_application(project: str, *src_subdirs: str) -> ModuleType:
    src = os.path.join(_ROOT, project, 'src')
    for subdir in ('.', *src_subdirs):
        path = os.path.normpath(os.path.join(src, subdir))
        if path not in sys.path:
            sys.path.insert(0, path)
    spec = importlib.util.spec_from_file_location(
        f'{project}_application', os.path.join(src, 'application.py'))
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@task(positional=['seed', 'n'])
def run_calculator_cli_app(c: Context, seed: str, n: str) -> None:
    """Run CalculatorCliApp::Application"""
    application = _load_application(
        'calculator_cli_app', 'queries', 'validations')
    application.Application.run(args=[seed, n])


@task
def print_fibonacci_sequence(c: Context) -> None:
    """Print fibonacci sequence"""
    application = _load_application('fibonacci_sequence')

    print('Provide the initial number to start the sequence from')
    init_num = input().strip()

    print('Provide the number of iterations')
    iterations = input().strip()

    params: dict[str, int] = {}
    if init_num:
        params['init_num'] = int(init_num)
    if iterations:
        params['iter'] = int(iterations)

    print(', '.join(str(num) for num in application.fibonacci(**params)))


@task
def print_fizzbuzz_sequence(c: Context) -> None:
    """Print fizzbuzz sequence"""
    application = _load_application('fizzbuzz')

    print('Provide the initial number to start the sequence from')
    init_num = int(input().strip())

    print('Provide the terminal number of stop the sequence at')
    terminal_num = int(input().strip())

    print('Which logic do you want to use? '
          '(1: if, 2: if and ternary, 3: ternary)')
    logic_type = int(input().strip())

    result: list[str] = []
    for num in range(init_num, terminal_num + 1):
        if logic_type == 1:
            result.append(application.fizzbuzz_in_if(num))
        elif logic_type == 2:
            result.append(application.fizzbuzz_in_if_and_ternary(num))
        elif logic_type == 3:
            result.append(application.fizzbuzz_in_ternary(num))
        else:
            result.append(str(num))

    print(', '.join(result))


@task
def print_letter_matching_inspection(c: Context) -> None:
    """Print the result of letter matching inspection"""
    application = _load_application('letter_matching_inspection')

    print('Provide the source string to compare from')
    source = input().strip()

    print('Provide the target string to compare with')
    target = input().strip()

    result = application.Application.exactly_equal_size_and_included(
        source=source, target=target)
    print(f'Result: {str(result).lower()}')


@task
def print_nabeatsu_sequence(c: Context) -> None:
    """Print nabeatsu sequence"""
    application = _load_application('nabeatsu')

    print('Provide the initial number to start the sequence from')
    init_num = int(input().strip())

    print('Provide the terminal number of stop the sequence at')
    terminal_num = int(input().strip())

    print('Which logic do you want to use? (1: if, 2: ternary)')
    logic_type = int(input().strip())

    result: list[str] = []
    for num in range(init_num, terminal_num + 1):
        if logic_type == 1:
            result.append(application.go_crazy_in_if(num))
        elif logic_type == 2:
            result.append(application.go_crazy_in_ternary(num))
        else:
            result.append(str(num))

    print(', '.join(result))


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    failed: list[str] = []
    for project in PROJECTS:
        with c.cd(project):
            result = c.run('pytest .', warn=True)
        if result is None or not result.ok:
            failed.append(project)
    if failed:
        raise Exit(f'Tests failed in: {", ".join(failed)}', code=1)
