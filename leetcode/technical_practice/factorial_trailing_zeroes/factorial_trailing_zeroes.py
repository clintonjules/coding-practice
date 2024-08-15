import math
import sys

class Solution:
    def trailingZeroes(self, n: int) -> int:
        sys.set_int_max_str_digits(0)
        
        fact = str(math.factorial(n))[::-1]

        count = 0
        for each in fact:
            if each == '0':
                count += 1

            else:
                break

        return count
