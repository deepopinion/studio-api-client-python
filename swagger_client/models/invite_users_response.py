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


class InviteUsersResponse(object):
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
        'invitations': 'Invitations',
        'not_invited': 'list[InviteUsersResponseNotInvited]'
    }

    attribute_map = {
        'invitations': 'invitations',
        'not_invited': 'not_invited'
    }

    def __init__(self, invitations=None, not_invited=None, _configuration=None):  # noqa: E501
        """InviteUsersResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._invitations = None
        self._not_invited = None
        self.discriminator = None

        if invitations is not None:
            self.invitations = invitations
        if not_invited is not None:
            self.not_invited = not_invited

    @property
    def invitations(self):
        """Gets the invitations of this InviteUsersResponse.  # noqa: E501


        :return: The invitations of this InviteUsersResponse.  # noqa: E501
        :rtype: Invitations
        """
        return self._invitations

    @invitations.setter
    def invitations(self, invitations):
        """Sets the invitations of this InviteUsersResponse.


        :param invitations: The invitations of this InviteUsersResponse.  # noqa: E501
        :type: Invitations
        """

        self._invitations = invitations

    @property
    def not_invited(self):
        """Gets the not_invited of this InviteUsersResponse.  # noqa: E501

        List of users that were not invited  # noqa: E501

        :return: The not_invited of this InviteUsersResponse.  # noqa: E501
        :rtype: list[InviteUsersResponseNotInvited]
        """
        return self._not_invited

    @not_invited.setter
    def not_invited(self, not_invited):
        """Sets the not_invited of this InviteUsersResponse.

        List of users that were not invited  # noqa: E501

        :param not_invited: The not_invited of this InviteUsersResponse.  # noqa: E501
        :type: list[InviteUsersResponseNotInvited]
        """

        self._not_invited = not_invited

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
        if issubclass(InviteUsersResponse, dict):
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
        if not isinstance(other, InviteUsersResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InviteUsersResponse):
            return True

        return self.to_dict() != other.to_dict()
