# Write a Python program to remove a key from a dictionary.

my_dict={'a':1,'b':2,'c':3,'d':4}

print my_dict    # {'a': 1, 'c': 3, 'b': 2, 'd': 4}

if 'a' in my_dict:
    del my_dict['a']

print my_dict   #  {'c': 3, 'b': 2, 'd': 4}
