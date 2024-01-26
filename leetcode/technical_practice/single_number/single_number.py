def singleNumber(self, nums: List[int]) -> int:
    cache = {}

    for n in nums:
        if n in cache.keys():
            cache[n] += 1

        else:
            cache[n] = 1

    return list(cache.keys())[list(cache.values()).index(1)]
