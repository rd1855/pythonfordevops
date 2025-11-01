set_of_nums = {} #empty dictionary
print(type(set_of_nums))

set_of_nums = {None} #set with one element None
print(type(set_of_nums))

set1 = {11,1,1,1,1,2,2,2,3,3,4,5,5,4,3,2,1}
set2 = {1,1,1,2,4,54,6,8,7,5,3,2,1}

print(set1.intersection(set2)) #common elements in both sets
print(set1.union(set2)) #combines unique elements from both sets
print(set1.difference(set2)) #elements in set1 but not in set2
print(set2.difference(set1)) #elements in set2 but not in set1

#Removing the duplicates form the list using set
list_with_dups = [1,2,3,4,5,5,4,3,2,1,1,2,3,4,5]
print("List with duplicates:", list_with_dups)
list_with_dups = list(set(list_with_dups))
print("List after removing duplicates:", list_with_dups)
