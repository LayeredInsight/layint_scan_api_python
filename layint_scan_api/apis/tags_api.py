# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.3
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


class TagsApi(object):
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

    def add_tag(self, tag, **kwargs):
        """
        Add a tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_tag(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tag tag: Name of the tag to be added (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_tag_with_http_info(tag, **kwargs)
        else:
            (data) = self.add_tag_with_http_info(tag, **kwargs)
            return data

    def add_tag_with_http_info(self, tag, **kwargs):
        """
        Add a tag
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_tag_with_http_info(tag, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param Tag tag: Name of the tag to be added (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag' is set
        if ('tag' not in params) or (params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `add_tag`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tag' in params:
            body_params = params['tag']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['ApiKey']

        return self.api_client.call_api('/Tags', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_tag(self, tag_id, **kwargs):
        """
        Delete a tag by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tag(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: ID of tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_tag_with_http_info(tag_id, **kwargs)
        else:
            (data) = self.delete_tag_with_http_info(tag_id, **kwargs)
            return data

    def delete_tag_with_http_info(self, tag_id, **kwargs):
        """
        Delete a tag by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_tag_with_http_info(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: ID of tag to delete (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params) or (params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `delete_tag`")


        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagID'] = params['tag_id']

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

        return self.api_client.call_api('/Tags/{tagID}', 'DELETE',
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

    def get_tag(self, tag_id, **kwargs):
        """
        Get a tag by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: ID of tag to get (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tag_with_http_info(tag_id, **kwargs)
        else:
            (data) = self.get_tag_with_http_info(tag_id, **kwargs)
            return data

    def get_tag_with_http_info(self, tag_id, **kwargs):
        """
        Get a tag by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tag_with_http_info(tag_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str tag_id: ID of tag to get (required)
        :return: Tag
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_id' is set
        if ('tag_id' not in params) or (params['tag_id'] is None):
            raise ValueError("Missing the required parameter `tag_id` when calling `get_tag`")


        collection_formats = {}

        path_params = {}
        if 'tag_id' in params:
            path_params['tagID'] = params['tag_id']

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

        return self.api_client.call_api('/Tags/{tagID}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tag',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tags(self, **kwargs):
        """
        List all tags
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tags(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Tags
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tags_with_http_info(**kwargs)
        else:
            (data) = self.get_tags_with_http_info(**kwargs)
            return data

    def get_tags_with_http_info(self, **kwargs):
        """
        List all tags
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tags_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: Tags
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
                    " to method get_tags" % key
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

        return self.api_client.call_api('/Tags', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Tags',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
