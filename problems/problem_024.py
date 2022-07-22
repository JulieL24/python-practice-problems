# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    num_of_num = len(values)
    total = sum(values)
    if values == []:
        return None
    else:
        return total / num_of_num


list = [1,2,3,4,5,6]
list1 = [10,20]
print(calculate_average(list))
print(calculate_average(list1))