# Complete the remove_duplicate_letters that takes a string
# parameter "s" and returns a string with all of the
# duplicates removed.
#
# Examples:
#   * For "abc", the result is "abc"
#   * For "abcabc", the result is "abc"
#   * For "abccba", the result is "abc"
#   * For "abccbad", the result is "abcd"
#
# If the list is empty, then return the empty string.

def remove_duplicate_letters(s):
    if s == "":
        return []
    list1 = []
    new_list = list(s)
    for str in new_list:
        if str not in list1:
            list1.append(str)
    return "".join(list1)


print(remove_duplicate_letters("hello"))
print(remove_duplicate_letters("ball"))