# Chapter 10

# 10-1
# Write a function called nested_sum that takes a list of lists of integers and adds up the
# elements from all of the nested lists. 

t = [[3,2],[5],[10,1,3]]

def nested_sum(nest):
    add = []
    total = 0
    for s in nest:
        add.append(sum(s))
    for s in add:
        total += s
    return total

# print(nested_sum(t))

# 10-2
# Write a function called csum that takes a list of numbers and returns the cumulative
# sum; that is, a new list where the ith element is the sum of the first i+1 elements from
# the original list.

addme = [1,2,3,4,8]

def csum(values):
    iterator = 0
    csum = []
    for s in values:
        iterator += s
        csum.append(iterator)
    return csum

# print(csum(addme))

# 10-3
# Write a function called middle that takes a list and returns a new list that contains all
# but the first and last elements.

def middle(mid):
    return mid[1:len(mid)-1]

# print(middle(addme))

# 10-4
# Write a function called chop that takes a list, modifies it by removing the first and last
# elements, and returns None.

def chop(mid):
    mid.pop()
    mid.pop(0)

# print(addme)

# 10-5
# Write a function called is_sorted that takes a list as a parameter and returns True if
# the list is sorted in ascending order and False otherwise.

sort_me = ['b','z','d']
sort_metoo = [1,0,3,4]

def is_sorted(things):
    copy = things[:]
    copy.sort()
    if copy == things:
        return True
    return False

print(is_sorted(sort_me))
print(is_sorted(sort_metoo))