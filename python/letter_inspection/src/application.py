class Application:
    def __init__(self, str_1: str, str_2: str) -> None:
        self.str_1 = str_1
        self.str_2 = str_2

    def exactly_equal_size_and_included(self) -> bool:
        return self.__sort_string__(self.str_1) == self.__sort_string__(self.str_2)

    # private

    def __sort_string__(self, str: str) -> str:
        return ''.join(sorted(str))
