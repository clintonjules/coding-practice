def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    count = len(ransomNote)

    for letter in magazine:
        if letter in ransomNote:
            count -= 1
            ransomNote = ransomNote.replace(letter,'',1)
    
    return True if count == 0 else False
