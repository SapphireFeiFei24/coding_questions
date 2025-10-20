# Modular

## Inverse of a num with modular
### when mod is a prime(10**9+7)
> Fermat's little theorem
```python
def inverse(prime, MOD):
    pow(prime, MOD-2, MOD)
```
### MOD is not prime but gcd(B, MOD) = 1
> Extended Euclidean Algorithm
```python
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    else:
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y
def modinv(b, mod):
    g, x, _ = extended_gcd(b, mod)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % mod
def modinv(b, mod):
    g, x, _ = extended_gcd(b, mod)
    if g != 1:
        raise ValueError("Inverse does not exist")
    return x % mod
```
### if gcd(B, MOD) != 1
Then it has no modular inverse.

# Greatest Common Divisor
## Euclidean Algorithm
```python
gcd(a, b) == gcd(b, a % b)

when b == 0, gcd(a, 0) == |a|
```