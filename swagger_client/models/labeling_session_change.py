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


class LabelingSessionChange(object):
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
        'classes': 'list[str]',
        'document_ids': 'list[int]',
        'documents': 'list[LabelledDocument]',
        'labels': 'list[str]',
        'name': 'str'
    }

    attribute_map = {
        'classes': 'classes',
        'document_ids': 'document_ids',
        'documents': 'documents',
        'labels': 'labels',
        'name': 'name'
    }

    def __init__(self, classes=None, document_ids=None, documents=None, labels=None, name=None, _configuration=None):  # noqa: E501
        """LabelingSessionChange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._classes = None
        self._document_ids = None
        self._documents = None
        self._labels = None
        self._name = None
        self.discriminator = None

        if classes is not None:
            self.classes = classes
        if document_ids is not None:
            self.document_ids = document_ids
        if documents is not None:
            self.documents = documents
        if labels is not None:
            self.labels = labels
        if name is not None:
            self.name = name

    @property
    def classes(self):
        """Gets the classes of this LabelingSessionChange.  # noqa: E501

        Classes contained in that session.  # noqa: E501

        :return: The classes of this LabelingSessionChange.  # noqa: E501
        :rtype: list[str]
        """
        return self._classes

    @classes.setter
    def classes(self, classes):
        """Sets the classes of this LabelingSessionChange.

        Classes contained in that session.  # noqa: E501

        :param classes: The classes of this LabelingSessionChange.  # noqa: E501
        :type: list[str]
        """

        self._classes = classes

    @property
    def document_ids(self):
        """Gets the document_ids of this LabelingSessionChange.  # noqa: E501


        :return: The document_ids of this LabelingSessionChange.  # noqa: E501
        :rtype: list[int]
        """
        return self._document_ids

    @document_ids.setter
    def document_ids(self, document_ids):
        """Sets the document_ids of this LabelingSessionChange.


        :param document_ids: The document_ids of this LabelingSessionChange.  # noqa: E501
        :type: list[int]
        """

        self._document_ids = document_ids

    @property
    def documents(self):
        """Gets the documents of this LabelingSessionChange.  # noqa: E501


        :return: The documents of this LabelingSessionChange.  # noqa: E501
        :rtype: list[LabelledDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this LabelingSessionChange.


        :param documents: The documents of this LabelingSessionChange.  # noqa: E501
        :type: list[LabelledDocument]
        """

        self._documents = documents

    @property
    def labels(self):
        """Gets the labels of this LabelingSessionChange.  # noqa: E501

        Labels contained in that session.  # noqa: E501

        :return: The labels of this LabelingSessionChange.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this LabelingSessionChange.

        Labels contained in that session.  # noqa: E501

        :param labels: The labels of this LabelingSessionChange.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def name(self):
        """Gets the name of this LabelingSessionChange.  # noqa: E501

        Name of the labeling session  # noqa: E501

        :return: The name of this LabelingSessionChange.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelingSessionChange.

        Name of the labeling session  # noqa: E501

        :param name: The name of this LabelingSessionChange.  # noqa: E501
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
        if issubclass(LabelingSessionChange, dict):
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
        if not isinstance(other, LabelingSessionChange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LabelingSessionChange):
            return True

        return self.to_dict() != other.to_dict()
