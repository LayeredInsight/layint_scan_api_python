# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.4
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import layint_scan_api
from layint_scan_api.rest import ApiException
from layint_scan_api.apis.authentication_api import AuthenticationApi


class TestAuthenticationApi(unittest.TestCase):
    """ AuthenticationApi unit test stubs """

    def setUp(self):
        self.api = layint_scan_api.apis.authentication_api.AuthenticationApi()

    def tearDown(self):
        pass

    def test_login(self):
        """
        Test case for login

        Processes local login request
        """
        pass

    def test_token_request(self):
        """
        Test case for token_request

        Returns a session token for a oauth2 token
        """
        pass


if __name__ == '__main__':
    unittest.main()
