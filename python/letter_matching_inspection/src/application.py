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

    def _exactly_equal_size_and_included(self) -> bool:
        return self._sort_string(
            self._source) == self._sort_string(
            self._target)

    # private

    def _sort_string(self, str: str) -> str:
        return ''.join(sorted(str))
