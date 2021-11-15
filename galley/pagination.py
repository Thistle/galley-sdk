import logging

logger = logging.getLogger(__name__)


def paginate_results(func, page_size: int = 25):
    """
    can decorate any function with an initial list input
    and collect its output in pages of page_size
    """

    def wrapper(*args):
        input_list = args[0]
        result = []
        if type(input_list) is not list:
            logger.error(f'argument {input_list} is not a list')
            return result
        for partition in range((len(input_list)//page_size) + 1):
            result.extend(
                func(input_list[partition * page_size: (partition + 1) * page_size])
            )
        return result

    return wrapper
