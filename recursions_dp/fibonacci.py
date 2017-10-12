import collections

cache = collections.defaultdict(int)

cache[0] = 0
cache[1] = 1
cache[2] = 2

def fibonacci(n):
    if n <= 2:
        return n

    if cache[n-1] > 0:
        f1 = cache[n-1]
    else:
        f1 = cache[n-1] = fibonacci(n-1)

    if cache[n-2] > 0:
        f2 = cache[n-2]
    else:
        f2 = cache[n-2] = fibonacci(n-2)

    return f1 + f2

def even_terms_sum():
    sum = 0
    for k in cache.keys():
        if cache[k] % 2 == 0 and cache[k] <= 4000000:
            sum += cache[k]
    return sum