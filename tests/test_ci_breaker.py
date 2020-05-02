import unittest

from ci_benchmark.ci_breaker import CIBreaker


class TestCIBreaker(unittest.TestCase):
    def setUp(self):
        self.ci_breaker = CIBreaker()

    def test_break(self):
        self.assertEqual("CIBreaker", self.ci_breaker.test_covered())
