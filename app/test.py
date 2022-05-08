#!/bin/python

from unittest.mock import patch
from main import parse_args
import unittest


class TestUtils(unittest.TestCase):

    def test_parser(self):
        parser = parse_args(['1', '2'])
        self.assertEqual(parser, 3)


if __name__ == '__main__':
    unittest.main()