"""
https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python
"""
import unittest

all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]


class RomanNumerals:
    @staticmethod
    def to_roman(val: int):
        roman = ''
        while val > 0:
            for i, r in all_roman:
                while val >= i:
                    roman += r
                    val -= i

        return roman


    @staticmethod
    def from_roman(roman_num: str):
        dec = 0
        for i, r in all_roman:
            while roman_num.startswith(r):
                dec += i
                roman_num = roman_num[len(r):]

        return dec

"""
best solutions:
class RomanNumerals:
    @staticmethod
    def to_roman(val: int):
        roman = ''
        while val > 0:
            for i, r in all_roman:
                while val >= i:
                    roman += r
                    val -= i

        return roman


    @staticmethod
    def from_roman(roman_num: str):
        dec = 0
        for i, r in all_roman:
            while roman_num.startswith(r):
                dec += i
                roman_num = roman_num[len(r):]

        return dec

"""


class ExtractDomainFromUrl(unittest.TestCase):
    def test_domain_name(self):
        self.assertEqual(1000, RomanNumerals.from_roman('M'))
        self.assertEqual(4, RomanNumerals.from_roman('IV'))
        self.assertEqual(1, RomanNumerals.from_roman('I'))
        self.assertEqual(1990, RomanNumerals.from_roman('MCMXC'))
        self.assertEqual(2008, RomanNumerals.from_roman('MMVIII'))

        self.assertEqual('M', RomanNumerals.to_roman(1000))
        self.assertEqual('IV', RomanNumerals.to_roman(4))
        self.assertEqual('I', RomanNumerals.to_roman(1))
        self.assertEqual('MCMXC', RomanNumerals.to_roman(1990))
        self.assertEqual('MMVIII', RomanNumerals.to_roman(2008))
