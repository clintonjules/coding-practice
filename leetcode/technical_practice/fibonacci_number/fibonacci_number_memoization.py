def fib(self, n: int) -> int:
    if n == 0:
        return 0

    # Use n+1 to include 0 also
    cache = [None] * (n + 1)
    cache[0] = 0
    cache[1] = 1

    # Use n+1 since the range function excludes the upper limit
    for i in range(2,n+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]
