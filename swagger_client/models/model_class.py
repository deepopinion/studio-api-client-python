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


class ModelClass(object):
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
        'description': 'str',
        'example': 'str',
        'id': 'int',
        'name': 'str'
    }

    attribute_map = {
        'description': 'description',
        'example': 'example',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, description=None, example=None, id=None, name=None, _configuration=None):  # noqa: E501
        """ModelClass - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._example = None
        self._id = None
        self._name = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if example is not None:
            self.example = example
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def description(self):
        """Gets the description of this ModelClass.  # noqa: E501

        The class's description to help the annotator.  # noqa: E501

        :return: The description of this ModelClass.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelClass.

        The class's description to help the annotator.  # noqa: E501

        :param description: The description of this ModelClass.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def example(self):
        """Gets the example of this ModelClass.  # noqa: E501

        A usage example.  # noqa: E501

        :return: The example of this ModelClass.  # noqa: E501
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example):
        """Sets the example of this ModelClass.

        A usage example.  # noqa: E501

        :param example: The example of this ModelClass.  # noqa: E501
        :type: str
        """

        self._example = example

    @property
    def id(self):
        """Gets the id of this ModelClass.  # noqa: E501

        The ID of the label  # noqa: E501

        :return: The id of this ModelClass.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelClass.

        The ID of the label  # noqa: E501

        :param id: The id of this ModelClass.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelClass.  # noqa: E501

        The class's name.  # noqa: E501

        :return: The name of this ModelClass.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelClass.

        The class's name.  # noqa: E501

        :param name: The name of this ModelClass.  # noqa: E501
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
        if issubclass(ModelClass, dict):
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
        if not isinstance(other, ModelClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModelClass):
            return True

        return self.to_dict() != other.to_dict()
