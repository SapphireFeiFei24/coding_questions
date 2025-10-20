"""
Reverse bits of a given 32 bits signed integer

Example
"00000010100101000001111010011100" -> "00111001011110000010100101000000"
"""

'''
Naive solution: reverse it bit by bit in a for loop
O(1) for both time and space complexity
'''
def reverse_bit_by_bit(n):
    ret, power = 0, 31
    while n:
        ret += (n & 1) << power
        n = n >> 1  # right shift one
        power -= 1  # move down one bit

    return ret

'''
Solution 2: Reverse byte by byte
'''
import functools
# memoization with decorator
@functools.lru_cache(maxsize=256)
def reverseByte(self, byte):  # a templte for reverse a byte
    return (byte * 0x0202020202 & 0x010884422010) % 1023
def reverseBits(self, n: int) -> int:
    ret, power = 0, 24
    while n:
        ret += reverseByte(n & 0xFF) << power  # n & 0xFF: to get the right most byte
        n = n >> 8
        power -= 8
    return ret

'''
Divide and Conquer(masking and shifting):
1. Divide original 32-bits into blocks with few bits using bit masking
2. Reverse each block via bit shifting
'''
def masking_and_shifting(num):
    # 32 -> 16 and switch
    num = (num >> 16) | (num << 16)
    # within each 16, 16 -> 8 and switch
    num = ((num & 0xFF00FF00) >> 8) | ((num & 0x00FF00FF) << 8)
    # within each 8, 8 -> 4 and switch
    num = ((num & 0xF0F0F0F0) >> 4) | ((num & 0x0F0F0F0F) << 4)
    # within each 4, 4-> 2 and switch
    # C in 4 bits: 1100, 3 in 4 bits: 0011
    num = ((num & 0xCCCCCCCC) >> 2) | ((num & 0x33333333) << 2)
    # within each 2, 2->1 and switch
    # A in 4 bits: 1010, 5 in 4 bits: 0101
    num = ((num & 0xAAAAAAAA) >> 1) | ((num & 0x55555555) << 1)
    return num



