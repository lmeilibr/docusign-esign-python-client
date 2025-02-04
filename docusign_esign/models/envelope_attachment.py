# coding: utf-8

"""
    DocuSign REST API

    The DocuSign REST API provides you with a powerful, convenient, and simple Web services API for interacting with DocuSign.  # noqa: E501

    OpenAPI spec version: v2.1
    Contact: devcenter@docusign.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from docusign_esign.client.configuration import Configuration


class EnvelopeAttachment(object):
    """NOTE: This class is auto generated by the swagger code generator program.

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
        'access_control': 'str',
        'attachment_id': 'str',
        'attachment_type': 'str',
        'error_details': 'ErrorDetails',
        'label': 'str',
        'name': 'str'
    }

    attribute_map = {
        'access_control': 'accessControl',
        'attachment_id': 'attachmentId',
        'attachment_type': 'attachmentType',
        'error_details': 'errorDetails',
        'label': 'label',
        'name': 'name'
    }

    def __init__(self, _configuration=None, **kwargs):  # noqa: E501
        """EnvelopeAttachment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_control = None
        self._attachment_id = None
        self._attachment_type = None
        self._error_details = None
        self._label = None
        self._name = None
        self.discriminator = None

        setattr(self, "_{}".format('access_control'), kwargs.get('access_control', None))
        setattr(self, "_{}".format('attachment_id'), kwargs.get('attachment_id', None))
        setattr(self, "_{}".format('attachment_type'), kwargs.get('attachment_type', None))
        setattr(self, "_{}".format('error_details'), kwargs.get('error_details', None))
        setattr(self, "_{}".format('label'), kwargs.get('label', None))
        setattr(self, "_{}".format('name'), kwargs.get('name', None))

    @property
    def access_control(self):
        """Gets the access_control of this EnvelopeAttachment.  # noqa: E501

          # noqa: E501

        :return: The access_control of this EnvelopeAttachment.  # noqa: E501
        :rtype: str
        """
        return self._access_control

    @access_control.setter
    def access_control(self, access_control):
        """Sets the access_control of this EnvelopeAttachment.

          # noqa: E501

        :param access_control: The access_control of this EnvelopeAttachment.  # noqa: E501
        :type: str
        """

        self._access_control = access_control

    @property
    def attachment_id(self):
        """Gets the attachment_id of this EnvelopeAttachment.  # noqa: E501

          # noqa: E501

        :return: The attachment_id of this EnvelopeAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_id

    @attachment_id.setter
    def attachment_id(self, attachment_id):
        """Sets the attachment_id of this EnvelopeAttachment.

          # noqa: E501

        :param attachment_id: The attachment_id of this EnvelopeAttachment.  # noqa: E501
        :type: str
        """

        self._attachment_id = attachment_id

    @property
    def attachment_type(self):
        """Gets the attachment_type of this EnvelopeAttachment.  # noqa: E501

          # noqa: E501

        :return: The attachment_type of this EnvelopeAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """Sets the attachment_type of this EnvelopeAttachment.

          # noqa: E501

        :param attachment_type: The attachment_type of this EnvelopeAttachment.  # noqa: E501
        :type: str
        """

        self._attachment_type = attachment_type

    @property
    def error_details(self):
        """Gets the error_details of this EnvelopeAttachment.  # noqa: E501

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :return: The error_details of this EnvelopeAttachment.  # noqa: E501
        :rtype: ErrorDetails
        """
        return self._error_details

    @error_details.setter
    def error_details(self, error_details):
        """Sets the error_details of this EnvelopeAttachment.

        This object describes errors that occur. It is only valid for responses and ignored in requests.  # noqa: E501

        :param error_details: The error_details of this EnvelopeAttachment.  # noqa: E501
        :type: ErrorDetails
        """

        self._error_details = error_details

    @property
    def label(self):
        """Gets the label of this EnvelopeAttachment.  # noqa: E501

          # noqa: E501

        :return: The label of this EnvelopeAttachment.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this EnvelopeAttachment.

          # noqa: E501

        :param label: The label of this EnvelopeAttachment.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def name(self):
        """Gets the name of this EnvelopeAttachment.  # noqa: E501

          # noqa: E501

        :return: The name of this EnvelopeAttachment.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvelopeAttachment.

          # noqa: E501

        :param name: The name of this EnvelopeAttachment.  # noqa: E501
        :type: str
        """

        self._name = name

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EnvelopeAttachment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EnvelopeAttachment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EnvelopeAttachment):
            return True

        return self.to_dict() != other.to_dict()
