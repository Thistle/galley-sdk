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


# REQUEST OPERATION FUNCTION TO QUERY / MUTATE GALLEY DATA

def make_request_to_galley(op: Operation, retries: int = 0, variables: Optional[Dict] = {}) -> Optional[Dict]:
    endpoint = build_galley_endpoint()
    data = None
    try:
        # Fires a request to galley and fetches data
        data = endpoint(op, variables)
    except Exception as ex:
        # TODO(Dip 20210831 - The exception is too broad but we will have followup ticket to elaborate this.)
        logger.error(f"{GALLEY_ERROR_PREFIX} Unable to process operation request: {ex}")
        retries += 1
        if retries < max_retries:
            make_request_to_galley(op, retries)
    return data


# DATA VALIDATORS

def validate_response_data(data, *fields):
    error = None

    if data is None:
        logger.info(f"{GALLEY_ERROR_PREFIX} Error retrieving response data: API return null value or raised an exception")
        return None

    if any(key in data for key in ('error', 'errors')):
        error = data.get('error') or data.get('errors')
        logger.error(f"{GALLEY_ERROR_PREFIX} Error retrieving response data{f': {error}' if error else ''}")
        return None

    if 'data' in data and data['data']:
        head = data['data']

        if 'viewer' in data['data']:
            if data['data']['viewer']:
                head = data['data']['viewer']
            else:
                logger.error(f"{GALLEY_ERROR_PREFIX} Error retrieving 'viewer' data")
                return None

        return validate_fields(head, fields) if fields else head

    else:
        logger.error(f"{GALLEY_ERROR_PREFIX} Error retrieving response data")
        return None

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
        return all(
            key in response_data and validate_response_data_structure(
                forecasted_data_struct[key], response_data[key]
            ) for key in forecasted_data_struct
        )
    elif isinstance(forecasted_data_struct, list) and isinstance(response_data, list):
        return all(validate_response_data_structure(forecasted_data_struct[0], rds) for rds in response_data)
    elif isinstance(forecasted_data_struct, type):
        return isinstance(response_data, forecasted_data_struct)
    elif forecasted_data_struct == Any:
        # If the value has return type Any we should assume this field could have any type of value.
        # These values are hard to do data validation.
        return True
    else:
        return False

