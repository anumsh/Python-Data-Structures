# Write a Python program to check if a given key already exists in a dictionary.

dd = {'a': 33, 'c': 89, 'b': 56, 'e': 44, 'd': 34, 'j': 50}

def is_key_present(x):
    if x in dd:
        print("key is present in the dictionary")
    else:
        print ("key is not present in the dictionary")

is_key_present("g")  # key is not present in the dictionary
is_key_present("a")     # key is present in the dictionary
