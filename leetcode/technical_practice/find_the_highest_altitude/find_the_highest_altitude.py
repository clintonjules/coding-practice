def largestAltitude(self, gain: List[int]) -> int:
    altitudes = [0]

    for i, each in enumerate(gain):
        current = altitudes[i]

        altitudes.append(current + each)

    return max(altitudes)
