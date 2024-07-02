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

    def test_public_repos_url(self) -> None:
        '''testing public_repos in client.py'''
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mk:
            mk.return_value = {
                "repos_url": "https://api.github.com/users/abc/repos"
                }
            test_obj = GithubOrgClient("abc")._public_repos_url
            self.assertEqual(test_obj, mk.return_value["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock):
        '''testing on public repositories'''
        payload_mk = [{"name": "abc"}, {"name": "google"}]
        mock.return_value = payload_mk
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as G_mock:
            G_mock.return_value = "https://api.github.com/orgs/abc/repos"
            test_obj = GithubOrgClient("abc")
            repo = test_obj.public_repos()
            self.assertEqual(repo, ["abc", "google"])

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        '''checking for license'''
        res = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(res, expected)


if __name__ == '__main__':
    unittest.main()
