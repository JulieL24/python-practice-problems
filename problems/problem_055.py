# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"

def simple_roman(number):
    if number == 1:
        return "I"
    elif number == 2:
        return "II"
    elif number == 3:
        return "III"
    elif number == 4:
        return "IV"
    elif number == 5:
        return "V"
    elif number == 6:
        return "VI"
    elif number == 7:
        return "VII"
    elif number == 8: 
        return "VIII"
    elif number == 9:
        return "IX"
    else: 
        return "X"


# def simple_roman(number):           # solution
#     lookup = {                      # solution
#         1: "I",                     # solution
#         2: "II",                    # solution
#         3: "III",                   # solution
#         4: "IV",                    # solution
#         5: "V",                     # solution
#         6: "VI",                    # solution
#         7: "VII",                   # solution
#         8: "VIII",                  # solution
#         9: "IX",                    # solution
#         10: "X",                    # solution
#     }                               # solution
#     return lookup[number]           # solution

