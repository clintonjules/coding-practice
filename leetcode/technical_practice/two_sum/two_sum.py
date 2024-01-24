# Bloomberg

def twoSum(self, nums: List[int], target: int) -> List[int]:
    cache = []

    for i, n in enumerate(nums):
        cache.append(n)

        check = target - n
        if check in cache and cache.index(check) != i:
            return [i, cache.index(check)]

    return [] 
