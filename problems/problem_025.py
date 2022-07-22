# Complete the calculate_sum function which accepts
# a list of numerical values and returns the sum of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#

def calculate_sum(values):
    if values == []:
        return None
    return sum(values)


list = [1, 2, 3, 4]
print(calculate_sum(list))