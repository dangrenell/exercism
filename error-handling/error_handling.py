def handle_error_by_throwing_exception():
    raise ValueError("Message")


def handle_error_by_returning_none(input_data):
    try:
        return int(input_data)
    except:
        return None


def handle_error_by_returning_tuple(input_data):
    try:
        return True, int(input_data)
    except:
        return False, input_data


def filelike_objects_are_closed_on_exception(filelike_object):
    filelike_object.open()
    filelike_object.close()
    filelike_object.do_something()
