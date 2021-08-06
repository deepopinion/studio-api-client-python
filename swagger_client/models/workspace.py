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


class Workspace(object):
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
        'created': 'datetime',
        'description': 'str',
        'id': 'int',
        'is_beta': 'bool',
        'is_read_only': 'bool',
        'name': 'str'
    }

    attribute_map = {
        'created': 'created',
        'description': 'description',
        'id': 'id',
        'is_beta': 'is_beta',
        'is_read_only': 'is_read_only',
        'name': 'name'
    }

    def __init__(self, created=None, description=None, id=None, is_beta=None, is_read_only=None, name=None, _configuration=None):  # noqa: E501
        """Workspace - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._description = None
        self._id = None
        self._is_beta = None
        self._is_read_only = None
        self._name = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_beta is not None:
            self.is_beta = is_beta
        if is_read_only is not None:
            self.is_read_only = is_read_only
        if name is not None:
            self.name = name

    @property
    def created(self):
        """Gets the created of this Workspace.  # noqa: E501

        creation date  # noqa: E501

        :return: The created of this Workspace.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Workspace.

        creation date  # noqa: E501

        :param created: The created of this Workspace.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def description(self):
        """Gets the description of this Workspace.  # noqa: E501

        the description of the workspace  # noqa: E501

        :return: The description of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Workspace.

        the description of the workspace  # noqa: E501

        :param description: The description of this Workspace.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Workspace.  # noqa: E501

        The ID of the workspace.  # noqa: E501

        :return: The id of this Workspace.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Workspace.

        The ID of the workspace.  # noqa: E501

        :param id: The id of this Workspace.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_beta(self):
        """Gets the is_beta of this Workspace.  # noqa: E501

        if the workspace has beta features  # noqa: E501

        :return: The is_beta of this Workspace.  # noqa: E501
        :rtype: bool
        """
        return self._is_beta

    @is_beta.setter
    def is_beta(self, is_beta):
        """Sets the is_beta of this Workspace.

        if the workspace has beta features  # noqa: E501

        :param is_beta: The is_beta of this Workspace.  # noqa: E501
        :type: bool
        """

        self._is_beta = is_beta

    @property
    def is_read_only(self):
        """Gets the is_read_only of this Workspace.  # noqa: E501

        if the workspace is read-only  # noqa: E501

        :return: The is_read_only of this Workspace.  # noqa: E501
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """Sets the is_read_only of this Workspace.

        if the workspace is read-only  # noqa: E501

        :param is_read_only: The is_read_only of this Workspace.  # noqa: E501
        :type: bool
        """

        self._is_read_only = is_read_only

    @property
    def name(self):
        """Gets the name of this Workspace.  # noqa: E501

        The name of the workspace  # noqa: E501

        :return: The name of this Workspace.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Workspace.

        The name of the workspace  # noqa: E501

        :param name: The name of this Workspace.  # noqa: E501
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
        if issubclass(Workspace, dict):
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
        if not isinstance(other, Workspace):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Workspace):
            return True

        return self.to_dict() != other.to_dict()