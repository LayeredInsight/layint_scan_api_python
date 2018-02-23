# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.2
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class RegistryApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_ecr_creds(self, ecr_credentials, **kwargs):
        """
        Add credentials for AWS ECR
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_ecr_creds(ecr_credentials, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EcrCredentials ecr_credentials: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_ecr_creds_with_http_info(ecr_credentials, **kwargs)
        else:
            (data) = self.add_ecr_creds_with_http_info(ecr_credentials, **kwargs)
            return data

    def add_ecr_creds_with_http_info(self, ecr_credentials, **kwargs):
        """
        Add credentials for AWS ECR
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_ecr_creds_with_http_info(ecr_credentials, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EcrCredentials ecr_credentials: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ecr_credentials']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_ecr_creds" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ecr_credentials' is set
        if ('ecr_credentials' not in params) or (params['ecr_credentials'] is None):
            raise ValueError("Missing the required parameter `ecr_credentials` when calling `add_ecr_creds`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ecr_credentials' in params:
            body_params = params['ecr_credentials']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/EcrCreds', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def add_registry(self, registry, **kwargs):
        """
        Add a new registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_registry(registry, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Registry registry: Registry object to be added (required)
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_registry_with_http_info(registry, **kwargs)
        else:
            (data) = self.add_registry_with_http_info(registry, **kwargs)
            return data

    def add_registry_with_http_info(self, registry, **kwargs):
        """
        Add a new registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_registry_with_http_info(registry, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Registry registry: Registry object to be added (required)
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_registry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registry' is set
        if ('registry' not in params) or (params['registry'] is None):
            raise ValueError("Missing the required parameter `registry` when calling `add_registry`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'registry' in params:
            body_params = params['registry']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Registry', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Registry',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_registry(self, registry_id, **kwargs):
        """
        Deletes a registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_registry(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: Registry id to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_registry_with_http_info(registry_id, **kwargs)
        else:
            (data) = self.delete_registry_with_http_info(registry_id, **kwargs)
            return data

    def delete_registry_with_http_info(self, registry_id, **kwargs):
        """
        Deletes a registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_registry_with_http_info(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: Registry id to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_registry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registry_id' is set
        if ('registry_id' not in params) or (params['registry_id'] is None):
            raise ValueError("Missing the required parameter `registry_id` when calling `delete_registry`")


        collection_formats = {}

        path_params = {}
        if 'registry_id' in params:
            path_params['registryId'] = params['registry_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Registry/{registryId}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_registries(self, **kwargs):
        """
        List all registries available to the user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_registries(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Registries
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_registries_with_http_info(**kwargs)
        else:
            (data) = self.get_registries_with_http_info(**kwargs)
            return data

    def get_registries_with_http_info(self, **kwargs):
        """
        List all registries available to the user
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_registries_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Registries
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_registries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Registry', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Registries',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_registry_by_id(self, registry_id, **kwargs):
        """
        Find registry by ID
        Returns a single registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_registry_by_id(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: ID of registry to return (required)
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_registry_by_id_with_http_info(registry_id, **kwargs)
        else:
            (data) = self.get_registry_by_id_with_http_info(registry_id, **kwargs)
            return data

    def get_registry_by_id_with_http_info(self, registry_id, **kwargs):
        """
        Find registry by ID
        Returns a single registry
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_registry_by_id_with_http_info(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: ID of registry to return (required)
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_registry_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registry_id' is set
        if ('registry_id' not in params) or (params['registry_id'] is None):
            raise ValueError("Missing the required parameter `registry_id` when calling `get_registry_by_id`")


        collection_formats = {}

        path_params = {}
        if 'registry_id' in params:
            path_params['registryId'] = params['registry_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Registry/{registryId}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Registry',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_registry(self, registry_id, **kwargs):
        """
        Updates a registry with form data
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_registry(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: ID of registry that needs to be updated (required)
        :param str name: Updated name of the registry
        :param str url: Updated URL for the registry
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_registry_with_http_info(registry_id, **kwargs)
        else:
            (data) = self.update_registry_with_http_info(registry_id, **kwargs)
            return data

    def update_registry_with_http_info(self, registry_id, **kwargs):
        """
        Updates a registry with form data
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_registry_with_http_info(registry_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int registry_id: ID of registry that needs to be updated (required)
        :param str name: Updated name of the registry
        :param str url: Updated URL for the registry
        :return: Registry
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['registry_id', 'name', 'url']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_registry" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'registry_id' is set
        if ('registry_id' not in params) or (params['registry_id'] is None):
            raise ValueError("Missing the required parameter `registry_id` when calling `update_registry`")


        collection_formats = {}

        path_params = {}
        if 'registry_id' in params:
            path_params['registryId'] = params['registry_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'name' in params:
            form_params.append(('name', params['name']))
        if 'url' in params:
            form_params.append(('url', params['url']))

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/x-www-form-urlencoded'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Registry/{registryId}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Registry',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
