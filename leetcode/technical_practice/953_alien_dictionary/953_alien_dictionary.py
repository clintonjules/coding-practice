def isAlienSorted(self, words: List[str], order: str) -> bool:
        rosetta = {}

        num = 0
        for o in order:
            rosetta[o] = num

            num += 1

        num_words = []
        
        for word in words:
            new_word = []
            for letter in word:
                new_word.append(rosetta[letter])

            num_words.append(new_word)

        for i in range(len(num_words)-1):
            if num_words[i] > num_words[i+1]:
                return False

            if num_words[i] == num_words[i+1]:
                if len(num_words[i]) > len(num_words[i+1]):
                    return False


        return True
