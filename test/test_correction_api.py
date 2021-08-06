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
from swagger_client.api.correction_api import CorrectionApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCorrectionApi(unittest.TestCase):
    """CorrectionApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.correction_api.CorrectionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_project_id_corrections_correction_id_delete(self):
        """Test case for projects_project_id_corrections_correction_id_delete

        Delete a correction session.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post(self):
        """Test case for projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_statuses_post

        Mark a segment as corrected.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post(self):
        """Test case for projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_post

        Add a tag to a segment.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete(self):
        """Test case for projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_delete

        Delete a tag.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put(self):
        """Test case for projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_put

        Change a tag.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post(self):
        """Test case for projects_project_id_corrections_correction_id_documents_document_id_segments_segment_id_tags_tag_id_statuses_post

        Confirm a tag.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_documents_get(self):
        """Test case for projects_project_id_corrections_correction_id_documents_get

        Get correction session's documents.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_correction_id_get(self):
        """Test case for projects_project_id_corrections_correction_id_get

        Return a correction session.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_get(self):
        """Test case for projects_project_id_corrections_get

        Return a list of correction sessions that belongs to a project.  # noqa: E501
        """
        pass

    def test_projects_project_id_corrections_post(self):
        """Test case for projects_project_id_corrections_post

        Create a new correction session.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
