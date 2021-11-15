import logging

logger = logging.getLogger(__name__)


def paginate_results(page_size=25):
    """
    can decorate any function with an initial list input
    and collect its output in pages of page_size
    """

    def decorating_function(func):
        def wrapper(*args):
            result = []

            try:
                input_list = args[0]
            except IndexError:
                logger.error('this function requires an argument')
                return result

            if type(input_list) is not list:
                logger.error(f'arg {input_list} is not a list')
                return result

            for partition in range((len(input_list) // page_size) + 1):
                print('making request')
                chunk = input_list[partition * page_size: (partition + 1) * page_size]
                if len(chunk) > 0:
                    result.extend(func(chunk))
            return result
        return wrapper

    return decorating_function
