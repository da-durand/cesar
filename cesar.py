alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j","k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

word = "abc"
word2 = "nez"
code3 = "hello"

encrypted_word = ""

for i in range (len(word)):
    char = word[i]
    print(char)
    encrypted_word += alphabet[i + 5]

print(encrypted_word + "\n")

encrypted_word = ""

for i in range (len(word2)):
    char = word2[i]
    print(char)
    encrypted_word += alphabet[i + 5]

print(encrypted_word)

encrypted_word = ""