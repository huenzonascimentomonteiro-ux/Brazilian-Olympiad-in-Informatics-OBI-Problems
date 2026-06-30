Nlogonia Cipher
The King of Nlogonia has ordered that all important documents be "encrypted" so that only those who know the cipher can read them (encrypting a document means altering the original by modifying the letters according to a specific encryption algorithm).

The King decreed that the following algorithm must be used to encrypt the documents:

Each consonant must be replaced by exactly three letters, in the following order:
the consonant itself (let's call it the original consonant);
the vowel closest to the original consonant in the alphabet, with the additional rule that if the original consonant is equidistant from two vowels, the vowel closer to the beginning of the alphabet is used. For example, if the original consonant is 'd', the vowel to be used is 'e', ​​as it is the closest vowel; if the original consonant is 'c', the vowel to be used is 'a', because 'c' is equidistant from 'a' and 'e', ​​and 'a' is closer to the beginning of the alphabet.
the consonant that follows the original consonant in alphabetical order. For example, if the original consonant is 'd', the consonant to be used is 'f'. If the original consonant is 'z', the letter 'z' itself is used.
Vowels are not modified.
For this task, the alphabet is
a b c d e f g h i j k l m n o p q r s t u v x z
and the vowels are
a e i o u
For example, the cipher for the word "ter" is "tuveros" (tuv-e-ros) and the cipher for the word "paz" is "poqazuz" (poq-a-zuz).

The King of Nlogonia is looking for someone who can write a program to generate the cipher for a given word. Can you help him?

Input:
The first and only line of the input contains a word P consisting of lowercase, unaccented letters.

Output:
Your program must produce a single line containing the encrypted word. Constraints
The word P consists of between 1 and 30 letters, all lowercase and without accents.
