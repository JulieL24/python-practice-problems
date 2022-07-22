# Complete the has_quorum function to test to see if the number
# of the people in the attendees list is greater than or equal
# to 50% of the number of people in the members list.

def has_quorum(attendees_list, members_list):
    fifty_percent = len(members_list) / 2
    if (len(attendees_list) >= fifty_percent):
        return True
    else:
        return False



list = ['Amy','Scott','Peter','Sam']
list2 = ['Amy','Scott','Peter','Sam','Jamie']
print(has_quorum(list,list2))
#print(has_quorum(22,50))