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


class LoginResponse(object):
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
        'auth_token': 'str',
        'message': 'str',
        'status': 'str'
    }

    attribute_map = {
        'auth_token': 'auth_token',
        'message': 'message',
        'status': 'status'
    }

    def __init__(self, auth_token=None, message=None, status=None, _configuration=None):  # noqa: E501
        """LoginResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auth_token = None
        self._message = None
        self._status = None
        self.discriminator = None

        if auth_token is not None:
            self.auth_token = auth_token
        if message is not None:
            self.message = message
        if status is not None:
            self.status = status

    @property
    def auth_token(self):
        """Gets the auth_token of this LoginResponse.  # noqa: E501

        A token that should be use to authenticate the requests  # noqa: E501

        :return: The auth_token of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._auth_token

    @auth_token.setter
    def auth_token(self, auth_token):
        """Sets the auth_token of this LoginResponse.

        A token that should be use to authenticate the requests  # noqa: E501

        :param auth_token: The auth_token of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._auth_token = auth_token

    @property
    def message(self):
        """Gets the message of this LoginResponse.  # noqa: E501


        :return: The message of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LoginResponse.


        :param message: The message of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this LoginResponse.  # noqa: E501


        :return: The status of this LoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this LoginResponse.


        :param status: The status of this LoginResponse.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(LoginResponse, dict):
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
        if not isinstance(other, LoginResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LoginResponse):
            return True

        return self.to_dict() != other.to_dict()
