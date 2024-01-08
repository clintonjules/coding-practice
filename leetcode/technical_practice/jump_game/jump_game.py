def canJump(self, nums: List[int]) -> bool:
    if len(nums) == 1:
       return True

    start = len(nums)-2

    # Check if can make to end or to the prev one that can make it tot he goal
    can_goal = len(nums) -1

    for i in range(start,-1,-1):
        if (nums[i] >= (len(nums)-1) - i) or (nums[i] >= can_goal - i):
        
            can_goal = i

    return True if can_goal == 0 else False
