def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        elif n == 2:
            return 1

        else:
            cache = [0, 1, 1]

            for i in range(3, n+1):
                cache.append(cache[i-1] + cache[i-2] + cache[i-3])

            return cache.pop()
