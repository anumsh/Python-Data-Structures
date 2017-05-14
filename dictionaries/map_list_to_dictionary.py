# Write a Python program to map two lists into a dictionary.

keys=['name','age','phone']
values=["anum",20,"333-578-0292"]
person_dictinary= dict(zip(keys,values))
print (person_dictinary)   # {'phone': '333-578-0292', 'age': 20, 'name': 'anum'}
