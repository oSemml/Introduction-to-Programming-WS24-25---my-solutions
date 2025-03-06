# Assume each list contains every element only once

# Create a list containing elements that are in both list1 and list2
def intersection(list1, list2):
    output = [x for x in list1 if x in list2]
    return output

# Create a list that contains all elements from list1 and any elements from list2 that are not already in list1
def union(list1, list2):
    output = list1 + [x for x in list2 if x not in list1]
    return output