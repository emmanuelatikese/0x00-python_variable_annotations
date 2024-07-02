#!/usr/bin/env python3
'''working on parameterized.expand'''
import unittest
from typing import Sequence, Mapping, Any
from nose.tools import assert_equal
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''Function starts with parameterized.expand'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any):
        '''Checks access_nested_map function'''
        assert_equal(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence):
        '''testing for errors'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''getting json class test'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: bool):
        '''testing get_json function'''
        with patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = test_payload
            assert_equal(get_json(test_url), test_payload)
            self.assertEqual(mock_get.call_count, 1)


class TestMemoize(unittest.TestCase):
    '''testing memoize decorator'''
    def test_memoize(self):
        '''memorizing decorator'''
        class TestClass:
            '''testing class'''
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as test:
            test_obj = TestClass()
            test_obj.a_property()
            test_obj.a_property()
            test.assert_called_once()


if __name__ == '__main__':
    unittest.main()
