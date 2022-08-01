import backoff
from http import HTTPStatus
from typing import Dict, Optional, Any
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from galley import api_key, api_url, max_retries
import logging

logger = logging.getLogger(__name__)

GALLEY_ERROR_PREFIX = "(GalleyError)"


# GALLEY ENDPOINT BUILDER

def build_galley_endpoint() -> HTTPEndpoint:
    headers = {
        'x-api-key': api_key,
        'Accept': 'application/json'
    }
    return HTTPEndpoint(api_url, headers)


def can_retry(data: Optional[Dict]) -> bool:
    return data.get('status') in [
        HTTPStatus.REQUEST_TIMEOUT,
        HTTPStatus.TOO_MANY_REQUESTS,
        HTTPStatus.INTERNAL_SERVER_ERROR,
        HTTPStatus.SERVICE_UNAVAILABLE
    ] if data else False


# REQUEST OPERATION FUNCTION TO QUERY / MUTATE GALLEY DATA
@backoff.on_predicate(lambda: backoff.constant(interval=0.5), predicate=can_retry, max_tries=max_retries + 1)
def make_request_to_galley(op: Operation, variables: Optional[Dict] = None) -> Optional[Dict]:
    endpoint = build_galley_endpoint()
    return endpoint(op, {} if variables is None else variables)

# DATA VALIDATORS
def validate_response_data(data, *fields):
    error = None

    if data is None:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Error retrieving response data: API return null value or raised an exception")

    if any(key in data for key in ('error', 'errors')):
        error = data.get('error') or data.get('errors')
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Error retrieving response data{f': {error}' if error else ''}")

    if 'data' in data and data['data']:
        head = data['data']

        if 'viewer' in data['data']:
            if data['data']['viewer']:
                head = data['data']['viewer']
            else:
                raise ValueError(f"{GALLEY_ERROR_PREFIX} Error retrieving 'viewer' data")

        return validate_fields(head, fields) if fields else head

    else:
        raise ValueError(f"{GALLEY_ERROR_PREFIX} Error retrieving response data")


def validate_fields(data, keys):
    _data = data
    for key in keys:
        try:
            _data = _data[key]
        except KeyError:
            logger.error(f"{GALLEY_ERROR_PREFIX} Error retrieving '{key}' data")
            return None
    return _data


def validate_response_data_structure(forecasted_data_struct: Any, response_data: Any) -> bool:
    if isinstance(forecasted_data_struct, dict) and isinstance(response_data, dict):
        # check if all keys in forecasted_data_struct are in response_data
        return all(
            key in response_data and validate_response_data_structure(
                forecasted_data_struct[key], response_data[key]
            ) for key in forecasted_data_struct
        )
    elif isinstance(forecasted_data_struct, list) and isinstance(response_data, list):
        # check if all elements in forecasted_data_struct are in response_data
        return all(validate_response_data_structure(forecasted_data_struct[0], rds) for rds in response_data)
    elif isinstance(forecasted_data_struct, type):
        # check if response_data is of type forecasted_data_struct
        return isinstance(response_data, forecasted_data_struct)
    elif forecasted_data_struct == Any:
        # If the value has return type Any we should assume this field could have any type of value.
        # These values are hard to do data validation.
        return True

    return False
