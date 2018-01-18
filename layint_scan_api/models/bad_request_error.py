# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.1
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class BadRequestError(object):
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
        'code': 'int',
        'message': 'str',
        'message_info': 'str',
        'status': 'int'
    }

    attribute_map = {
        'code': 'Code',
        'message': 'Message',
        'message_info': 'MessageInfo',
        'status': 'Status'
    }

    def __init__(self, code=None, message=None, message_info=None, status=None):
        """
        BadRequestError - a model defined in Swagger
        """

        self._code = None
        self._message = None
        self._message_info = None
        self._status = None

        if code is not None:
          self.code = code
        if message is not None:
          self.message = message
        if message_info is not None:
          self.message_info = message_info
        if status is not None:
          self.status = status

    @property
    def code(self):
        """
        Gets the code of this BadRequestError.
        Internal Error code for lookup in documentation

        :return: The code of this BadRequestError.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this BadRequestError.
        Internal Error code for lookup in documentation

        :param code: The code of this BadRequestError.
        :type: int
        """

        self._code = code

    @property
    def message(self):
        """
        Gets the message of this BadRequestError.
        Short-form message describing error

        :return: The message of this BadRequestError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BadRequestError.
        Short-form message describing error

        :param message: The message of this BadRequestError.
        :type: str
        """

        self._message = message

    @property
    def message_info(self):
        """
        Gets the message_info of this BadRequestError.
        Long-form message describing error

        :return: The message_info of this BadRequestError.
        :rtype: str
        """
        return self._message_info

    @message_info.setter
    def message_info(self, message_info):
        """
        Sets the message_info of this BadRequestError.
        Long-form message describing error

        :param message_info: The message_info of this BadRequestError.
        :type: str
        """

        self._message_info = message_info

    @property
    def status(self):
        """
        Gets the status of this BadRequestError.
        HTTP status code

        :return: The status of this BadRequestError.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this BadRequestError.
        HTTP status code

        :param status: The status of this BadRequestError.
        :type: int
        """

        self._status = status

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
        if not isinstance(other, BadRequestError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
