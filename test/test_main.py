"""Esse arquivo testa o arquivo main.py"""

import unittest  # for creating the test case
from main import fibonacci


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def test_fibonacci_relation(self):
        """Testa se o i-ésimo número de Fibonacci é igual a soma dos dois anteriores"""
        for i in range(3, 10):
            self.assertEqual(fibonacci(i), fibonacci(i - 1) + fibonacci(i - 2))

    def test_fibonacci_0(self):
        """Testa se o 0-ésimo número de Fibonacci é igual a 0"""
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_1(self):
        """Testa se o 1-ésimo número de Fibonacci é igual a 1"""
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_2(self):
        """Testa se o 2-ésimo número de Fibonacci é igual a 1"""
        self.assertEqual(fibonacci(2), 1)

    def test_fibonacci_3(self):
        """Testa se o 3-ésimo número de Fibonacci é igual a 2"""
        self.assertEqual(fibonacci(3), 2)
