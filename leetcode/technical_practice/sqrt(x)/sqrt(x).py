def mySqrt(self, x: int) -> int:
    # Using the repeated subtraction method
    count = 0
    i = 1

    while x >= 0:
        x -= i

        i += 2
        count += 1

    return count-1
