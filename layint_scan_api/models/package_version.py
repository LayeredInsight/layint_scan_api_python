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


class PackageVersion(object):
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
        'pkg': 'str',
        'ver': 'str'
    }

    attribute_map = {
        'pkg': 'Pkg',
        'ver': 'Ver'
    }

    def __init__(self, pkg=None, ver=None):
        """
        PackageVersion - a model defined in Swagger
        """

        self._pkg = None
        self._ver = None

        if pkg is not None:
          self.pkg = pkg
        if ver is not None:
          self.ver = ver

    @property
    def pkg(self):
        """
        Gets the pkg of this PackageVersion.
        Name of software package

        :return: The pkg of this PackageVersion.
        :rtype: str
        """
        return self._pkg

    @pkg.setter
    def pkg(self, pkg):
        """
        Sets the pkg of this PackageVersion.
        Name of software package

        :param pkg: The pkg of this PackageVersion.
        :type: str
        """

        self._pkg = pkg

    @property
    def ver(self):
        """
        Gets the ver of this PackageVersion.
        Version of software package

        :return: The ver of this PackageVersion.
        :rtype: str
        """
        return self._ver

    @ver.setter
    def ver(self, ver):
        """
        Sets the ver of this PackageVersion.
        Version of software package

        :param ver: The ver of this PackageVersion.
        :type: str
        """

        self._ver = ver

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
        if not isinstance(other, PackageVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
