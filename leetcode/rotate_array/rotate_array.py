def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if k <= len(nums):
        a = nums[-k:]
        b = nums[:len(nums)-k]

        nums[:k] = a
        nums[k:] = b

    else:
        extra = k % len(nums)

        a = nums[len(nums)-extra:]
        b = nums[:len(nums)-extra]

        nums[:k] = a
        nums[k:] = b
