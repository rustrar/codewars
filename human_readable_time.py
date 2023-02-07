"""
https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python
"""
import unittest


def make_readable(seconds):
    h = str(seconds // 3600)
    m = str((seconds % 3600) // 60)
    s = str((seconds % 3600) % 60)
    return f"{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}"

"""
best solution:
def make_readable(seconds):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
"""


class HumanReadableTime(unittest.TestCase):
    def test_make_readable(self):
        self.assertEqual("00:00:00", make_readable(0))
        self.assertEqual("00:00:05", make_readable(5))
        self.assertEqual("00:01:00", make_readable(60))
        self.assertEqual("23:59:59", make_readable(86399))
        self.assertEqual("99:59:59", make_readable(359999))
