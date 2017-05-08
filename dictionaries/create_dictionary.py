# how to create dictionary

# empty dictionary

dict1= {}

# dictionary with  integer keys
dict2= {1:  'anum', 2: 'sharma'}

# dictionary with mixed keys

dict3= {'name':'anum', 1: [2,3,4]}

# dict()

dict4= dict({1:'anum',2:'sharma'})

# from sequence having each item as a pair

dict5= dict([(1,'anum'),(2,'sharma')])

print dict1     # {}
print dict2     # {1: 'anum', 2: 'sharma'}
print dict3     # {1: [2, 3, 4], 'name': 'anum'}
print dict4     # {1: 'anum', 2: 'sharma'}
print dict5     # {1: 'anum', 2: 'sharma'}
