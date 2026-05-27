class Application:
    @classmethod
    def exactly_equal_size_and_included(
            cls, source: str, target: str) -> bool:
        return cls(
            source=source,
            target=target)._exactly_equal_size_and_included()

    def __init__(self, source: str, target: str) -> None:
        self._source: str = source
        self._target: str = target

    # private

    def _exactly_equal_size_and_included(self) -> bool:
        return self._sort_string(self._source) == \
            self._sort_string(self._target)

    def _sort_string(self, string: str) -> str:
        return ''.join(sorted(string))
