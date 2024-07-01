#!/usr/bin/env python3
'''working on parameterized.expand'''
import unittest
from utils import access_nested_map
from nose.tools import assert_equal
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    '''Function starts with parameterized.expand'''
    @parameterized.expand([
        ("test_1", {"a": 1}, ("a",), 1),
        ("test_2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("test_3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        '''Checks access_nested_map function'''
        assert_equal(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
