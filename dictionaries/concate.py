# Write a Python program to concatenate following dictionaries to create a new one.

dict1={"a":33,"b":56}
dict2={"c":89,"d":34}
dict3= {"e":44,"j":50}

dict4={}

for d in (dict1, dict2, dict3) : dict4.update(d)
print dict4   #  {'a': 33, 'c': 89, 'b': 56, 'e': 44, 'd': 34, 'j': 50}
