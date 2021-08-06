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


class ChangeAnnotationTag(object):
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
        '_class': 'str',
        'label': 'str',
        'span': 'list[int]',
        'text': 'str'
    }

    attribute_map = {
        '_class': 'class',
        'label': 'label',
        'span': 'span',
        'text': 'text'
    }

    def __init__(self, _class=None, label=None, span=None, text=None, _configuration=None):  # noqa: E501
        """ChangeAnnotationTag - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self.__class = None
        self._label = None
        self._span = None
        self._text = None
        self.discriminator = None

        if _class is not None:
            self._class = _class
        if label is not None:
            self.label = label
        if span is not None:
            self.span = span
        if text is not None:
            self.text = text

    @property
    def _class(self):
        """Gets the _class of this ChangeAnnotationTag.  # noqa: E501

        The class's name.  # noqa: E501

        :return: The _class of this ChangeAnnotationTag.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this ChangeAnnotationTag.

        The class's name.  # noqa: E501

        :param _class: The _class of this ChangeAnnotationTag.  # noqa: E501
        :type: str
        """

        self.__class = _class

    @property
    def label(self):
        """Gets the label of this ChangeAnnotationTag.  # noqa: E501

        The label's name.  # noqa: E501

        :return: The label of this ChangeAnnotationTag.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this ChangeAnnotationTag.

        The label's name.  # noqa: E501

        :param label: The label of this ChangeAnnotationTag.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def span(self):
        """Gets the span of this ChangeAnnotationTag.  # noqa: E501


        :return: The span of this ChangeAnnotationTag.  # noqa: E501
        :rtype: list[int]
        """
        return self._span

    @span.setter
    def span(self, span):
        """Sets the span of this ChangeAnnotationTag.


        :param span: The span of this ChangeAnnotationTag.  # noqa: E501
        :type: list[int]
        """

        self._span = span

    @property
    def text(self):
        """Gets the text of this ChangeAnnotationTag.  # noqa: E501

        Annotated text  # noqa: E501

        :return: The text of this ChangeAnnotationTag.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ChangeAnnotationTag.

        Annotated text  # noqa: E501

        :param text: The text of this ChangeAnnotationTag.  # noqa: E501
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
        if issubclass(ChangeAnnotationTag, dict):
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
        if not isinstance(other, ChangeAnnotationTag):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeAnnotationTag):
            return True

        return self.to_dict() != other.to_dict()
