# Bit Manipulation

## Representing integers in computer
### Signed and unsigned
For k-bit integers, the range of signed integers is -2^(k-1) to 2^(k-1)-1 
The value range of an unsigned integer is 0 to 2^k - 1.

The sign bit: highest bit, 0 represents non-negative, 1 represents negative
### Original code, inverse code and complement code
* [Original code] the sign bit + the absolute value of the truth value of the machine number.
  * [Issue 1] two different original codes for 0
  * [Issue 2] subtractions with original code leads to incorrect results.
* [Inverse code]
  * Non-negative number: same as the original code
  * Negative number: flip every bit of the orignal code except the sign bit
  * [Issue] dual representation of 0 remains
* [Complement code] The computer uses the complement code for calculations
  * Non-negative number: same ass the original code and the inverse code
  * Negative number: add 1 to the inverse code
  * [Advantage 1] no -0, can represent -128 instead(minimum value for original and inverse is -127)
  * [Advantage 2] no subtraction problem
  * Applications: two's complement representations
    * Positive: itself
    * Negative: ~X+1
    * How to get the original negative number from it's two's complement representation:
      * `origin=complement-(1<<32)`
    * Check if it's a negative number
      * `num>=(1<<31)`

## Concepts and properties of bitwise operators
> Operator Priority: (from highest to low) \
> ~, <</>>, &, ^, |
### AND, OR, XOR and Negation
* AND `&`
* OR `|`
* XOR `^`
* Negation `~`

### Shift operation
#### Arithmetic shift vs logical shift
* Logical Shift always fill with zeros, regardless of the sign
* Arithmetic Ship preserve the sign
  * Left shift: fill with 0 on the right
  * Right shift: will with sign bit

  
* Difference
  * Arithmetic is only meaningful for signed integers
    * Always arithmetic in python, integers and signed and unbounded.
    * Arithmetic for signed integer in c++
  * Logical shift is for unsigned integers or bit-level operations

#### Relationship between shift operations and multiplication/division
```python
A << k == A * pow(2,k)
A >> k == A // pow(2,k)
```

### Properties of bitwise operations
// TODO: revisit for applications
* Idempotent law: `a & a == a, a | a == a`
* Commutative law: `a & b == b & a, a | b == b | a, a ^ b == b ^ a`
* Associativity law
  * `(a & b) & c == a & (b & c)`
  * `(a | b) | c == a | (b | c)`
  * `(a ^ b) ^ c == a ^ (b ^ c)`
* Distributive law
  * `(a & b) | c == (a | c) & (b | c)`
  * `(a | b) & c == (a & c) | (b & c)`
  * `(a ^ b) & c == (a & c) ^ (b & c)`
* De Morgan's law
  * `~(a & b) == (~a) | (~b)`
  * `~(a | b) == (~a) & (~b)`
* Negative operation properties:
  * `-1 == ~0`
  * `-a == ~(a-1)`
* AND operation properties:
  * `a & 0 == 0`
  * `a & (-1) == a`
  * `a & (~a) == 0`
* OR operation properties:
  * `a | 0 == a`
  * `a | (~a) == -1`
* XOR operation:
  * `a ^ 0 == a`
  * `a ^ a == 0`
* Others:
  * The result of `a&(a-1)` change the last 1 in the binary representation of `a` to 0
    * Used to reset the last one bit
  * The result of `a&(-a)` (equivalent to `a&(~(a-1)))`) is to keep the last 1 of the binary representation of `a`, and set the remaining 1 to 0
    * Used to get the last 1 bit of a

## Use bit operation to optimize performance
### Comparison with usual operator
* Bitwise op(&, >>)
  * Operate directly at the bit level
  * Are faster at the CPU instruction level
  * Constant time and no division hardware involved
* Division/Modulo
  * Are slower, since they user the CPU's integer division unit
  * Typically 5-10x more expensive than bitwise op in compiled code(e.g. C++)
  * In language like python, the speed difference is smaller, because both are high-level integer operations wrapped in Python objects - so Python's overhead dominates

#### Equivalent Replacement
* For powers of two(i.e. 16)
```python
a % 16 == a & 15

a // 16 == a >> 4
```
* For non-powers of two // TODO: dig deeper later
  * Division: multiply by "magic constant" + shift
* Addition and Difference
> When a > b >= 0
```python
def a_plus_b(a, b): # a+b
    while b:
        a, b = a ^ b, (a & b) << 1
    return a
def a_subtract_b(a, b): # a-b
    while b:
        a, b = a ^ b, ((~a) & b) << 1
    return b
```
# Cheetsheets
## Reverse bit for a byte
```python
def reverseByte(byte):
    return (byte * 0x0202020202 & 0x010884422010) % 1023
```

## Get the rightmost byte
```python
n & 0xFF
```

## Get a binary number of length k that is all 1s
```python
(1 << k) - 1
```

## Get common prefix of two number
> Shift both numbers to the right until they become equal
```python
def get_common_prefix(m, n):
  shift = 0
  while m != n:
    m >>= 1
    n >>= 1
    shift += 1
  return m << shift
```
## Number of valid bits
* for cpp
`__builtin_popcount(mask)`
* Any language: precompute(O(N)) using `count[i] = count[i//2] + (i % 2 == 1)`
## Bitmasking DP related
* Get i-th bit in the state x
``(x>>i) & 1``
* Check if x is a subset of y
``(x&y) == x``
* Check if there are no adjacent valid status in x
``(x&(x>>1))== 0``