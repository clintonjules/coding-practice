    def strStr(self, haystack: str, needle: str) -> int:
        try:
            substring = haystack.index(needle)
        
            return substring
        except ValueError:
            return -1
