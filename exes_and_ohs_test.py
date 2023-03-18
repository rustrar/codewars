"""
https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python
"""
from collections import Counter
import unittest


def xo(s) -> bool:
    cnt = Counter(s.lower())
    return cnt['x'] == cnt['o']


"""
best solutions:
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
"""


class ExesAndOhs_test(unittest.TestCase):
    def test_exes_and_ohs(self) -> None:
        # self.assertEqual('1', range_extraction(1))
        self.assertTrue(xo('xo'))
        self.assertTrue(xo('xo0'))
        self.assertTrue(xo('XxOo0'))
        self.assertFalse(xo('xxxoo'))
