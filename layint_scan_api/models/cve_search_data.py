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


class CveSearchData(object):
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
        'limit': 'int',
        'cvss_score': 'float',
        'tags': 'list[str]'
    }

    attribute_map = {
        'limit': 'Limit',
        'cvss_score': 'CvssScore',
        'tags': 'Tags'
    }

    def __init__(self, limit=None, cvss_score=None, tags=None):
        """
        CveSearchData - a model defined in Swagger
        """

        self._limit = None
        self._cvss_score = None
        self._tags = None

        if limit is not None:
          self.limit = limit
        if cvss_score is not None:
          self.cvss_score = cvss_score
        if tags is not None:
          self.tags = tags

    @property
    def limit(self):
        """
        Gets the limit of this CveSearchData.

        :return: The limit of this CveSearchData.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this CveSearchData.

        :param limit: The limit of this CveSearchData.
        :type: int
        """

        self._limit = limit

    @property
    def cvss_score(self):
        """
        Gets the cvss_score of this CveSearchData.
        Mininum CVSS score to consider (between 0-10.0)

        :return: The cvss_score of this CveSearchData.
        :rtype: float
        """
        return self._cvss_score

    @cvss_score.setter
    def cvss_score(self, cvss_score):
        """
        Sets the cvss_score of this CveSearchData.
        Mininum CVSS score to consider (between 0-10.0)

        :param cvss_score: The cvss_score of this CveSearchData.
        :type: float
        """

        self._cvss_score = cvss_score

    @property
    def tags(self):
        """
        Gets the tags of this CveSearchData.
        Filter vulnerable images based on tag names

        :return: The tags of this CveSearchData.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this CveSearchData.
        Filter vulnerable images based on tag names

        :param tags: The tags of this CveSearchData.
        :type: list[str]
        """

        self._tags = tags

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
        if not isinstance(other, CveSearchData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
