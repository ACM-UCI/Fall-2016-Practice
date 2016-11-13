# Find all prime numbers up to n
def sieve(n):
    l = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not l[i]:
            primes.append(i)
            for j in range(2*i, n + 1, i):
                l[j] = True
    return primes