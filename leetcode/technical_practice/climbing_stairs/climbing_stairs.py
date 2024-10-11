def climbStairs(self, n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 2

    cache = [1, 2]

    for i in range(2,n):
        cache.append(cache[i-2] + cache[i-1])

    return cache[n-1]
