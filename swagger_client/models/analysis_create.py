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


class AnalysisCreate(object):
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
        'column': 'int',
        'column_name': 'str',
        'documents': 'list[Document]',
        'file_id': 'str',
        'header_first': 'bool',
        'name': 'str',
        'split': 'bool'
    }

    attribute_map = {
        'column': 'column',
        'column_name': 'column_name',
        'documents': 'documents',
        'file_id': 'file_id',
        'header_first': 'header_first',
        'name': 'name',
        'split': 'split'
    }

    def __init__(self, column=None, column_name=None, documents=None, file_id=None, header_first=None, name=None, split=None, _configuration=None):  # noqa: E501
        """AnalysisCreate - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._column = None
        self._column_name = None
        self._documents = None
        self._file_id = None
        self._header_first = None
        self._name = None
        self._split = None
        self.discriminator = None

        if column is not None:
            self.column = column
        if column_name is not None:
            self.column_name = column_name
        if documents is not None:
            self.documents = documents
        if file_id is not None:
            self.file_id = file_id
        if header_first is not None:
            self.header_first = header_first
        if name is not None:
            self.name = name
        if split is not None:
            self.split = split

    @property
    def column(self):
        """Gets the column of this AnalysisCreate.  # noqa: E501

        The index of the column that should be used as source  # noqa: E501

        :return: The column of this AnalysisCreate.  # noqa: E501
        :rtype: int
        """
        return self._column

    @column.setter
    def column(self, column):
        """Sets the column of this AnalysisCreate.

        The index of the column that should be used as source  # noqa: E501

        :param column: The column of this AnalysisCreate.  # noqa: E501
        :type: int
        """

        self._column = column

    @property
    def column_name(self):
        """Gets the column_name of this AnalysisCreate.  # noqa: E501

        Name of the column or property that contains data to be analyzed  # noqa: E501

        :return: The column_name of this AnalysisCreate.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this AnalysisCreate.

        Name of the column or property that contains data to be analyzed  # noqa: E501

        :param column_name: The column_name of this AnalysisCreate.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def documents(self):
        """Gets the documents of this AnalysisCreate.  # noqa: E501

        array of objects that represent documents.  # noqa: E501

        :return: The documents of this AnalysisCreate.  # noqa: E501
        :rtype: list[Document]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this AnalysisCreate.

        array of objects that represent documents.  # noqa: E501

        :param documents: The documents of this AnalysisCreate.  # noqa: E501
        :type: list[Document]
        """

        self._documents = documents

    @property
    def file_id(self):
        """Gets the file_id of this AnalysisCreate.  # noqa: E501

        Unique identifier of the file  # noqa: E501

        :return: The file_id of this AnalysisCreate.  # noqa: E501
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        """Sets the file_id of this AnalysisCreate.

        Unique identifier of the file  # noqa: E501

        :param file_id: The file_id of this AnalysisCreate.  # noqa: E501
        :type: str
        """

        self._file_id = file_id

    @property
    def header_first(self):
        """Gets the header_first of this AnalysisCreate.  # noqa: E501

        Whether the first line should be used as the file header  # noqa: E501

        :return: The header_first of this AnalysisCreate.  # noqa: E501
        :rtype: bool
        """
        return self._header_first

    @header_first.setter
    def header_first(self, header_first):
        """Sets the header_first of this AnalysisCreate.

        Whether the first line should be used as the file header  # noqa: E501

        :param header_first: The header_first of this AnalysisCreate.  # noqa: E501
        :type: bool
        """

        self._header_first = header_first

    @property
    def name(self):
        """Gets the name of this AnalysisCreate.  # noqa: E501

        Name of the analysis  # noqa: E501

        :return: The name of this AnalysisCreate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisCreate.

        Name of the analysis  # noqa: E501

        :param name: The name of this AnalysisCreate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def split(self):
        """Gets the split of this AnalysisCreate.  # noqa: E501

        Whether documents should be split into sentences  # noqa: E501

        :return: The split of this AnalysisCreate.  # noqa: E501
        :rtype: bool
        """
        return self._split

    @split.setter
    def split(self, split):
        """Sets the split of this AnalysisCreate.

        Whether documents should be split into sentences  # noqa: E501

        :param split: The split of this AnalysisCreate.  # noqa: E501
        :type: bool
        """

        self._split = split

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
        if issubclass(AnalysisCreate, dict):
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
        if not isinstance(other, AnalysisCreate):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AnalysisCreate):
            return True

        return self.to_dict() != other.to_dict()
