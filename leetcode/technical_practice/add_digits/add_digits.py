def addDigits(self, num: int) -> int:
    sum = 0

    while num != 0:
        sum += num % 10
        num = int(num / 10)
        
    if len(str(sum)) > 1:
        return self.addDigits(sum)

    return sum
