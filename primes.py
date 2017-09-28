
def primes(n):
    primes = []

    is_prime = [False, False] + [True] * (n-1)

    for i in range(2, n+1):
        if not is_prime[i]:
            continue

        primes.append(i)

        for j in range(i, len(is_prime), i):
            is_prime[j] = False

    return primes
