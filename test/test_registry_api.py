# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.1
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import layint_scan_api
from layint_scan_api.rest import ApiException
from layint_scan_api.apis.registry_api import RegistryApi


class TestRegistryApi(unittest.TestCase):
    """ RegistryApi unit test stubs """

    def setUp(self):
        self.api = layint_scan_api.apis.registry_api.RegistryApi()

    def tearDown(self):
        pass

    def test_add_ecr_creds(self):
        """
        Test case for add_ecr_creds

        Add credentials for AWS ECR
        """
        pass

    def test_add_registry(self):
        """
        Test case for add_registry

        Add a new registry
        """
        pass

    def test_delete_registry(self):
        """
        Test case for delete_registry

        Deletes a registry
        """
        pass

    def test_get_registries(self):
        """
        Test case for get_registries

        List all registries available to the user
        """
        pass

    def test_get_registry_by_id(self):
        """
        Test case for get_registry_by_id

        Find registry by ID
        """
        pass

    def test_update_registry(self):
        """
        Test case for update_registry

        Updates a registry with form data
        """
        pass


if __name__ == '__main__':
    unittest.main()
