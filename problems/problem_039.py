# Complete the reverse_dictionary function which has a
# single parameter that is a dictionary. Return a new
# dictionary that has the original dictionary's values
# for its keys, and the original dictionary's keys for
# its values.
#
# Examples:
#   * input:  {}
#     output: {}
#   * input:  {"key": "value"}
#     output: {"value", "key"}
#   * input:  {"one": 1, "two": 2, "three": 3}
#     output: {1: "one", 2: "two", 3: "three"}

def reverse_dictionary(dictionary):
    newDict = {val: key for key, val in dictionary.items()}
    return newDict


prob = {"key": "value"}
prob1 = {}
prob2 = {"one": 1, "two": 2, "three": 3}

print(reverse_dictionary(prob))
print(reverse_dictionary(prob1))
print(reverse_dictionary(prob2))

