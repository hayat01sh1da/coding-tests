from application import fibonacci


class ApplicationTest:
    pass


class TestCase1(ApplicationTest):
    def test_fibonacci(self) -> None:
        assert fibonacci(init_num=0, iter=10) == \
            [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


class TestCase2(ApplicationTest):
    def test_fibonacci(self) -> None:
        assert fibonacci(init_num=10, iter=10) == \
            [10, 11, 21, 32, 53, 85, 138, 223, 361, 584]
