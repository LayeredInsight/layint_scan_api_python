# coding: utf-8

"""
    Layered Insight Scan

    Layered Insight Scan performs static vulnerability analysis, license and package compliance.  You can find out more about Scan at http://layeredinsight.com.

    OpenAPI spec version: 0.9.3
    Contact: help@layeredinsight.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LicenseProduct(object):
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
        'assessment': 'bool',
        'compliance': 'bool',
        'witness': 'bool',
        'control': 'bool'
    }

    attribute_map = {
        'assessment': 'Assessment',
        'compliance': 'Compliance',
        'witness': 'Witness',
        'control': 'Control'
    }

    def __init__(self, assessment=False, compliance=False, witness=False, control=False):
        """
        LicenseProduct - a model defined in Swagger
        """

        self._assessment = None
        self._compliance = None
        self._witness = None
        self._control = None

        if assessment is not None:
          self.assessment = assessment
        if compliance is not None:
          self.compliance = compliance
        if witness is not None:
          self.witness = witness
        if control is not None:
          self.control = control

    @property
    def assessment(self):
        """
        Gets the assessment of this LicenseProduct.

        :return: The assessment of this LicenseProduct.
        :rtype: bool
        """
        return self._assessment

    @assessment.setter
    def assessment(self, assessment):
        """
        Sets the assessment of this LicenseProduct.

        :param assessment: The assessment of this LicenseProduct.
        :type: bool
        """

        self._assessment = assessment

    @property
    def compliance(self):
        """
        Gets the compliance of this LicenseProduct.

        :return: The compliance of this LicenseProduct.
        :rtype: bool
        """
        return self._compliance

    @compliance.setter
    def compliance(self, compliance):
        """
        Sets the compliance of this LicenseProduct.

        :param compliance: The compliance of this LicenseProduct.
        :type: bool
        """

        self._compliance = compliance

    @property
    def witness(self):
        """
        Gets the witness of this LicenseProduct.

        :return: The witness of this LicenseProduct.
        :rtype: bool
        """
        return self._witness

    @witness.setter
    def witness(self, witness):
        """
        Sets the witness of this LicenseProduct.

        :param witness: The witness of this LicenseProduct.
        :type: bool
        """

        self._witness = witness

    @property
    def control(self):
        """
        Gets the control of this LicenseProduct.

        :return: The control of this LicenseProduct.
        :rtype: bool
        """
        return self._control

    @control.setter
    def control(self, control):
        """
        Sets the control of this LicenseProduct.

        :param control: The control of this LicenseProduct.
        :type: bool
        """

        self._control = control

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
        if not isinstance(other, LicenseProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
