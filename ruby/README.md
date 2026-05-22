## 1. Environment

- Ruby 4.0.5

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

### 3-1. Run CalculatorCliApp::Application

```command
$ rake run_calculator_cli_app -- foo 4
348
```

### 3-2. Print fibonacci sequence

```command
$ rake print_fibonacci_sequence
Provide the initial number to start the sequence from
0
Provide the number of iterations
10
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### 3-3. Print fizzbuzz sequence

```command
$ rake print_fizzbuzz_sequence
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
$ rake print_letter_matching_inspection
Provide the source string to compare from
listen
Provide the target string to compare with
silent
Result: true
```

### 3-5. Print nabeatsu sequence

```command
$ rake print_nabeatsu_sequence
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
$ rake
Run options: --seed 20563

# Running:

..............

Finished in 1.575424s, 8.8865 runs/s, 246.9177 assertions/s.

14 runs, 389 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 15 files
...............

15 files inspected, no offenses detected
```

## 6. Type Checks

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 10 RBS files under sig/generated
$ steep check
15 files inspected, no offenses detected
# Type checking files:

FFFFFFFFFFFFF

fibonacci_sequence/test/application_test.rb:4:6: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test; end
        ~~~~~~~~~~~~~~~

fibonacci_sequence/test/application_test.rb:4:24: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test; end
                          ~~~~~~~~

fibonacci_sequence/test/application_test.rb:6:6: [warning] Cannot find the declaration of class: `TestCase1`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TestCase1 < ApplicationTest
        ~~~~~~~~~

fibonacci_sequence/test/application_test.rb:6:18: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TestCase1 < ApplicationTest
                    ~~~~~~~~~~~~~~~

fibonacci_sequence/test/application_test.rb:10:6: [error] Type `::Object` does not have method `fibonacci`
│ Diagnostic ID: Ruby::NoMethod
│
└       fibonacci(init_num: 0, iter: 10)
        ~~~~~~~~~

fibonacci_sequence/test/application_test.rb:8:4: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(
      ~~~~~~~~~~~~

fibonacci_sequence/test/application_test.rb:15:6: [warning] Cannot find the declaration of class: `TestCase2`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TestCase2 < ApplicationTest
        ~~~~~~~~~

fibonacci_sequence/test/application_test.rb:15:18: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TestCase2 < ApplicationTest
                    ~~~~~~~~~~~~~~~

fibonacci_sequence/test/application_test.rb:19:6: [error] Type `::Object` does not have method `fibonacci`
│ Diagnostic ID: Ruby::NoMethod
│
└       fibonacci(init_num: 10, iter: 10)
        ~~~~~~~~~

fibonacci_sequence/test/application_test.rb:17:4: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(
      ~~~~~~~~~~~~

fizzbuzz/src/application.rb:1:4: [warning] Method `::Object#fizzbuzz_in_if` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def fizzbuzz_in_if(num)
      ~~~~~~~~~~~~~~

fizzbuzz/src/application.rb:13:4: [warning] Method `::Object#fizzbuzz_in_if_and_ternary` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def fizzbuzz_in_if_and_ternary(num)
      ~~~~~~~~~~~~~~~~~~~~~~~~~~

fizzbuzz/src/application.rb:21:4: [warning] Method `::Object#fizzbuzz_in_ternary` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def fizzbuzz_in_ternary(num)
      ~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:4:7: [warning] Cannot find the declaration of module: `LetterMatchingInspection`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ module LetterMatchingInspection
         ~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:5:8: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   class ApplicationTest < Minitest::Test
          ~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:5:26: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   class ApplicationTest < Minitest::Test
                            ~~~~~~~~

letter_matching_inspection/test/application_test.rb:7:15: [warning] Cannot find the declaration of constant: `LetterMatchingInspection`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       assert ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                 ~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:7:6: [error] Type `::Object` does not have method `assert`
│ Diagnostic ID: Ruby::NoMethod
│
└       assert ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
        ~~~~~~

letter_matching_inspection/test/application_test.rb:12:15: [warning] Cannot find the declaration of constant: `LetterMatchingInspection`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                 ~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:12:6: [error] Type `::Object` does not have method `refute`
│ Diagnostic ID: Ruby::NoMethod
│
└       refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
        ~~~~~~

letter_matching_inspection/test/application_test.rb:17:15: [warning] Cannot find the declaration of constant: `LetterMatchingInspection`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
                 ~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/test/application_test.rb:17:6: [error] Type `::Object` does not have method `refute`
│ Diagnostic ID: Ruby::NoMethod
│
└       refute ::LetterMatchingInspection::Application.exactly_equal_size_and_included?(source: 'hogefoobar',
        ~~~~~~

nabeatsu/src/application.rb:1:4: [warning] Method `::Object#go_crazy_in_if` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def go_crazy_in_if(num)
      ~~~~~~~~~~~~~~

nabeatsu/src/application.rb:10:4: [warning] Method `::Object#go_crazy_in_ternary` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def go_crazy_in_ternary(num)
      ~~~~~~~~~~~~~~~~~~~

calculator_cli_app/src/application.rb:4:7: [warning] Cannot find the declaration of module: `CalculatorCliApp`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ module CalculatorCliApp
         ~~~~~~~~~~~~~~~~

calculator_cli_app/src/application.rb:5:8: [warning] Cannot find the declaration of class: `Application`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   class Application
          ~~~~~~~~~~~

calculator_cli_app/src/application.rb:6:14: [warning] Cannot find the declaration of constant: `Validations`
│ Diagnostic ID: Ruby::UnknownConstant
│
└     include ::Validations::ArgsValidation
                ~~~~~~~~~~~

calculator_cli_app/src/application.rb:8:13: [warning] Method `::Object.run!` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└     def self.run!(args)
               ~~~~

calculator_cli_app/src/application.rb:9:10: [error] Unexpected positional argument
│ Diagnostic ID: Ruby::UnexpectedPositionalArgument
│
└       new(args).run!
            ~~~~

calculator_cli_app/src/application.rb:9:16: [error] Type `::Object` does not have method `run!`
│ Diagnostic ID: Ruby::NoMethod
│
└       new(args).run!
                  ~~~~

calculator_cli_app/src/application.rb:19:16: [error] Type `::Object` does not have method `args_size`
│ Diagnostic ID: Ruby::NoMethod
│
└       validate!(args_size, seed, n.to_i.nonzero?)
                  ~~~~~~~~~

calculator_cli_app/src/application.rb:19:27: [error] Type `::Object` does not have method `seed`
│ Diagnostic ID: Ruby::NoMethod
│
└       validate!(args_size, seed, n.to_i.nonzero?)
                             ~~~~

calculator_cli_app/src/application.rb:19:33: [error] Type `::Object` does not have method `n`
│ Diagnostic ID: Ruby::NoMethod
│
└       validate!(args_size, seed, n.to_i.nonzero?)
                                   ~

calculator_cli_app/src/application.rb:19:6: [error] Type `::Object` does not have method `validate!`
│ Diagnostic ID: Ruby::NoMethod
│
└       validate!(args_size, seed, n.to_i.nonzero?)
        ~~~~~~~~~

calculator_cli_app/src/application.rb:21:15: [error] Type `::Object` does not have method `calculation_query`
│ Diagnostic ID: Ruby::NoMethod
│
└       result = calculation_query.f(n)
                 ~~~~~~~~~~~~~~~~~

calculator_cli_app/src/application.rb:21:35: [error] Type `::Object` does not have method `n`
│ Diagnostic ID: Ruby::NoMethod
│
└       result = calculation_query.f(n)
                                     ~

calculator_cli_app/src/application.rb:30:31: [warning] Cannot find the declaration of constant: `Queries`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       @calculation_query ||= ::Queries::CalculationQuery.new(seed)
                                 ~~~~~~~

calculator_cli_app/src/application.rb:30:61: [error] Type `::Object` does not have method `seed`
│ Diagnostic ID: Ruby::NoMethod
│
└       @calculation_query ||= ::Queries::CalculationQuery.new(seed)
                                                               ~~~~

calculator_cli_app/test/application_test.rb:4:6: [warning] Cannot find the declaration of constant: `CalculatorCliApp`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class CalculatorCliApp::ApplicationTest < Minitest::Test
        ~~~~~~~~~~~~~~~~

calculator_cli_app/test/application_test.rb:4:42: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class CalculatorCliApp::ApplicationTest < Minitest::Test
                                            ~~~~~~~~

calculator_cli_app/test/application_test.rb:10:31: [warning] Cannot find the declaration of constant: `CalculatorCliApp`
│ Diagnostic ID: Ruby::UnknownConstant
│
└     assert_output("348\n") { ::CalculatorCliApp::Application.run!(argv) }
                                 ~~~~~~~~~~~~~~~~

calculator_cli_app/test/application_test.rb:10:66: [error] Type `::Object` does not have method `argv`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_output("348\n") { ::CalculatorCliApp::Application.run!(argv) }
                                                                    ~~~~

calculator_cli_app/test/application_test.rb:10:4: [error] Type `::Object` does not have method `assert_output`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_output("348\n") { ::CalculatorCliApp::Application.run!(argv) }
      ~~~~~~~~~~~~~

fibonacci_sequence/src/application.rb:1:4: [warning] Method `::Object#fibonacci` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└ def fibonacci(init_num:, iter:)
      ~~~~~~~~~

fibonacci_sequence/src/application.rb:4:16: [warning] Empty array doesn't have type annotation
│ Diagnostic ID: Ruby::UnannotatedEmptyCollection
│
└   result      = []
                  ~~

calculator_cli_app/src/queries/calculation_query.rb:4:7: [warning] Cannot find the declaration of module: `Queries`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ module Queries
         ~~~~~~~

calculator_cli_app/src/queries/calculation_query.rb:5:8: [warning] Cannot find the declaration of class: `CalculationQuery`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   class CalculationQuery
          ~~~~~~~~~~~~~~~~

calculator_cli_app/src/queries/calculation_query.rb:16:8: [error] Type `::Object` does not have method `f`
│ Diagnostic ID: Ruby::NoMethod
│
└         f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
          ~

calculator_cli_app/src/queries/calculation_query.rb:16:19: [error] Type `::Object` does not have method `f`
│ Diagnostic ID: Ruby::NoMethod
│
└         f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
                     ~

calculator_cli_app/src/queries/calculation_query.rb:16:30: [error] Type `::Object` does not have method `f`
│ Diagnostic ID: Ruby::NoMethod
│
└         f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
                                ~

calculator_cli_app/src/queries/calculation_query.rb:16:41: [error] Type `::Object` does not have method `f`
│ Diagnostic ID: Ruby::NoMethod
│
└         f(n - 1) + f(n - 2) + f(n - 3) + f(n - 4)
                                           ~

calculator_cli_app/src/queries/calculation_query.rb:18:8: [error] Type `::Object` does not have method `ask_server`
│ Diagnostic ID: Ruby::NoMethod
│
└         ask_server(n)
          ~~~~~~~~~~

calculator_cli_app/src/queries/calculation_query.rb:27:15: [warning] Cannot find the declaration of constant: `URI`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       @uri ||= URI.parse(ENV['CALCULATION_API'])
                 ~~~

calculator_cli_app/src/queries/calculation_query.rb:31:20: [error] Type `::Object` does not have method `seed`
│ Diagnostic ID: Ruby::NoMethod
│
└       params    = { seed:, n: }
                      ~~~~

calculator_cli_app/src/queries/calculation_query.rb:32:6: [error] Type `::Object` does not have method `uri`
│ Diagnostic ID: Ruby::NoMethod
│
└       uri.query = URI.encode_www_form(params)
        ~~~

calculator_cli_app/src/queries/calculation_query.rb:32:18: [warning] Cannot find the declaration of constant: `URI`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       uri.query = URI.encode_www_form(params)
                    ~~~

calculator_cli_app/src/queries/calculation_query.rb:33:18: [warning] Cannot find the declaration of constant: `Net`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       req       = Net::HTTP::Get.new(uri)
                    ~~~

calculator_cli_app/src/queries/calculation_query.rb:33:37: [error] Type `::Object` does not have method `uri`
│ Diagnostic ID: Ruby::NoMethod
│
└       req       = Net::HTTP::Get.new(uri)
                                       ~~~

calculator_cli_app/src/queries/calculation_query.rb:34:18: [warning] Cannot find the declaration of constant: `Net`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       res       = Net::HTTP.start(uri.host, uri.port) { it.request(req) }
                    ~~~

calculator_cli_app/src/queries/calculation_query.rb:34:34: [error] Type `::Object` does not have method `uri`
│ Diagnostic ID: Ruby::NoMethod
│
└       res       = Net::HTTP.start(uri.host, uri.port) { it.request(req) }
                                    ~~~

calculator_cli_app/src/queries/calculation_query.rb:34:44: [error] Type `::Object` does not have method `uri`
│ Diagnostic ID: Ruby::NoMethod
│
└       res       = Net::HTTP.start(uri.host, uri.port) { it.request(req) }
                                              ~~~

calculator_cli_app/src/queries/calculation_query.rb:34:56: [error] Type `::Object` does not have method `it`
│ Diagnostic ID: Ruby::NoMethod
│
└       res       = Net::HTTP.start(uri.host, uri.port) { it.request(req) }
                                                          ~~

calculator_cli_app/src/queries/calculation_query.rb:35:6: [warning] Cannot find the declaration of constant: `JSON`
│ Diagnostic ID: Ruby::UnknownConstant
│
└       JSON.parse(res.body)['result']
        ~~~~

letter_matching_inspection/src/application.rb:1:7: [warning] Cannot find the declaration of module: `LetterMatchingInspection`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ module LetterMatchingInspection
         ~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/src/application.rb:2:8: [warning] Cannot find the declaration of class: `Application`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   class Application
          ~~~~~~~~~~~

letter_matching_inspection/src/application.rb:3:13: [warning] Method `::Object.exactly_equal_size_and_included?` is not declared in RBS
│ Diagnostic ID: Ruby::UndeclaredMethodDefinition
│
└     def self.exactly_equal_size_and_included?(source:, target:)
               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/src/application.rb:4:10: [error] Unexpected keyword argument
│ Diagnostic ID: Ruby::UnexpectedKeywordArgument
│
└       new(source:, target:).exactly_equal_size_and_included?
            ~~~~~~

letter_matching_inspection/src/application.rb:4:19: [error] Unexpected keyword argument
│ Diagnostic ID: Ruby::UnexpectedKeywordArgument
│
└       new(source:, target:).exactly_equal_size_and_included?
                     ~~~~~~

letter_matching_inspection/src/application.rb:4:28: [error] Type `::Object` does not have method `exactly_equal_size_and_included?`
│ Diagnostic ID: Ruby::NoMethod
│
└       new(source:, target:).exactly_equal_size_and_included?
                              ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

letter_matching_inspection/src/application.rb:13:18: [error] Type `::Object` does not have method `source`
│ Diagnostic ID: Ruby::NoMethod
│
└       sort_string(source) == sort_string(target)
                    ~~~~~~

letter_matching_inspection/src/application.rb:13:6: [error] Type `::Object` does not have method `sort_string`
│ Diagnostic ID: Ruby::NoMethod
│
└       sort_string(source) == sort_string(target)
        ~~~~~~~~~~~

letter_matching_inspection/src/application.rb:13:41: [error] Type `::Object` does not have method `target`
│ Diagnostic ID: Ruby::NoMethod
│
└       sort_string(source) == sort_string(target)
                                           ~~~~~~

letter_matching_inspection/src/application.rb:13:29: [error] Type `::Object` does not have method `sort_string`
│ Diagnostic ID: Ruby::NoMethod
│
└       sort_string(source) == sort_string(target)
                               ~~~~~~~~~~~

calculator_cli_app/src/validations/args_validation.rb:1:7: [warning] Cannot find the declaration of module: `Validations`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ module Validations
         ~~~~~~~~~~~

calculator_cli_app/src/validations/args_validation.rb:2:9: [warning] Cannot find the declaration of module: `ArgsValidation`
│ Diagnostic ID: Ruby::UnknownConstant
│
└   module ArgsValidation
           ~~~~~~~~~~~~~~

calculator_cli_app/src/validations/args_validation.rb:5:8: [error] Type `::BasicObject` does not have method `puts`
│ Diagnostic ID: Ruby::NoMethod
│
└         puts 'Too many arguments'
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:6:8: [error] Type `::BasicObject` does not have method `exit`
│ Diagnostic ID: Ruby::NoMethod
│
└         exit 1
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:8:8: [error] Type `::BasicObject` does not have method `puts`
│ Diagnostic ID: Ruby::NoMethod
│
└         puts 'No argument provided'
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:9:8: [error] Type `::BasicObject` does not have method `exit`
│ Diagnostic ID: Ruby::NoMethod
│
└         exit 1
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:11:8: [error] Type `::BasicObject` does not have method `puts`
│ Diagnostic ID: Ruby::NoMethod
│
└         puts 'Provide both seed and n'
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:12:8: [error] Type `::BasicObject` does not have method `exit`
│ Diagnostic ID: Ruby::NoMethod
│
└         exit 1
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:14:8: [error] Type `::BasicObject` does not have method `puts`
│ Diagnostic ID: Ruby::NoMethod
│
└         puts 'Provide seed as string and n as number'
          ~~~~

calculator_cli_app/src/validations/args_validation.rb:15:8: [error] Type `::BasicObject` does not have method `exit`
│ Diagnostic ID: Ruby::NoMethod
│
└         exit 1
          ~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:4:6: [warning] Cannot find the declaration of class: `CalculationQueryTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class CalculationQueryTest < Minitest::Test
        ~~~~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:4:29: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class CalculationQueryTest < Minitest::Test
                               ~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:6:27: [warning] Cannot find the declaration of constant: `Queries`
│ Diagnostic ID: Ruby::UnknownConstant
│
└     @calculation_query = ::Queries::CalculationQuery.new('foo')
                             ~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:14:6: [warning] Cannot find the declaration of class: `ArgumentZeroTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentZeroTest < CalculationQueryTest
        ~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:14:25: [warning] Cannot find the declaration of class: `CalculationQueryTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentZeroTest < CalculationQueryTest
                           ~~~~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:16:20: [error] Type `::Object` does not have method `calculation_query`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(1, calculation_query.f(0))
                      ~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:16:4: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(1, calculation_query.f(0))
      ~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:20:6: [warning] Cannot find the declaration of class: `ArgumentTwoTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentTwoTest < CalculationQueryTest
        ~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:20:24: [warning] Cannot find the declaration of class: `CalculationQueryTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentTwoTest < CalculationQueryTest
                          ~~~~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:22:20: [error] Type `::Object` does not have method `calculation_query`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(2, calculation_query.f(2))
                      ~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:22:4: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(2, calculation_query.f(2))
      ~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:26:6: [warning] Cannot find the declaration of class: `ArgumentFourTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentFourTest < CalculationQueryTest
        ~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:26:25: [warning] Cannot find the declaration of class: `CalculationQueryTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ArgumentFourTest < CalculationQueryTest
                           ~~~~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:28:22: [error] Type `::Object` does not have method `calculation_query`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(348, calculation_query.f(4))
                        ~~~~~~~~~~~~~~~~~

calculator_cli_app/test/queries/calculation_query_test.rb:28:4: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└     assert_equal(348, calculation_query.f(4))
      ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:4:6: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test; end
        ~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:4:24: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test; end
                          ~~~~~~~~

fizzbuzz/test/application_test.rb:6:6: [warning] Cannot find the declaration of class: `IfStatementTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class IfStatementTest < ApplicationTest
        ~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:6:24: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class IfStatementTest < ApplicationTest
                          ~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:10:33: [error] Type `::Object` does not have method `fizzbuzz_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_if(num)
                                   ~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:10:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_if(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:12:29: [error] Type `::Object` does not have method `fizzbuzz_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_if(num)
                               ~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:12:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_if(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:14:29: [error] Type `::Object` does not have method `fizzbuzz_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_if(num)
                               ~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:14:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_if(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:16:31: [error] Type `::Object` does not have method `fizzbuzz_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_if(num)
                                 ~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:16:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_if(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:22:6: [warning] Cannot find the declaration of class: `TernaryStatementTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TernaryStatementTest < ApplicationTest
        ~~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:22:29: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class TernaryStatementTest < ApplicationTest
                               ~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:26:33: [error] Type `::Object` does not have method `fizzbuzz_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_ternary(num)
                                   ~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:26:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:28:29: [error] Type `::Object` does not have method `fizzbuzz_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_ternary(num)
                               ~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:28:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:30:29: [error] Type `::Object` does not have method `fizzbuzz_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_ternary(num)
                               ~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:30:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:32:31: [error] Type `::Object` does not have method `fizzbuzz_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_ternary(num)
                                 ~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:32:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:38:6: [warning] Cannot find the declaration of class: `HybridStatementTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class HybridStatementTest < ApplicationTest
        ~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:38:28: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class HybridStatementTest < ApplicationTest
                              ~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:42:33: [error] Type `::Object` does not have method `fizzbuzz_in_if_and_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_if_and_ternary(num)
                                   ~~~~~~~~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:42:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'FizzBuzz', fizzbuzz_in_if_and_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:44:29: [error] Type `::Object` does not have method `fizzbuzz_in_if_and_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_if_and_ternary(num)
                               ~~~~~~~~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:44:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Fizz', fizzbuzz_in_if_and_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:46:29: [error] Type `::Object` does not have method `fizzbuzz_in_if_and_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_if_and_ternary(num)
                               ~~~~~~~~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:46:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal 'Buzz', fizzbuzz_in_if_and_ternary(num)
          ~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:48:31: [error] Type `::Object` does not have method `fizzbuzz_in_if_and_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_if_and_ternary(num)
                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~

fizzbuzz/test/application_test.rb:48:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, fizzbuzz_in_if_and_ternary(num)
          ~~~~~~~~~~~~

nabeatsu/test/application_test.rb:4:6: [warning] Cannot find the declaration of class: `ApplicationTest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test
        ~~~~~~~~~~~~~~~

nabeatsu/test/application_test.rb:4:24: [warning] Cannot find the declaration of constant: `Minitest`
│ Diagnostic ID: Ruby::UnknownConstant
│
└ class ApplicationTest < Minitest::Test
                          ~~~~~~~~

nabeatsu/test/application_test.rb:8:32: [error] Type `::Object` does not have method `go_crazy_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal "#{num}!", go_crazy_in_if(num)
                                  ~~~~~~~~~~~~~~

nabeatsu/test/application_test.rb:8:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal "#{num}!", go_crazy_in_if(num)
          ~~~~~~~~~~~~

nabeatsu/test/application_test.rb:10:31: [error] Type `::Object` does not have method `go_crazy_in_if`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, go_crazy_in_if(num)
                                 ~~~~~~~~~~~~~~

nabeatsu/test/application_test.rb:10:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, go_crazy_in_if(num)
          ~~~~~~~~~~~~

nabeatsu/test/application_test.rb:18:32: [error] Type `::Object` does not have method `go_crazy_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal "#{num}!", go_crazy_in_ternary(num)
                                  ~~~~~~~~~~~~~~~~~~~

nabeatsu/test/application_test.rb:18:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal "#{num}!", go_crazy_in_ternary(num)
          ~~~~~~~~~~~~

nabeatsu/test/application_test.rb:20:31: [error] Type `::Object` does not have method `go_crazy_in_ternary`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, go_crazy_in_ternary(num)
                                 ~~~~~~~~~~~~~~~~~~~

nabeatsu/test/application_test.rb:20:8: [error] Type `::Object` does not have method `assert_equal`
│ Diagnostic ID: Ruby::NoMethod
│
└         assert_equal num.to_s, go_crazy_in_ternary(num)
          ~~~~~~~~~~~~

Detected 140 problems from 13 files
```
