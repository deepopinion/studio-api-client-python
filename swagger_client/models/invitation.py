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


class Invitation(object):
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
        'email': 'str',
        'id': 'int',
        'invitation_link': 'str',
        'invited_by_id': 'int',
        'organization_id': 'int',
        'role': 'str'
    }

    attribute_map = {
        'created': 'created',
        'email': 'email',
        'id': 'id',
        'invitation_link': 'invitation_link',
        'invited_by_id': 'invited_by_id',
        'organization_id': 'organization_id',
        'role': 'role'
    }

    def __init__(self, created=None, email=None, id=None, invitation_link=None, invited_by_id=None, organization_id=None, role=None, _configuration=None):  # noqa: E501
        """Invitation - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._email = None
        self._id = None
        self._invitation_link = None
        self._invited_by_id = None
        self._organization_id = None
        self._role = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if invitation_link is not None:
            self.invitation_link = invitation_link
        if invited_by_id is not None:
            self.invited_by_id = invited_by_id
        if organization_id is not None:
            self.organization_id = organization_id
        if role is not None:
            self.role = role

    @property
    def created(self):
        """Gets the created of this Invitation.  # noqa: E501

        invitation date  # noqa: E501

        :return: The created of this Invitation.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Invitation.

        invitation date  # noqa: E501

        :param created: The created of this Invitation.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501

        Invited email  # noqa: E501

        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.

        Invited email  # noqa: E501

        :param email: The email of this Invitation.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this Invitation.  # noqa: E501

        The ID of the invitation  # noqa: E501

        :return: The id of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Invitation.

        The ID of the invitation  # noqa: E501

        :param id: The id of this Invitation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def invitation_link(self):
        """Gets the invitation_link of this Invitation.  # noqa: E501

        The invitation link. This link contains an invitation token  # noqa: E501

        :return: The invitation_link of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._invitation_link

    @invitation_link.setter
    def invitation_link(self, invitation_link):
        """Sets the invitation_link of this Invitation.

        The invitation link. This link contains an invitation token  # noqa: E501

        :param invitation_link: The invitation_link of this Invitation.  # noqa: E501
        :type: str
        """

        self._invitation_link = invitation_link

    @property
    def invited_by_id(self):
        """Gets the invited_by_id of this Invitation.  # noqa: E501

        ID of the user who sent the invitation  # noqa: E501

        :return: The invited_by_id of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._invited_by_id

    @invited_by_id.setter
    def invited_by_id(self, invited_by_id):
        """Sets the invited_by_id of this Invitation.

        ID of the user who sent the invitation  # noqa: E501

        :param invited_by_id: The invited_by_id of this Invitation.  # noqa: E501
        :type: int
        """

        self._invited_by_id = invited_by_id

    @property
    def organization_id(self):
        """Gets the organization_id of this Invitation.  # noqa: E501

        ID of the organization  # noqa: E501

        :return: The organization_id of this Invitation.  # noqa: E501
        :rtype: int
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Invitation.

        ID of the organization  # noqa: E501

        :param organization_id: The organization_id of this Invitation.  # noqa: E501
        :type: int
        """

        self._organization_id = organization_id

    @property
    def role(self):
        """Gets the role of this Invitation.  # noqa: E501

        User's role  # noqa: E501

        :return: The role of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this Invitation.

        User's role  # noqa: E501

        :param role: The role of this Invitation.  # noqa: E501
        :type: str
        """
        allowed_values = ["USER", "VIEWER", "ANNOTATOR", "ADMIN", "MANAGER"]  # noqa: E501
        if (self._configuration.client_side_validation and
                role not in allowed_values):
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

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
        if issubclass(Invitation, dict):
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
        if not isinstance(other, Invitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invitation):
            return True

        return self.to_dict() != other.to_dict()