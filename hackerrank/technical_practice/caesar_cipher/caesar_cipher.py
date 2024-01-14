def caesarCipher(s, k):
    # Write your code here
    output = ''

    for letter in s:
        if not letter.isalpha():
            output += letter
            continue
            
        caesar_char = ord(letter) + (k % 26)
        print(caesar_char)
        if letter.islower() and caesar_char < 123:
            output += chr(caesar_char)
        elif letter.isupper() and caesar_char < 91:
            output += chr(caesar_char)
        else:
            output += chr(caesar_char - 26)
    
    return output
