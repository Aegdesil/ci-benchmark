import unittest

from ci_benchmark.greeting import Greeting


class TestGreeting(unittest.TestCase):
    def setUp(self):
        self.greeting = Greeting("World")

    def test_greet(self):
        self.assertIn("World", self.greeting.greet())
