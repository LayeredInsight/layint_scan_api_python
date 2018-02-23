# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.2
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class ClairData(object):
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
        'layer': 'list[ClairLayer]',
        'error': 'str'
    }

    attribute_map = {
        'layer': 'Layer',
        'error': 'Error'
    }

    def __init__(self, layer=None, error=None):
        """
        ClairData - a model defined in Swagger
        """

        self._layer = None
        self._error = None

        if layer is not None:
          self.layer = layer
        if error is not None:
          self.error = error

    @property
    def layer(self):
        """
        Gets the layer of this ClairData.

        :return: The layer of this ClairData.
        :rtype: list[ClairLayer]
        """
        return self._layer

    @layer.setter
    def layer(self, layer):
        """
        Sets the layer of this ClairData.

        :param layer: The layer of this ClairData.
        :type: list[ClairLayer]
        """

        self._layer = layer

    @property
    def error(self):
        """
        Gets the error of this ClairData.
        Any errors encountered while scanning this layer of the container image

        :return: The error of this ClairData.
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """
        Sets the error of this ClairData.
        Any errors encountered while scanning this layer of the container image

        :param error: The error of this ClairData.
        :type: str
        """

        self._error = error

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
        if not isinstance(other, ClairData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
