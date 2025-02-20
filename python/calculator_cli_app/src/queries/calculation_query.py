import urllib.request
import os
import json

class CalculationQuery:
    def __init__(self, seed):
        self.seed = seed
        self.uri  = None

    def f(self, n):
        if n == 0:
            return 1
        elif n == 2:
            return 2
        elif n % 2 == 0:
            return self.f(n - 1) + self.f(n - 2) + self.f(n - 3) + self.f(n - 4)
        else:
            return self.__ask_server__(n)

  # private

    def __uri__(self):
        if self.uri:
            return self.uri
        else:
            self.uri = os.environ['CALCULATION_API']
            return self.uri

    def __ask_server__(self, n):
        params = { 'seed': self.seed, 'n': n }
        req    = urllib.request.Request('{}?{}'.format(self.__uri__(), urllib.parse.urlencode(params)))
        res    = urllib.request.urlopen(req)
        result = json.loads(res.read())['result']
        return result
