# The Python append() and extend() Methods

numbers=[1,2,3,4,5]

print numbers   # will print [1, 2, 3, 4, 5]

# append example
"""
adds its argument to the end of the list as a single item,
which means that when the append() function
takes an iterable as its argument, it will treat it as a single object.

"""
numbers.append([7,8])

print numbers  # will print [1, 2, 3, 4, 5, [7, 8]]


# extend example
"""
takes an iterable (it takes a list, set, tuple or string),
and adds each element of the iterable to the list one at a time.
"""
numbers.extend("anum")

print numbers  # will print [1, 2, 3, 4, 5, [7, 8], 'a', 'n', 'u', 'm']


# To concatenate lists, use  + operator

plusList=numbers + [22,33] 

print plusList  # will print  [1, 2, 3, 4, 5, [7, 8], 'a', 'n', 'u', 'm', 22, 33]
