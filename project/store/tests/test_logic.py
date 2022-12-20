from unittest import TestCase

from store.logic import operations


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(6, 13, '+')
        self.assertEqual(19, result)


    def test_minus(self):
        result = operations(6, 1, '-')
        self.assertEqual(5, result)


    def test_multi(self):
        result = operations(6, 5, '*')
        self.assertEqual(30, result)