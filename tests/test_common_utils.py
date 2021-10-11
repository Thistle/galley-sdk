from typing import Any
from unittest import mock, TestCase
from sgqlc.operation import Operation

from galley.common import (
    validate_response_data_structure,
    validate_response_data,
    validate_fields,
    make_request_to_galley
)
from galley.queries import Query
from galley.mutations import Mutation


class TestValidateResponseDataStructure(TestCase):
    def setUp(self):
        self.forecasted_data_struct = {
            'id': int,
            'name': str,
            'description': Any
        }

    def test_data_structure_validation_successful(self):
        self.response_data = {
            'id': 10000,
            'name': 'Test Testovich',
            'description': 'Test description'
        }
        is_valid = validate_response_data_structure(
            forecasted_data_struct=self.forecasted_data_struct,
            response_data=self.response_data
        )
        self.assertEqual(is_valid, True)

    def test_data_structure_validation_failed(self):
        self.response_data = {
            'id': 'wrongID',
            'name': 10000,
            'description': None
        }
        is_valid = validate_response_data_structure(
            forecasted_data_struct=self.forecasted_data_struct,
            response_data=self.response_data
        )
        self.assertEqual(is_valid, False)


class TestValidateResponseData(TestCase):
    def test_error_or_errors_validation(self):
        self.response_data = {
            'errors': [{
                'message': "Invalid input.",
                "code": "BAD_USER_INPUT",
            }],
            "data": None
        }
        result = validate_response_data(self.response_data)
        self.assertEqual(result, None)

    def test_query_viewer_field_successful(self):
        self.data = {
            "recipe": {
                "id": "ABCDE123",
                "name": "Test Recipe",
            }
        }

        self.return_value = {
            "data": {
                "viewer": self.data
            }
        }
        result = validate_response_data(self.return_value)
        self.assertEqual(result, self.data)

    def test_query_viewer_field_failure(self):
        self.return_value = {
            "data": {
                "viewer": None
            }
        }
        result = validate_response_data(self.return_value)
        self.assertEqual(result, None)

    def test_response_data_failure(self):
        self.return_value = {
            'data': None
        }
        result = validate_response_data(self.return_value)
        self.assertEqual(result, None)

    def test_response_data_fields_check_success(self):
        self.data = {
            'id': 12345,
            'name': 'Test Testovich',
            'description': 'Test description.'
        }

        self.fields = {
            'item1': {
                'item2': {
                    'item3': self.data
                }
            }
        }

        self.return_value = {
            'data': self.fields
        }
        checked = validate_fields(self.fields, ('item1', 'item2', 'item3'))
        result = validate_response_data(self.return_value, 'item1', 'item2', 'item3')
        self.assertEqual(result, self.data)
        self.assertEqual(checked, self.data)


class TestQueryGalleyDataOperation(TestCase):
    @mock.patch('sgqlc.endpoint.http.HTTPEndpoint.__call__')
    def test_retrieve_successful(self, mock_endpoint_call):
        mock_endpoint_call.return_value = {
            'id': 10000,
            'name': 'Test testovich',
            'description': 'Test description'
        }
        make_request_to_galley(op=Operation(Query))
        self.assertEqual(mock_endpoint_call.call_count, 1)

    @mock.patch('sgqlc.endpoint.http.HTTPEndpoint.__call__', **{'side_effect': Exception()})
    def test_retrieve_retry(self, mock_endpoint_call):
        result = make_request_to_galley(op=Operation(Query))
        self.assertEqual(mock_endpoint_call.call_count, 2)
        self.assertEqual(result, None)


class TestMutateGalleyDataOperation(TestCase):
    @mock.patch('sgqlc.endpoint.http.HTTPEndpoint.__call__')
    def test_mutatation_successful(self, mock_endpoint_call):
        mock_endpoint_call.return_value = {
            'id': 12345,
            'description': 'Test description...'
        }
        make_request_to_galley(op=Operation(Mutation))
        self.assertEqual(mock_endpoint_call.call_count, 1)

    @mock.patch('sgqlc.endpoint.http.HTTPEndpoint.__call__', **{'side_effect': Exception()})
    def test_mutation_retry(self, mock_endpoint_call):
        result = make_request_to_galley(op=Operation(Mutation))
        self.assertEqual(mock_endpoint_call.call_count, 2)
        self.assertEqual(result, None)
