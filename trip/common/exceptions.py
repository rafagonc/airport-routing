from rest_framework.exceptions import APIException


class RouteException(APIException):
    pass


class ValdationError(RouteException):
    statuscode = 400
    default_code = "validation_error"

    def __init__(self, error):
        self.detail = error

    def __str__(self):
        return self.detail


class MissingRequestDataException(RouteException):
    statuscode = 400
    default_code = "missing_field_on_request"

    def __init__(self, data, key):
        self.data = data
        self.key = key
        self.detail = "%s is missing on the request, found %s" % (self.key,
                                                                  self.data)

    def __str__(self):
        return self.detail


class MissingFileException(RouteException):
    statuscode = 400
    default_code = "missing_file_on_server"

    def __init__(self, filename):
        self.filename = filename
        self.detail = "%s is missing on server path" % self.filename

    def __str__(self):
        return self.detail
