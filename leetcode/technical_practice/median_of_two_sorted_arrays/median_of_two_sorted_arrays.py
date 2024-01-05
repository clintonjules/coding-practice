def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    both = nums1 + nums2
    both.sort()

    length = (len(both)-1)

    return both[math.ceil(length / 2)] if len(both) % 2 != 0 else \
        (both[math.ceil(length / 2)] + both[length // 2]) / 2
