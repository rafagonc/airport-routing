from .exceptions import MissingRequestDataException

def get_request_field(data, key, optional=False, default=None):
    value = data.get(key, default)
    if value is None and optional is False:
        raise MissingRequestDataException(data, key)
    return value
        
