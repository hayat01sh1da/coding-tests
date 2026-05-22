## 1. Environment

- Python 3.14.5

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

### 3-1. Run CalculatorCliApp::Application

```command
$ invoke run_calculator_cli_app foo 4
348
```

### 3-2. Print fibonacci sequence

```command
$ invoke print_fibonacci_sequence
Provide the initial number to start the sequence from
0
Provide the number of iterations
10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 3-3. Print fizzbuzz sequence

```command
$ invoke print_fizzbuzz_sequence
Provide the initial number to start the sequence from
1
Provide the terminal number of stop the sequence at
15
Which logic do you want to use? (1: if, 2: if and ternary, 3: ternary)
1
1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
```

### 3-4. Print the result of letter matching inspection

```command
$ invoke print_letter_matching_inspection
Provide the source string to compare from
listen
Provide the target string to compare with
silent
Result: true
```

### 3-5. Print nabeatsu sequence

```command
$ invoke print_nabeatsu_sequence
Provide the initial number to start the sequence from
1
Provide the terminal number of stop the sequence at
15
Which logic do you want to use? (1: if, 2: ternary)
1
1, 2, 3!, 4, 5, 6!, 7, 8, 9!, 10, 11, 12!, 13!, 14, 15!
```

## 4. Unit Test

```command
$ invoke test
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: coding-tests/python/calculator_cli_app
configfile: pyproject.toml
collected 4 items

test/queries/test_calculation_query.py ...                               [ 75%]
test/test_application.py .                                               [100%]

============================== 4 passed in 1.91s ===============================
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: coding-tests/python/fibonacci_sequence
configfile: pyproject.toml
collected 2 items

test/test_application.py ..                                              [100%]

============================== 2 passed in 0.08s ===============================
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: coding-tests/python/fizzbuzz
configfile: pyproject.toml
collected 3 items

test/test_application.py ...                                             [100%]

============================== 3 passed in 0.10s ===============================
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: coding-tests/python/letter_matching_inspection
configfile: pyproject.toml
collected 3 items

test/test_application.py ...                                             [100%]

============================== 3 passed in 0.09s ===============================
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: coding-tests/python/nabeatsu
configfile: pyproject.toml
collected 2 items

test/test_application.py ..                                              [100%]

============================== 2 passed in 0.09s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Checks

```command
$ for directory in ./*/
$ do
$   echo "===== mypy ${directory} ====="
$   mypy "${directory}"
$ done
===== mypy ./calculator_cli_app/ =====
Success: no issues found in 7 source files
===== mypy ./fibonacci_sequence/ =====
Success: no issues found in 4 source files
===== mypy ./fizzbuzz/ =====
Success: no issues found in 4 source files
===== mypy ./letter_matching_inspection/ =====
Success: no issues found in 4 source files
===== mypy ./nabeatsu/ =====
Success: no issues found in 4 source files
```
