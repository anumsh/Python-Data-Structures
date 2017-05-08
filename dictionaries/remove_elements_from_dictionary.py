# How to delete or remove elements from a dictionary?

# create a dictionary
squares = {1:1, 2:4, 3:9, 4:16, 5:25}

# remove particular item
print (squares.pop(4))    #  16

print squares       # {1: 1, 2: 4, 3: 9, 5: 25}

# remove arbitrary item

print (squares.popitem())  #  (1, 1)

print squares       # {2: 4, 3: 9, 5: 25}

# remove all items

squares.clear()

print squares          # {}

# delete the dictionary itself

del squares
