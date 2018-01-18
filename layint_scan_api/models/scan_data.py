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


class ScanData(object):
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
        'parent_sid': 'str',
        'user_sid': 'str',
        'uri': 'str',
        'image_id': 'str',
        'date_created': 'str',
        'date_updated': 'str',
        'status': 'str',
        'events': 'list[ERRORUNKNOWN]',
        'clair': 'list[ClairData]'
    }

    attribute_map = {
        'sid': 'Sid',
        'parent_sid': 'ParentSid',
        'user_sid': 'UserSid',
        'uri': 'Uri',
        'image_id': 'ImageId',
        'date_created': 'DateCreated',
        'date_updated': 'DateUpdated',
        'status': 'Status',
        'events': 'Events',
        'clair': 'Clair'
    }

    def __init__(self, sid=None, parent_sid=None, user_sid=None, uri=None, image_id=None, date_created=None, date_updated=None, status=None, events=None, clair=None):
        """
        ScanData - a model defined in Swagger
        """

        self._sid = None
        self._parent_sid = None
        self._user_sid = None
        self._uri = None
        self._image_id = None
        self._date_created = None
        self._date_updated = None
        self._status = None
        self._events = None
        self._clair = None

        if sid is not None:
          self.sid = sid
        if parent_sid is not None:
          self.parent_sid = parent_sid
        if user_sid is not None:
          self.user_sid = user_sid
        if uri is not None:
          self.uri = uri
        if image_id is not None:
          self.image_id = image_id
        if date_created is not None:
          self.date_created = date_created
        if date_updated is not None:
          self.date_updated = date_updated
        if status is not None:
          self.status = status
        if events is not None:
          self.events = events
        if clair is not None:
          self.clair = clair

    @property
    def sid(self):
        """
        Gets the sid of this ScanData.
        Internal ID of this scan

        :return: The sid of this ScanData.
        :rtype: str
        """
        return self._sid

    @sid.setter
    def sid(self, sid):
        """
        Sets the sid of this ScanData.
        Internal ID of this scan

        :param sid: The sid of this ScanData.
        :type: str
        """

        self._sid = sid

    @property
    def parent_sid(self):
        """
        Gets the parent_sid of this ScanData.
        Internal ID of image that was scanned

        :return: The parent_sid of this ScanData.
        :rtype: str
        """
        return self._parent_sid

    @parent_sid.setter
    def parent_sid(self, parent_sid):
        """
        Sets the parent_sid of this ScanData.
        Internal ID of image that was scanned

        :param parent_sid: The parent_sid of this ScanData.
        :type: str
        """

        self._parent_sid = parent_sid

    @property
    def user_sid(self):
        """
        Gets the user_sid of this ScanData.
        ID of image owner

        :return: The user_sid of this ScanData.
        :rtype: str
        """
        return self._user_sid

    @user_sid.setter
    def user_sid(self, user_sid):
        """
        Sets the user_sid of this ScanData.
        ID of image owner

        :param user_sid: The user_sid of this ScanData.
        :type: str
        """

        self._user_sid = user_sid

    @property
    def uri(self):
        """
        Gets the uri of this ScanData.
        a

        :return: The uri of this ScanData.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this ScanData.
        a

        :param uri: The uri of this ScanData.
        :type: str
        """

        self._uri = uri

    @property
    def image_id(self):
        """
        Gets the image_id of this ScanData.
        Docker image ID

        :return: The image_id of this ScanData.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        """
        Sets the image_id of this ScanData.
        Docker image ID

        :param image_id: The image_id of this ScanData.
        :type: str
        """

        self._image_id = image_id

    @property
    def date_created(self):
        """
        Gets the date_created of this ScanData.
        Timestamp representing date scan was run

        :return: The date_created of this ScanData.
        :rtype: str
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """
        Sets the date_created of this ScanData.
        Timestamp representing date scan was run

        :param date_created: The date_created of this ScanData.
        :type: str
        """

        self._date_created = date_created

    @property
    def date_updated(self):
        """
        Gets the date_updated of this ScanData.
        Timestamp representing date this record was updated

        :return: The date_updated of this ScanData.
        :rtype: str
        """
        return self._date_updated

    @date_updated.setter
    def date_updated(self, date_updated):
        """
        Sets the date_updated of this ScanData.
        Timestamp representing date this record was updated

        :param date_updated: The date_updated of this ScanData.
        :type: str
        """

        self._date_updated = date_updated

    @property
    def status(self):
        """
        Gets the status of this ScanData.
        Status of scan

        :return: The status of this ScanData.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this ScanData.
        Status of scan

        :param status: The status of this ScanData.
        :type: str
        """

        self._status = status

    @property
    def events(self):
        """
        Gets the events of this ScanData.
        Log of events that occurred (or are occurring) during scan

        :return: The events of this ScanData.
        :rtype: list[ERRORUNKNOWN]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this ScanData.
        Log of events that occurred (or are occurring) during scan

        :param events: The events of this ScanData.
        :type: list[ERRORUNKNOWN]
        """

        self._events = events

    @property
    def clair(self):
        """
        Gets the clair of this ScanData.

        :return: The clair of this ScanData.
        :rtype: list[ClairData]
        """
        return self._clair

    @clair.setter
    def clair(self, clair):
        """
        Sets the clair of this ScanData.

        :param clair: The clair of this ScanData.
        :type: list[ClairData]
        """

        self._clair = clair

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
        if not isinstance(other, ScanData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other