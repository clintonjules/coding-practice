def longestCommonPrefix(self, strs: List[str]) -> str:
    first = strs[0]
    output = ''

    if len(strs) == 1:
        return first

    for i in range(len(first)+1):
        to_cmp = first[:i]
        right = 0

        for each in strs[1:]:
            if to_cmp == each[:len(to_cmp)]:
                right += 1

        if right == len(strs[1:]):
            output = to_cmp


    return output
