import json
import os
import urllib.parse
import urllib.request


class CalculationQuery:
    def __init__(self, seed: str) -> None:
        self._seed: str = seed

    def f(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 2:
            return 2
        elif n % 2 == 0:
            return self.f(n - 1) + self.f(n - 2) + \
                self.f(n - 3) + self.f(n - 4)
        else:
            return self._ask_server(n)

    # private

    @property
    def _uri(self) -> str:
        if not hasattr(self, '_cached_uri'):
            self._cached_uri: str = os.environ['CALCULATION_API']
        return self._cached_uri

    def _ask_server(self, n: int) -> int:
        params = {'seed': self._seed, 'n': n}
        req = urllib.request.Request(
            f'{self._uri}?{urllib.parse.urlencode(params)}')
        res = urllib.request.urlopen(req)
        result: int = json.loads(res.read())['result']
        return result
