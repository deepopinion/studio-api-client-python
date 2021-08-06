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


class DetailedModel(object):
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
        'base': 'str',
        'classes': 'list[str]',
        'created': 'datetime',
        'demoset': 'list[LabelledDocument]',
        'display_name': 'str',
        'id': 'int',
        'labels': 'list[str]',
        'language': 'str',
        'long_description': 'str',
        'metrics': 'object',
        'name': 'str',
        'owner': 'str',
        'progress': 'float',
        'project_id': 'int',
        'score': 'float',
        'short_description': 'str',
        'status': 'str',
        'type': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'base': 'base',
        'classes': 'classes',
        'created': 'created',
        'demoset': 'demoset',
        'display_name': 'display_name',
        'id': 'id',
        'labels': 'labels',
        'language': 'language',
        'long_description': 'long_description',
        'metrics': 'metrics',
        'name': 'name',
        'owner': 'owner',
        'progress': 'progress',
        'project_id': 'project_id',
        'score': 'score',
        'short_description': 'short_description',
        'status': 'status',
        'type': 'type',
        'uuid': 'uuid'
    }

    def __init__(self, base=None, classes=None, created=None, demoset=None, display_name=None, id=None, labels=None, language=None, long_description=None, metrics=None, name=None, owner=None, progress=None, project_id=None, score=None, short_description=None, status=None, type=None, uuid=None, _configuration=None):  # noqa: E501
        """DetailedModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._base = None
        self._classes = None
        self._created = None
        self._demoset = None
        self._display_name = None
        self._id = None
        self._labels = None
        self._language = None
        self._long_description = None
        self._metrics = None
        self._name = None
        self._owner = None
        self._progress = None
        self._project_id = None
        self._score = None
        self._short_description = None
        self._status = None
        self._type = None
        self._uuid = None
        self.discriminator = None

        if base is not None:
            self.base = base
        if classes is not None:
            self.classes = classes
        if created is not None:
            self.created = created
        if demoset is not None:
            self.demoset = demoset
        if display_name is not None:
            self.display_name = display_name
        if id is not None:
            self.id = id
        if labels is not None:
            self.labels = labels
        if language is not None:
            self.language = language
        if long_description is not None:
            self.long_description = long_description
        if metrics is not None:
            self.metrics = metrics
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if progress is not None:
            self.progress = progress
        if project_id is not None:
            self.project_id = project_id
        if score is not None:
            self.score = score
        if short_description is not None:
            self.short_description = short_description
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid

    @property
    def base(self):
        """Gets the base of this DetailedModel.  # noqa: E501

        the name of the model used to create the modal that's being changed  # noqa: E501

        :return: The base of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base):
        """Sets the base of this DetailedModel.

        the name of the model used to create the modal that's being changed  # noqa: E501

        :param base: The base of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._base = base

    @property
    def classes(self):
        """Gets the classes of this DetailedModel.  # noqa: E501

        All classes that belong to the project  # noqa: E501

        :return: The classes of this DetailedModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._classes

    @classes.setter
    def classes(self, classes):
        """Sets the classes of this DetailedModel.

        All classes that belong to the project  # noqa: E501

        :param classes: The classes of this DetailedModel.  # noqa: E501
        :type: list[str]
        """

        self._classes = classes

    @property
    def created(self):
        """Gets the created of this DetailedModel.  # noqa: E501

        creation date  # noqa: E501

        :return: The created of this DetailedModel.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DetailedModel.

        creation date  # noqa: E501

        :param created: The created of this DetailedModel.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def demoset(self):
        """Gets the demoset of this DetailedModel.  # noqa: E501

        A list of documents to be used to demo a model  # noqa: E501

        :return: The demoset of this DetailedModel.  # noqa: E501
        :rtype: list[LabelledDocument]
        """
        return self._demoset

    @demoset.setter
    def demoset(self, demoset):
        """Sets the demoset of this DetailedModel.

        A list of documents to be used to demo a model  # noqa: E501

        :param demoset: The demoset of this DetailedModel.  # noqa: E501
        :type: list[LabelledDocument]
        """

        self._demoset = demoset

    @property
    def display_name(self):
        """Gets the display_name of this DetailedModel.  # noqa: E501

        a friendly name.  # noqa: E501

        :return: The display_name of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DetailedModel.

        a friendly name.  # noqa: E501

        :param display_name: The display_name of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this DetailedModel.  # noqa: E501

        The ID of the model  # noqa: E501

        :return: The id of this DetailedModel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DetailedModel.

        The ID of the model  # noqa: E501

        :param id: The id of this DetailedModel.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                id is not None and id < 1):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._id = id

    @property
    def labels(self):
        """Gets the labels of this DetailedModel.  # noqa: E501

        All labels that belong to the project  # noqa: E501

        :return: The labels of this DetailedModel.  # noqa: E501
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DetailedModel.

        All labels that belong to the project  # noqa: E501

        :param labels: The labels of this DetailedModel.  # noqa: E501
        :type: list[str]
        """

        self._labels = labels

    @property
    def language(self):
        """Gets the language of this DetailedModel.  # noqa: E501

        Language of the model  # noqa: E501

        :return: The language of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DetailedModel.

        Language of the model  # noqa: E501

        :param language: The language of this DetailedModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["en", "de", "ar"]  # noqa: E501
        if (self._configuration.client_side_validation and
                language not in allowed_values):
            raise ValueError(
                "Invalid value for `language` ({0}), must be one of {1}"  # noqa: E501
                .format(language, allowed_values)
            )

        self._language = language

    @property
    def long_description(self):
        """Gets the long_description of this DetailedModel.  # noqa: E501

        a longer description which proper describes the model  # noqa: E501

        :return: The long_description of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._long_description

    @long_description.setter
    def long_description(self, long_description):
        """Sets the long_description of this DetailedModel.

        a longer description which proper describes the model  # noqa: E501

        :param long_description: The long_description of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._long_description = long_description

    @property
    def metrics(self):
        """Gets the metrics of this DetailedModel.  # noqa: E501

        The metrics associated to the model  # noqa: E501

        :return: The metrics of this DetailedModel.  # noqa: E501
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this DetailedModel.

        The metrics associated to the model  # noqa: E501

        :param metrics: The metrics of this DetailedModel.  # noqa: E501
        :type: object
        """

        self._metrics = metrics

    @property
    def name(self):
        """Gets the name of this DetailedModel.  # noqa: E501

        internal name. It should be unique for a workspace  # noqa: E501

        :return: The name of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DetailedModel.

        internal name. It should be unique for a workspace  # noqa: E501

        :param name: The name of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this DetailedModel.  # noqa: E501


        :return: The owner of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DetailedModel.


        :param owner: The owner of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def progress(self):
        """Gets the progress of this DetailedModel.  # noqa: E501


        :return: The progress of this DetailedModel.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this DetailedModel.


        :param progress: The progress of this DetailedModel.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def project_id(self):
        """Gets the project_id of this DetailedModel.  # noqa: E501

        The ID of the project  # noqa: E501

        :return: The project_id of this DetailedModel.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this DetailedModel.

        The ID of the project  # noqa: E501

        :param project_id: The project_id of this DetailedModel.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def score(self):
        """Gets the score of this DetailedModel.  # noqa: E501

        model score. As this is a result of a training session, this value shouldn't be touched  # noqa: E501

        :return: The score of this DetailedModel.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this DetailedModel.

        model score. As this is a result of a training session, this value shouldn't be touched  # noqa: E501

        :param score: The score of this DetailedModel.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def short_description(self):
        """Gets the short_description of this DetailedModel.  # noqa: E501

        a short description to help users quickly identify the model  # noqa: E501

        :return: The short_description of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this DetailedModel.

        a short description to help users quickly identify the model  # noqa: E501

        :param short_description: The short_description of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

    @property
    def status(self):
        """Gets the status of this DetailedModel.  # noqa: E501

        the model status  # noqa: E501

        :return: The status of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DetailedModel.

        the model status  # noqa: E501

        :param status: The status of this DetailedModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "QUEUED", "TRAINING", "FAILED", "READY", "ACTIVE", "PUBLISHED"]  # noqa: E501
        if (self._configuration.client_side_validation and
                status not in allowed_values):
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def type(self):
        """Gets the type of this DetailedModel.  # noqa: E501

        model type (1: BASE, 2: ABSA, 3: LABEL, 4: CLASS, 5: CLASSLABEL))  # noqa: E501

        :return: The type of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DetailedModel.

        model type (1: BASE, 2: ABSA, 3: LABEL, 4: CLASS, 5: CLASSLABEL))  # noqa: E501

        :param type: The type of this DetailedModel.  # noqa: E501
        :type: str
        """
        allowed_values = ["ABSA", "CLASS", "LABEL", "CLASSLABEL"]  # noqa: E501
        if (self._configuration.client_side_validation and
                type not in allowed_values):
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this DetailedModel.  # noqa: E501

        model unique identifier. Should be a UUID value  # noqa: E501

        :return: The uuid of this DetailedModel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this DetailedModel.

        model unique identifier. Should be a UUID value  # noqa: E501

        :param uuid: The uuid of this DetailedModel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(DetailedModel, dict):
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
        if not isinstance(other, DetailedModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DetailedModel):
            return True

        return self.to_dict() != other.to_dict()
