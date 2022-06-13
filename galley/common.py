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
    try:
        return endpoint(op, {} if variables is None else variables)
    except Exception as ex:
        logger.exception(ex)
        return None


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


# filter_by = [{
#     haystack_key: any      --> haystack element collected into a csv
#     needle: any    --> needle neing searched
#     isFalse: bool --> Optional for negation
# }]
def apply_filters(obj, filter_by = None) -> bool:
    filters = True
    if filter_by:
        for filter_parameter in filter_by:
            # ensure that the needle and haystack keys are set
            if "haystack_key" in filter_parameter.keys() \
                and "needle" in filter_parameter.keys():
                # combine all haystack values into a csv
                haystack = {item.get(filter_parameter.get("haystack_key")) \
                            for item in obj}
                # apply the filter, can needle value be (or not be) found
                # in the haystack list
                filters = filters \
                    and (
                        filter_parameter.get("needle") in haystack
                        or filter_parameter.get("isFalse") is True \
                            and filter_parameter.get("needle") not in haystack
                    )
    return filters
