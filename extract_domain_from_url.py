"""
https://www.codewars.com/kata/514a024011ea4fb54200004b/train/python
"""
import unittest


def domain_name(url):
    return url.removeprefix("http://").removeprefix("https://").removeprefix("www.").split(".")[0]


"""
best solutions:

def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
"""


class ExtractDomainFromUrl(unittest.TestCase):
    def test_domain_name(self):
        self.assertEqual("google", domain_name("http://google.com"))
        self.assertEqual("google", domain_name("http://google.co.jp"))
        self.assertEqual("xakep", domain_name("www.xakep.ru"))
        self.assertEqual("youtube", domain_name("https://youtube.com"))
