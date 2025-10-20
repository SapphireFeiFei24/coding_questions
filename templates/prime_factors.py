"""
Get all the prime factors for n

Prime Number Theorem:
Numbers of primes for k <= k and is approximately around k/ln(k)
"""


# Handles large n (up to around 10^12)
def prime_factors(n):
    factors = []
    # Handle 2(even numbers) separately for efficiency
    while n % 2 == 0:  # O(sqrt(n))
        factors.append(2)
        n //= 2

    # Only need to check odd numbers up to sqrt(n)
    p = 3
    while p * p <= n:  # O(sqrt(n))
        if n % p == 0:
            factors.append(p)
            n //= p
        p += 2
    # It's a prime factor itself
    if n > 1:
        factors.append(n)
    return factors


# If handlers large queries, precompute the prime numbers up to sqrt(max(n))
# [Sieve of Eratosthenes] Up to N: O(NloglogN) -> only precompute up to sqrt(N): O(sqrt(N)loglog(sqrt(N))
def sieve(limit: int) -> list[int]:
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return [i for i, prime in enumerate(is_prime) if prime]


# Only check primes <= sqrt(n)
# O(sqrt(N)/ln(sqrt(N))
def prime_factors_with_sieve(n: int, primes: list[int]) -> list[int]:
    """Use precomputed primes for faster factorization."""
    factors = []
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors.append(p)
            n //= p
    if n > 1:
        factors.append(n)
    return factors