def removeElement(self, nums: List[int], val: int) -> int:
    val_count = nums.count(val)
    k = len(nums) - val_count

    for each in range(val_count):
        nums.remove(val)

    return k
