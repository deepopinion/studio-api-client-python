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


class FilePreview(object):
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
        'id': 'str',
        'preview': 'list[list[str]]'
    }

    attribute_map = {
        'id': 'id',
        'preview': 'preview'
    }

    def __init__(self, id=None, preview=None, _configuration=None):  # noqa: E501
        """FilePreview - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._id = None
        self._preview = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if preview is not None:
            self.preview = preview

    @property
    def id(self):
        """Gets the id of this FilePreview.  # noqa: E501

        The unique ID of the uploaded file.  # noqa: E501

        :return: The id of this FilePreview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FilePreview.

        The unique ID of the uploaded file.  # noqa: E501

        :param id: The id of this FilePreview.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def preview(self):
        """Gets the preview of this FilePreview.  # noqa: E501

        A preview of the columns found in that file. The first element represents the header, if present.  # noqa: E501

        :return: The preview of this FilePreview.  # noqa: E501
        :rtype: list[list[str]]
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this FilePreview.

        A preview of the columns found in that file. The first element represents the header, if present.  # noqa: E501

        :param preview: The preview of this FilePreview.  # noqa: E501
        :type: list[list[str]]
        """

        self._preview = preview

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
        if issubclass(FilePreview, dict):
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
        if not isinstance(other, FilePreview):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FilePreview):
            return True

        return self.to_dict() != other.to_dict()
