# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.4
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class TokenResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auth_token': 'str',
        'expires_in': 'int',
        'existing_user': 'bool',
        'identity': 'str',
        'uri': 'str'
    }

    attribute_map = {
        'auth_token': 'AuthToken',
        'expires_in': 'ExpiresIn',
        'existing_user': 'ExistingUser',
        'identity': 'Identity',
        'uri': 'Uri'
    }

    def __init__(self, auth_token=None, expires_in=None, existing_user=None, identity=None, uri=None):
        """
        TokenResponse - a model defined in Swagger
        """

        self._auth_token = None
        self._expires_in = None
        self._existing_user = None
        self._identity = None
        self._uri = None

        if auth_token is not None:
          self.auth_token = auth_token
        if expires_in is not None:
          self.expires_in = expires_in
        if existing_user is not None:
          self.existing_user = existing_user
        if identity is not None:
          self.identity = identity
        if uri is not None:
          self.uri = uri

    @property
    def auth_token(self):
        """
        Gets the auth_token of this TokenResponse.
        Authentication token to use for this session

        :return: The auth_token of this TokenResponse.
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """
        Sets the auth_token of this TokenResponse.
        Authentication token to use for this session

        :param auth_token: The auth_token of this TokenResponse.
        :type: str
        """

        self._auth_token = auth_token

    @property
    def expires_in(self):
        """
        Gets the expires_in of this TokenResponse.
        Expiration time of token, in seconds since epoch

        :return: The expires_in of this TokenResponse.
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """
        Sets the expires_in of this TokenResponse.
        Expiration time of token, in seconds since epoch

        :param expires_in: The expires_in of this TokenResponse.
        :type: int
        """

        self._expires_in = expires_in

    @property
    def existing_user(self):
        """
        Gets the existing_user of this TokenResponse.
        True if this was not user's first login

        :return: The existing_user of this TokenResponse.
        :rtype: bool
        """
        return self._existing_user

    @existing_user.setter
    def existing_user(self, existing_user):
        """
        Sets the existing_user of this TokenResponse.
        True if this was not user's first login

        :param existing_user: The existing_user of this TokenResponse.
        :type: bool
        """

        self._existing_user = existing_user

    @property
    def identity(self):
        """
        Gets the identity of this TokenResponse.

        :return: The identity of this TokenResponse.
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """
        Sets the identity of this TokenResponse.

        :param identity: The identity of this TokenResponse.
        :type: str
        """

        self._identity = identity

    @property
    def uri(self):
        """
        Gets the uri of this TokenResponse.
        URI to resource, usually the URI that generated this Response

        :return: The uri of this TokenResponse.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this TokenResponse.
        URI to resource, usually the URI that generated this Response

        :param uri: The uri of this TokenResponse.
        :type: str
        """

        self._uri = uri

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, TokenResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
