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


class Segment(object):
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
        'span': 'list[int]',
        'text': 'str'
    }

    attribute_map = {
        'span': 'span',
        'text': 'text'
    }

    def __init__(self, span=None, text=None, _configuration=None):  # noqa: E501
        """Segment - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._span = None
        self._text = None
        self.discriminator = None

        if span is not None:
            self.span = span
        if text is not None:
            self.text = text

    @property
    def span(self):
        """Gets the span of this Segment.  # noqa: E501

        The interval at which the segment occurs in the original document  # noqa: E501

        :return: The span of this Segment.  # noqa: E501
        :rtype: list[int]
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this Segment.

        The interval at which the segment occurs in the original document  # noqa: E501

        :param span: The span of this Segment.  # noqa: E501
        :type: list[int]
        """

        self._span = span

    @property
    def text(self):
        """Gets the text of this Segment.  # noqa: E501

        The segment text  # noqa: E501

        :return: The text of this Segment.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Segment.

        The segment text  # noqa: E501

        :param text: The text of this Segment.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(Segment, dict):
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
        if not isinstance(other, Segment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Segment):
            return True

        return self.to_dict() != other.to_dict()