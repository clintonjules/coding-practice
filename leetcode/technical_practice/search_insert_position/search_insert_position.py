def searchInsert(self, nums: List[int], target: int) -> int:
    middle = -(len(nums) // -2)

    if len(nums) == 1:
        if target > nums[0]:
            return 1
        else:
            return 0

    elif target >= nums[middle]:
        return self.searchInsert(nums[middle:], target) + middle

    else:
        return self.searchInsert(nums[:middle], target)
