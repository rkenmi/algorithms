import importlib
import re
import logging
logger = logging.getLogger(__name__)

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

class Algorithm(object):
    def __init__(self):
        self.name = name = to_snake_case(self.__class__.__name__)
        self.functions = []

        # Import relevant functions from the algorithm module
        try:
            module = importlib.import_module(name)
            for s in dir(module):
                if callable(getattr(module, s)) and s.startswith(self.name):
                    fcn = getattr(module, s)
                    self.functions.append(fcn)
                    setattr(self, s, fcn)

        except TypeError as e:
            logger.error("{}: {}".format(name, e.message))

    def get_functions(self):
        return self.functions

