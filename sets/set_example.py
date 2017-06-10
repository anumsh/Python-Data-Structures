s = set([1,2,3])
print s # set([1, 2, 3])

# Sets cannot have duplicate members
s1=set(["I", "was", "a", "child", "and", "she", "was", "a", "child"])
print s1 #set(['a', 'and', 'I', 'she', 'child', 'was'])

#We can make a set in two ways: set([]) or {[]}

s2 = {1, 2.0, 'three', (4,5)}

print s2 #set([(4, 5), 1, 2.0, 'three'])

#Basic operations of a set

List = [1,2,3]
set3=set(List)
print set3 #set([1, 2, 3])

s4 = set() # empty set
print s4 #set([])

s4.add("anum")  # adding single member at a time
s4.add("sharma")
print s4 # set(['sharma', 'anum'])

# ading multiple members
s4.update(["udacity","Nanodegrees"])
print s4 # set(['udacity', 'sharma', 'Nanodegrees', 'anum'])
