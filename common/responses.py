def success_response(data=None, message="Success", meta=None):
    return {
        "success": True,
        "message": message,
        "data": data,
        "meta": meta
    }


def error_response(message="Something went wrong", errors=None):
    return {
        "success": False,
        "message": message,
        "errors": errors
    }