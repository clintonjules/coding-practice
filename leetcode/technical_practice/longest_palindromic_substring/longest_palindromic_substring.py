def longestPalindrome(self, s: str) -> str:
    # First check if string is empty
    # Check if there exists another letter of the same after the current index
    # Check following characters until it doesn't the reversed string
    # Can just jump to next instances of the beginning letter to see if the reversed string is the same
    if not s:
        return ''

    longest = s[0]

    for i,letter in enumerate(s):
        current = s[i+1:]

        if letter not in current:
            continue

        to_cmp = ''
        for j, l in enumerate(current):
            to_cmp = to_cmp + l

            if l == letter:
                tmp = str(l + to_cmp)
                rev = tmp[::-1]

                if rev == tmp:
                    if len(rev) > len(longest):
                        longest = rev

    return longest
