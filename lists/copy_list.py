# How To Clone Or Copy A List in Python
import copy as c   # import copy libabry as c

numbers=[2,3,4,5,6,7]

# 1st method - slice

newList=numbers[:]

print newList

# 2nd method- list()

newList2=list(numbers)

print newList2

# 3rd method - copy()

newList3=c.copy(numbers)

print newList3

# If your list contains objects and you want to copy those as well,
# you can use copy.deepcopy(): copy.deepcopy(oldList)

# This is your list
objectList = ['a','b',['ab','ba']]

# Copy the `objectList`
copiedList = objectList[:]

# Change the first list element of `copiedList`
copiedList[0] = 'c'

# Go to the third element (the nested list) and change the second element
copiedList[2][1] = 'd'

# Print out the original list to see what happened to it
print(objectList)   #  ['a', 'b', ['ab', 'd']]
