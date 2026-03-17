from rest_framework.views import exception_handler
from rest_framework.response import Response
from common.responses import error_response
from common.exceptions import CustomException


def custom_exception_handler(exc, context):
    if isinstance(exc, CustomException):
        return Response(
            error_response(message=exc.message),
            status=exc.status_code
        )

    response = exception_handler(exc, context)

    if response is not None:
        return Response(
            error_response(
                message="Request validation failed",
                errors=response.data
            ),
            status=response.status_code
        )

    return Response(
        error_response(message="Internal server error"),
        status=500
    )