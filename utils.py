
def algorithms(module):
    """
    Retrieves algorithm functions from a module. Raises AssertionError if no functions are provided.
    :param module:
    :return:
    """
    blacklist = ['deque', 'defaultdict', 'namedtuple', 'OrderedDict']
    l = [getattr(module, attr) for attr in filter(lambda x: x not in blacklist, dir(module)) if callable(getattr(module, attr))]
    assert l
    return l
