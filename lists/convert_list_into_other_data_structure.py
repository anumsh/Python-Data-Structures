""" How To Convert A List To A Tuple
 How To Convert Your List To A Set In Python
 How To Convert Lists To A Dictionaries
"""

# list

numbers= [1,2,3,4,5,6,3,5,4,2,3,42,2,6,4,4,5,3,2,3]
print "lists= ",numbers

# convert list into tuple

numbers_in_tuple=tuple(numbers)
print "tuple= ",numbers_in_tuple

# convert list into set
number_in_set=set(numbers)

print number_in_set


# convert list into dictionary
helloWorld = ['hello','world','1','2']

# Convert to a dictionary
helloWorldDictionary = dict(zip(helloWorld[0::2], helloWorld[1::2]))

# Print out the result
print "dictionary= ",(helloWorldDictionary)



"""
Output:

lists=  [1, 2, 3, 4, 5, 6, 3, 5, 4, 2, 3, 42, 2, 6, 4, 4, 5, 3, 2, 3]
tuple=  (1, 2, 3, 4, 5, 6, 3, 5, 4, 2, 3, 42, 2, 6, 4, 4, 5, 3, 2, 3)
set([1, 2, 3, 4, 5, 6, 42])
dictionary=  {'1': '2', 'hello': 'world'}
"""
