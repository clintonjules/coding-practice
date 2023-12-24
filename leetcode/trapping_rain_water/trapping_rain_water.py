def trap(self, height: List[int]) -> int:
    # Instead of thinking of everything all at once,
    # Only care about the amount of water above each height value
    amount = 0

    for i in range(1,len(height)-1):
        max_possible_height = min(max(height[:i]), max(height[i:]))

        amount += max_possible_height - height[i] if max_possible_height > height[i] else 0

    return amount
