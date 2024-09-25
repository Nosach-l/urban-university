from pprint import pprint


def introspection_info(obj):
    return {'type': type(obj).__name__,
            'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))
                           and not attr.startswith("__")],
            'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
            'module': obj.__module__}


class ExampleClass:
    def __init__(self, value):
        self.value = value

    def method(self):
        return self.value


number_info = introspection_info(ExampleClass(42))
pprint(number_info)
