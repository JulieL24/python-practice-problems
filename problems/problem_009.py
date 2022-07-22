# Complete the is_palindrome function to check if the value in
# the word parameter is the same backward and forward.
#
# For example, the word "racecar" is a palindrome because, if
# you write it backwards, it's the same word.

# It uses the built-in function reversed and the join method
# for string objects.

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

#

    #return word[::-1]
    # return word.reverse()
    # for each letter in word we need to compare them 
    # compare length of word
    # if each letter in word2 

def is_palindrome(word):
    word1 = list(word)
    # print(word1)
    palindrome = True
    word2 = list(reversed(word))
    #print(word2)
    for str in word1:
        for str2 in word2:
         #   print(str2)
            if str == str2:
                is_palindrome = True
            elif str != str2:
                is_palindrome = False
    return is_palindrome
       

# print(is_palindrome("cat"))
print(is_palindrome("cat"))
print(is_palindrome("racecar"))