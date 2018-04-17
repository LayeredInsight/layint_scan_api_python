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


class Policy(object):
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
        'sid': 'str',
        'user_sid': 'str',
        'uri': 'str',
        'date_created': 'str',
        'date_updated': 'str',
        'name': 'str',
        'rules_id': 'list[str]',
        'rules': 'list[PolicyRule]'
    }

    attribute_map = {
        'sid': 'Sid',
        'user_sid': 'UserSid',
        'uri': 'Uri',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated',
        'name': 'Name',
        'rules_id': 'RulesId',
        'rules': 'Rules'
    }

    def __init__(self, sid=None, user_sid=None, uri=None, date_created=None, date_updated=None, name=None, rules_id=None, rules=None):
        """
        Policy - a model defined in Swagger
        """

        self._sid = None
        self._user_sid = None
        self._uri = None
        self._date_created = None
        self._date_updated = None
        self._name = None
        self._rules_id = None
        self._rules = None

        if sid is not None:
          self.sid = sid
        if user_sid is not None:
          self.user_sid = user_sid
        if uri is not None:
          self.uri = uri
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated
        if name is not None:
          self.name = name
        if rules_id is not None:
          self.rules_id = rules_id
        if rules is not None:
          self.rules = rules

    @property
    def sid(self):
        """
        Gets the sid of this Policy.
        ID for this rule

        :return: The sid of this Policy.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this Policy.
        ID for this rule

        :param sid: The sid of this Policy.
        :type: str
        """

        self._sid = sid

    @property
    def user_sid(self):
        """
        Gets the user_sid of this Policy.
        ID of owner of this rule

        :return: The user_sid of this Policy.
        :rtype: str
        """
        return self._user_sid

    @user_sid.setter
    def user_sid(self, user_sid):
        """
        Sets the user_sid of this Policy.
        ID of owner of this rule

        :param user_sid: The user_sid of this Policy.
        :type: str
        """

        self._user_sid = user_sid

    @property
    def uri(self):
        """
        Gets the uri of this Policy.

        :return: The uri of this Policy.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Policy.

        :param uri: The uri of this Policy.
        :type: str
        """

        self._uri = uri

    @property
    def date_created(self):
        """
        Gets the date_created of this Policy.
        Timestamp representing date scan was run

        :return: The date_created of this Policy.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this Policy.
        Timestamp representing date scan was run

        :param date_created: The date_created of this Policy.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this Policy.
        Timestamp representing date this record was updated

        :return: The date_updated of this Policy.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this Policy.
        Timestamp representing date this record was updated

        :param date_updated: The date_updated of this Policy.
        :type: str
        """

        self._date_updated = date_updated

    @property
    def name(self):
        """
        Gets the name of this Policy.
        Name of this policy

        :return: The name of this Policy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Policy.
        Name of this policy

        :param name: The name of this Policy.
        :type: str
        """

        self._name = name

    @property
    def rules_id(self):
        """
        Gets the rules_id of this Policy.
        List of IDs of the rules in this policy

        :return: The rules_id of this Policy.
        :rtype: list[str]
        """
        return self._rules_id

    @rules_id.setter
    def rules_id(self, rules_id):
        """
        Sets the rules_id of this Policy.
        List of IDs of the rules in this policy

        :param rules_id: The rules_id of this Policy.
        :type: list[str]
        """

        self._rules_id = rules_id

    @property
    def rules(self):
        """
        Gets the rules of this Policy.

        :return: The rules of this Policy.
        :rtype: list[PolicyRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this Policy.

        :param rules: The rules of this Policy.
        :type: list[PolicyRule]
        """

        self._rules = rules

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
        if not isinstance(other, Policy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
