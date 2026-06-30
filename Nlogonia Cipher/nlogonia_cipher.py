# Define alphabet, consonants and vowels
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n",
             "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

vowels = ["a", "e", "i", "o", "u"]

# Find next vowel in alphabet
def close_vowel(letter):
    idx = alphabet.index(letter)
    sml_dist = None
    cls_vowel = None

    for v in vowels:
        dist = abs(idx - alphabet.index(v))
        if sml_dist is None or sml_dist > dist:
            sml_dist = dist
            cls_vowel = v

    return cls_vowel

# Find next consonant in alphabet
def next_consonant(letter):
    if letter == "z":
        return letter
    
    else:
        idx = consonants.index(letter)

        nxt_consonant = consonants[idx + 1]
        return nxt_consonant

# Call word input
word = input("Input: ")

# Look every letter from the word individually 
new_word = ""
for letter in word:
    if letter in consonants:
        new_word += letter + close_vowel(letter) + next_consonant(letter)
    
    elif letter in vowels:
        new_word += letter
    
print(f"Output {new_word}")
