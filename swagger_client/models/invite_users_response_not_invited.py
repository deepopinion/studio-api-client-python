# coding: utf-8

"""
    Studio API

    Studio API  # noqa: E501

    OpenAPI spec version: 1.6.2 
    Contact: support@deepopinion.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class InviteUsersResponseNotInvited(object):
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
        'email': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'email': 'email',
        'reason': 'reason'
    }

    def __init__(self, email=None, reason=None, _configuration=None):  # noqa: E501
        """InviteUsersResponseNotInvited - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._email = None
        self._reason = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if reason is not None:
            self.reason = reason

    @property
    def email(self):
        """Gets the email of this InviteUsersResponseNotInvited.  # noqa: E501

        Invited email  # noqa: E501

        :return: The email of this InviteUsersResponseNotInvited.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this InviteUsersResponseNotInvited.

        Invited email  # noqa: E501

        :param email: The email of this InviteUsersResponseNotInvited.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def reason(self):
        """Gets the reason of this InviteUsersResponseNotInvited.  # noqa: E501

        The reason why invitation failed  # noqa: E501

        :return: The reason of this InviteUsersResponseNotInvited.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this InviteUsersResponseNotInvited.

        The reason why invitation failed  # noqa: E501

        :param reason: The reason of this InviteUsersResponseNotInvited.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(InviteUsersResponseNotInvited, dict):
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
        if not isinstance(other, InviteUsersResponseNotInvited):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteUsersResponseNotInvited):
            return True

        return self.to_dict() != other.to_dict()
