# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.3
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import layint_scan_api
from layint_scan_api.rest import ApiException
from layint_scan_api.models.unauthorized_error import UnauthorizedError


class TestUnauthorizedError(unittest.TestCase):
    """ UnauthorizedError unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUnauthorizedError(self):
        """
        Test UnauthorizedError
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = layint_scan_api.models.unauthorized_error.UnauthorizedError()
        pass


if __name__ == '__main__':
    unittest.main()
