def multiply(self, num1: str, num2: str) -> str:
    total1, total2 = 0, 0

    for i, n in enumerate(num1[::-1]):
        n = ord(n) - 48
        total1 += (10**i) * n if i != 0 else n

    for i, n in enumerate(num2[::-1]):
        n = ord(n) - 48
        total2 += (10**i) * n if i != 0 else n

    return str(total1 * total2)
