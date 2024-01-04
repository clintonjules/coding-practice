def removeDuplicates(self, nums: List[int]) -> int:
    s = list(set(nums))
    s.sort()

    for i, each in enumerate(s):
        nums[i] = each

    return len(s)
