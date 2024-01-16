def divide(self, dividend: int, divisor: int) -> int:
    if dividend == 0:
        return 0

    negative = ((dividend < 0) ^ (divisor < 0))

    dividend = abs(dividend)
    divisor = abs(divisor)

    quotient = len(range(0, dividend-divisor+1, divisor))

    output = -quotient if negative else quotient

    return min(max(-2147483648, output), 2147483647)
