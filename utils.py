
def algorithms(module):
    """
    Retrieves algorithm functions from a module. Raises AssertionError if no functions are provided.
    :param module:
    :return:
    """
    l = [getattr(module, attr) for attr in dir(module) if callable(getattr(module, attr))]
    assert l
    return l
