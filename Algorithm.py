import importlib
import re
import logging
import inspect
logger = logging.getLogger(__name__)

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Algorithm:
    def __init__(self):
        self.name = name = to_snake_case(self.__class__.__name__)

        # Import all functions from corresponding algorithm module
        try:
            module = importlib.import_module(name)
            self.functions = all_fcns = inspect.getmembers(module, inspect.isfunction)
            for fcn in all_fcns:
                # self.functions.append(fcn[1])
                setattr(self, fcn[0], fcn[1])

        except TypeError as e:
            logger.error("{}: {}".format(name, e))

    def get_functions(self):
        return [f[1] for f in self.functions]

