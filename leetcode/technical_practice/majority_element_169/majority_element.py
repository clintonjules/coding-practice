def majorityElement(self, nums: List[int]) -> int:
        cache = {}

        for each in nums:
            if each in cache.keys():
                cache[each] += 1
            else:
                cache[each] = 0

        return max(cache, key=cache.get)
