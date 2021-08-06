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


class ProjectTagsResponse(object):
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
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'tags': 'ClassLabelTags',
        'total': 'int'
    }

    attribute_map = {
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'tags': 'tags',
        'total': 'total'
    }

    def __init__(self, count=None, limit=None, offset=None, tags=None, total=None, _configuration=None):  # noqa: E501
        """ProjectTagsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._count = None
        self._limit = None
        self._offset = None
        self._tags = None
        self._total = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if tags is not None:
            self.tags = tags
        if total is not None:
            self.total = total

    @property
    def count(self):
        """Gets the count of this ProjectTagsResponse.  # noqa: E501

        Number of objects returned  # noqa: E501

        :return: The count of this ProjectTagsResponse.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ProjectTagsResponse.

        Number of objects returned  # noqa: E501

        :param count: The count of this ProjectTagsResponse.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def limit(self):
        """Gets the limit of this ProjectTagsResponse.  # noqa: E501

        Limit of entries that should be returned.  # noqa: E501

        :return: The limit of this ProjectTagsResponse.  # noqa: E501
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ProjectTagsResponse.

        Limit of entries that should be returned.  # noqa: E501

        :param limit: The limit of this ProjectTagsResponse.  # noqa: E501
        :type: int
        """

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ProjectTagsResponse.  # noqa: E501

        An offset is simply the number of records you wish to skip before selecting records.  # noqa: E501

        :return: The offset of this ProjectTagsResponse.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ProjectTagsResponse.

        An offset is simply the number of records you wish to skip before selecting records.  # noqa: E501

        :param offset: The offset of this ProjectTagsResponse.  # noqa: E501
        :type: int
        """

        self._offset = offset

    @property
    def tags(self):
        """Gets the tags of this ProjectTagsResponse.  # noqa: E501


        :return: The tags of this ProjectTagsResponse.  # noqa: E501
        :rtype: ClassLabelTags
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ProjectTagsResponse.


        :param tags: The tags of this ProjectTagsResponse.  # noqa: E501
        :type: ClassLabelTags
        """

        self._tags = tags

    @property
    def total(self):
        """Gets the total of this ProjectTagsResponse.  # noqa: E501

        Deprecated. Total of tags  # noqa: E501

        :return: The total of this ProjectTagsResponse.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ProjectTagsResponse.

        Deprecated. Total of tags  # noqa: E501

        :param total: The total of this ProjectTagsResponse.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ProjectTagsResponse, dict):
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
        if not isinstance(other, ProjectTagsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectTagsResponse):
            return True

        return self.to_dict() != other.to_dict()