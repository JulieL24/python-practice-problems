# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    newlist = []
    if not is_sunny and is_workday:
        newlist.append("umbrella")
    if is_workday:
        newlist.append("laptop")
    else:
        newlist.append("surfboard")
    return newlist

print(gear_for_day(True,True))
print(gear_for_day(True,False))
