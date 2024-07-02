#!/usr/bin/env python3
'''more of testing on file 2'''
from client import GithubOrgClient
import unittest
from typing import Sequence, Mapping, Any
from nose.tools import assert_equal
from parameterized import parameterized
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    '''Function starts with unittest.TestCase'''
    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json")
    def test_org(self, org_name: str, mock):
        '''testing org in client.py'''
        test_url = 'https://api.github.com/orgs/{}'.format(org_name)
        test_obj = GithubOrgClient(org_name)
        test_obj.org()
        mock.assert_called_once_with(test_url)

    def test_public_repos_url(self):
        '''testing public_repos in client.py'''
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mk:
            mk.return_value = {
                "repos_url": "https://api.github.com/users/abc/repos"
                }
            test_obj = GithubOrgClient("abc")._public_repos_url
            self.assertEqual(test_obj, mk.return_value["repos_url"])


if __name__ == '__main__':
    unittest.main()
