# Write a function that meets these requirements.
#
# Name:       shift_letters
# Parameters: a string containing a single word
# Returns:    a new string with all letters replaced
#             by the next letter in the alphabet
#
# If the letter "Z" or "z" appear in the string, then
# they would get replaced by "A" or "a", respectively.
#
# Examples:
#     * inputs:  "import"
#       result:  "jnqpsu"
#     * inputs:  "ABBA"
#       result:  "BCCB"
#     * inputs:  "Kala"
#       result:  "Lbmb"
#     * inputs:  "zap"
#       result:  "abq"
#
# You may want to look at the built-in Python functions
# "ord" and "chr" for this problem

def shift_letters(str):
    newStr = ""
    for letter in str: 
        if letter == "Z":
            newStr += "A"
        elif letter == "z":
            newStr += "a"
        else: 
            num = ord(letter) + 1
            newStr += chr(num)
    return newStr

print(ord("Z"))
print(ord("A"))
print(shift_letters("import"))
print(shift_letters("Zahara"))