"""
Description:
Given an equation, represented by words on the left side and the result on the right side.
You need to check if the equation is solvable under the following rules:
Each character is decoded as one digit (0 - 9).
No two characters can map to the same digit.
Each words[i] and result are decoded as one number without leading zeros.
Sum of numbers on the left side (words) will equal to the number on the right side (result).
Return true if the equation is solvable, otherwise return false.

Intuition
Backtracking all the possible solutions:
State: for the ith digit, considering the current word w.
Optimize using early return:
if the sum of the current digit is different from the digit of the result
then its definitely invalid
"""


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # generate from the last digit, to enable early stop
        # backtrace on both digit and word
        max_len = max([len(w) for w in words + [result]])
        if len(result) < max_len:  # the result has to be the longest
            return False

        def get_char(d, word):
            pos = len(word) - 1 - d
            if pos < 0:
                return ""
            return word[pos]

        def sum_digits(d, carry, encoder):
            res = carry
            for word in words:
                c = get_char(d, word)
                if not c:
                    continue
                res += encoder[c]
            return res

        def leading_zero(encoder):
            # if single digit, 0 is valid
            c = result[0]
            if encoder[c] == 0 and len(result) > 1:
                return True
            for w in words:
                c = w[0]
                if encoder[c] == 0 and len(w) > 1:
                    return True
            return False

        def verify(d, w, carry, encoder, all_digits):
            if d >= max_len:  # done encoding the full fomular, check no leading zero and no carry on the left
                # print("verifying", d, w, carry, encoder)
                return not carry and not leading_zero(encoder)

            if w == len(words):  # set for this digit
                left = sum_digits(d, carry, encoder)
                c = get_char(d, result)
                # print("set for digit", d, left, c, carry, encoder)
                if c in encoder:
                    if left % 10 != encoder[c]:
                        return False
                    # this digit is valid, check the next digit
                    return verify(d + 1, 0, left // 10, encoder, all_digits)
                else:
                    # try all all posible digits
                    for n in all_digits.copy():
                        encoder[c] = n
                        all_digits.remove(n)
                        v = verify(d, w, carry, encoder, all_digits)
                        if v:
                            return True
                        del encoder[c]
                        all_digits.add(n)
                    return False

            c = get_char(d, words[w])
            if not c:
                return verify(d, w + 1, carry, encoder, all_digits)
            if c in encoder:  # known encoder
                return verify(d, w + 1, carry, encoder, all_digits)

            # try out all possible encoder for word[i]
            for n in all_digits.copy():
                encoder[c] = n
                all_digits.remove(n)
                v = verify(d, w + 1, carry, encoder, all_digits)
                if v:
                    return True
                # reset
                del encoder[c]
                all_digits.add(n)

            return False

        all_digits = set([i for i in range(10)])
        return verify(0, 0, 0, {}, all_digits)
