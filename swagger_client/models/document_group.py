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


class DocumentGroup(object):
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
        'document_count': 'int',
        'id': 'int',
        'name': 'str',
        'project_id': 'int',
        'source': 'str',
        'status': 'str'
    }

    attribute_map = {
        'created': 'created',
        'document_count': 'document_count',
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'source': 'source',
        'status': 'status'
    }

    def __init__(self, created=None, document_count=None, id=None, name=None, project_id=None, source=None, status=None, _configuration=None):  # noqa: E501
        """DocumentGroup - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._document_count = None
        self._id = None
        self._name = None
        self._project_id = None
        self._source = None
        self._status = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if document_count is not None:
            self.document_count = document_count
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if source is not None:
            self.source = source
        if status is not None:
            self.status = status

    @property
    def created(self):
        """Gets the created of this DocumentGroup.  # noqa: E501


        :return: The created of this DocumentGroup.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DocumentGroup.


        :param created: The created of this DocumentGroup.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def document_count(self):
        """Gets the document_count of this DocumentGroup.  # noqa: E501

        Total of documents  # noqa: E501

        :return: The document_count of this DocumentGroup.  # noqa: E501
        :rtype: int
        """
        return self._document_count

    @document_count.setter
    def document_count(self, document_count):
        """Sets the document_count of this DocumentGroup.

        Total of documents  # noqa: E501

        :param document_count: The document_count of this DocumentGroup.  # noqa: E501
        :type: int
        """

        self._document_count = document_count

    @property
    def id(self):
        """Gets the id of this DocumentGroup.  # noqa: E501

        The ID of the document group.  # noqa: E501

        :return: The id of this DocumentGroup.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentGroup.

        The ID of the document group.  # noqa: E501

        :param id: The id of this DocumentGroup.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this DocumentGroup.  # noqa: E501

        The document group's name.  # noqa: E501

        :return: The name of this DocumentGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DocumentGroup.

        The document group's name.  # noqa: E501

        :param name: The name of this DocumentGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this DocumentGroup.  # noqa: E501

        The ID of the project that the document group belongs to.  # noqa: E501

        :return: The project_id of this DocumentGroup.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DocumentGroup.

        The ID of the project that the document group belongs to.  # noqa: E501

        :param project_id: The project_id of this DocumentGroup.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def source(self):
        """Gets the source of this DocumentGroup.  # noqa: E501

        The source of the documents for that group  # noqa: E501

        :return: The source of this DocumentGroup.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DocumentGroup.

        The source of the documents for that group  # noqa: E501

        :param source: The source of this DocumentGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANALYSIS", "UPLOAD", "ANNOTATIONS"]  # noqa: E501
        if (self._configuration.client_side_validation and
                source not in allowed_values):
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def status(self):
        """Gets the status of this DocumentGroup.  # noqa: E501

        The document group's status.  # noqa: E501

        :return: The status of this DocumentGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DocumentGroup.

        The document group's status.  # noqa: E501

        :param status: The status of this DocumentGroup.  # noqa: E501
        :type: str
        """
        allowed_values = ["PROCESSING", "CREATED", "DELETING", "FAILED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

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
        if issubclass(DocumentGroup, dict):
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
        if not isinstance(other, DocumentGroup):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DocumentGroup):
            return True

        return self.to_dict() != other.to_dict()
