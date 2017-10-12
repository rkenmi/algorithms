
def naive_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(i)

    return primes


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