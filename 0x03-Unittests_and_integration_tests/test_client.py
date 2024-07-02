#!/usr/bin/env python3
'''more of testing on file 2'''
from client import GithubOrgClient
import unittest
from typing import Sequence, Mapping, Any
from nose.tools import assert_equal
from parameterized import parameterized
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    '''Function starts with unittest.TestCase'''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock):
        '''testing org in client.py'''
        test_obj = GithubOrgClient(org_name)
        test_obj.org()
        mock.assert_called_once_with(
            'https://api.github.com/orgs/{}'.format(org_name))


if __name__ == '__main__':
    unittest.main()
