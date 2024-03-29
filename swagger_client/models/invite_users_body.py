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


class InviteUsersBody(object):
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
        'emails': 'list[str]',
        'role': 'str'
    }

    attribute_map = {
        'emails': 'emails',
        'role': 'role'
    }

    def __init__(self, emails=None, role=None, _configuration=None):  # noqa: E501
        """InviteUsersBody - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._emails = None
        self._role = None
        self.discriminator = None

        self.emails = emails
        self.role = role

    @property
    def emails(self):
        """Gets the emails of this InviteUsersBody.  # noqa: E501

        List of emails  # noqa: E501

        :return: The emails of this InviteUsersBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._emails

    @emails.setter
    def emails(self, emails):
        """Sets the emails of this InviteUsersBody.

        List of emails  # noqa: E501

        :param emails: The emails of this InviteUsersBody.  # noqa: E501
        :type: list[str]
        """
        if self._configuration.client_side_validation and emails is None:
            raise ValueError("Invalid value for `emails`, must not be `None`")  # noqa: E501

        self._emails = emails

    @property
    def role(self):
        """Gets the role of this InviteUsersBody.  # noqa: E501

        User's role  # noqa: E501

        :return: The role of this InviteUsersBody.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InviteUsersBody.

        User's role  # noqa: E501

        :param role: The role of this InviteUsersBody.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        allowed_values = ["USER", "VIEWER", "ANNOTATOR", "ADMIN", "MANAGER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                role not in allowed_values):
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(InviteUsersBody, dict):
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
        if not isinstance(other, InviteUsersBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteUsersBody):
            return True

        return self.to_dict() != other.to_dict()
