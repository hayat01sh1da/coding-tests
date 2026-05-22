from application import go_crazy_in_if, go_crazy_in_ternary


class ApplicationTest:
    def test_go_crazy_in_if_statement(self) -> None:
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                assert go_crazy_in_if(num) == f'{num}!'
            else:
                assert go_crazy_in_if(num) == str(num)

    def test_go_crazy_in_ternary_statement(self) -> None:
        for num in range(1, 41):
            if num % 3 == 0 or '3' in str(num):
                assert go_crazy_in_ternary(num) == f'{num}!'
            else:
                assert go_crazy_in_ternary(num) == str(num)
