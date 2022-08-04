# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]
import math 

def halve_the_list(list1):
    middleindex = math.ceil(len(list1) / 2)
    if len(list1) == 1:
        return list1
    list2 = list1[:middleindex]
    list3 = list1[middleindex:]
    return list2, list3

# def halve_the_list(input):                              # solution
#     return (                                            # solution
#         input[0:len(input) // 2 + (len(input) % 2)],    # solution
#         input[len(input) // 2 + (len(input) % 2):],     # solution
#     )                                                   # solution
                                                


# print(halve_the_list([1, 2, 3, 4]))
# print(halve_the_list([1, 2, 3]))
# print(halve_the_list([1]))
# print(halve_the_list([1,2,3,4,5]))

