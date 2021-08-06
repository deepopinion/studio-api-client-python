# coding: utf-8

"""
    Studio API

    Studio API  # noqa: E501

    OpenAPI spec version: 1.6.2 
    Contact: support@deepopinion.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.documents_api import DocumentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDocumentsApi(unittest.TestCase):
    """DocumentsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.documents_api.DocumentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_project_id_documents_document_id_delete(self):
        """Test case for projects_project_id_documents_document_id_delete

        Delete a document of a project.  # noqa: E501
        """
        pass

    def test_projects_project_id_documents_document_id_get(self):
        """Test case for projects_project_id_documents_document_id_get

        Get a particular document of a project.  # noqa: E501
        """
        pass

    def test_projects_project_id_documents_document_id_put(self):
        """Test case for projects_project_id_documents_document_id_put

        Change a document.  # noqa: E501
        """
        pass

    def test_projects_project_id_documents_get(self):
        """Test case for projects_project_id_documents_get

        Fetches all documents of a given project  # noqa: E501
        """
        pass

    def test_projects_project_id_documents_post(self):
        """Test case for projects_project_id_documents_post

        Create a new document.  # noqa: E501
        """
        pass

    def test_projects_project_id_upload_documents_post(self):
        """Test case for projects_project_id_upload_documents_post

        Upload new documents.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
