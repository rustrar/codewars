"""
https://www.codewars.com/kata/513e08acc600c94f01000001/train/python
"""

import unittest


def to_hex(s):
    return hex(s).removeprefix('0x').upper()


def rgb(r, g, b) -> str:
    r, g, b = [255 if s > 255 else 0 if s < 0 else s for s in (r, g, b)]
    return f"{to_hex(r).zfill(2)}{to_hex(g).zfill(2)}{to_hex(b).zfill(2)}"


"""
best solution:

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))
"""


class RGBToHexConversion(unittest.TestCase):
    def test_rgb(self):
        self.assertEqual(rgb(0, 0, 0), "000000")
        self.assertEqual(rgb(1, 2, 3), "010203")
        self.assertEqual("FFFFFF", rgb(255, 255, 255))
        self.assertEqual("FEFDFC", rgb(254, 253, 252))
        self.assertEqual("00FF7D", rgb(-20, 275, 125))
