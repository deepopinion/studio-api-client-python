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


class SegmentAnnotationStatus(object):
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
        'annotation_id': 'int',
        'created': 'datetime',
        'document_id': 'int',
        'name': 'str',
        'segment_id': 'int'
    }

    attribute_map = {
        'annotation_id': 'annotation_id',
        'created': 'created',
        'document_id': 'document_id',
        'name': 'name',
        'segment_id': 'segment_id'
    }

    def __init__(self, annotation_id=None, created=None, document_id=None, name=None, segment_id=None, _configuration=None):  # noqa: E501
        """SegmentAnnotationStatus - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._annotation_id = None
        self._created = None
        self._document_id = None
        self._name = None
        self._segment_id = None
        self.discriminator = None

        if annotation_id is not None:
            self.annotation_id = annotation_id
        if created is not None:
            self.created = created
        if document_id is not None:
            self.document_id = document_id
        if name is not None:
            self.name = name
        if segment_id is not None:
            self.segment_id = segment_id

    @property
    def annotation_id(self):
        """Gets the annotation_id of this SegmentAnnotationStatus.  # noqa: E501

        The ID of the labeling session.  # noqa: E501

        :return: The annotation_id of this SegmentAnnotationStatus.  # noqa: E501
        :rtype: int
        """
        return self._annotation_id

    @annotation_id.setter
    def annotation_id(self, annotation_id):
        """Sets the annotation_id of this SegmentAnnotationStatus.

        The ID of the labeling session.  # noqa: E501

        :param annotation_id: The annotation_id of this SegmentAnnotationStatus.  # noqa: E501
        :type: int
        """

        self._annotation_id = annotation_id

    @property
    def created(self):
        """Gets the created of this SegmentAnnotationStatus.  # noqa: E501


        :return: The created of this SegmentAnnotationStatus.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SegmentAnnotationStatus.


        :param created: The created of this SegmentAnnotationStatus.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def document_id(self):
        """Gets the document_id of this SegmentAnnotationStatus.  # noqa: E501

        The ID of the document.  # noqa: E501

        :return: The document_id of this SegmentAnnotationStatus.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this SegmentAnnotationStatus.

        The ID of the document.  # noqa: E501

        :param document_id: The document_id of this SegmentAnnotationStatus.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def name(self):
        """Gets the name of this SegmentAnnotationStatus.  # noqa: E501

        The status.  # noqa: E501

        :return: The name of this SegmentAnnotationStatus.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SegmentAnnotationStatus.

        The status.  # noqa: E501

        :param name: The name of this SegmentAnnotationStatus.  # noqa: E501
        :type: str
        """
        allowed_values = ["ANNOTATED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                name not in allowed_values):
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def segment_id(self):
        """Gets the segment_id of this SegmentAnnotationStatus.  # noqa: E501

        The ID of the segment.  # noqa: E501

        :return: The segment_id of this SegmentAnnotationStatus.  # noqa: E501
        :rtype: int
        """
        return self._segment_id

    @segment_id.setter
    def segment_id(self, segment_id):
        """Sets the segment_id of this SegmentAnnotationStatus.

        The ID of the segment.  # noqa: E501

        :param segment_id: The segment_id of this SegmentAnnotationStatus.  # noqa: E501
        :type: int
        """

        self._segment_id = segment_id

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
        if issubclass(SegmentAnnotationStatus, dict):
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
        if not isinstance(other, SegmentAnnotationStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SegmentAnnotationStatus):
            return True

        return self.to_dict() != other.to_dict()
