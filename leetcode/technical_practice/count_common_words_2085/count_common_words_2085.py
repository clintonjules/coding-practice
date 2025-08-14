class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        out = 0

        for word in words1:
            if words1.count(word) != 1:
                continue

            if word in words2 and words2.count(word) == 1:
                out += 1


        return out
