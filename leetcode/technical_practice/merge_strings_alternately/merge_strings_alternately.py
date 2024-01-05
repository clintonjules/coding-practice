def mergeAlternately(self, word1: str, word2: str) -> str:
    length = max(len(word1), len(word2))
    merged = ''

    if word1 == '' and word2 == '':
        return ''
    elif word1 != '' and word2 == '':
        return word1
    elif word1 == '' and word2 != '':
        return word2
    
    for i in range(length):
        if i <= len(word1)-1:
            # print(i, len(word1))
            merged = merged + word1[i]

        if i <= len(word2)-1:
            merged = merged + word2[i]

    return merged
