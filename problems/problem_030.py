# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    sorted_list = sorted(values)
    return sorted_list[len(sorted_list)-2]

    
#     largest = 0
#     second_largest = 0
#     if values == [] or len(values) == 1:
#         return None
#     for num in values:
#         if num >= largest:
#             second_largest = largest
#             largest = num
#     return second_largest

number2 = [5, 7, 10, 8]
numbers1 = [20, 43, 50, 5, 6]
print(find_second_largest(number2))
print(find_second_largest(numbers1))