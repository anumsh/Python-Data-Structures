# hashing
import hashlib
"""
Dictionaries in Python are implemented using hash tables.
It is an array whose indexes are obtained using a hash function on the keys.
"""
# empty dictionary
D={}
# add elements
D['a']=1
D['b']=2
D['c']=3
print D   # {'a': 1, 'c': 3, 'b': 2}

# looping through the hash table
for k,v in D.items():
           print k,":",v

"""
output:
a : 1
c : 3
b : 2
"""

# hashing from 2 arrays

keys=['a','s','f']
values=[1,2,3]
hash={k:v for k,v in zip(keys,values)}
print hash

"""
Python provides hashlib for secure hashes and message digests:
md5(), sha*()
"""
# import hashlib
print hashlib.md5("union") #<md5 HASH object @ 0xb6085660>
print hashlib.md5("union").hexdigest()  # aa252f7bcbb4b8379004aa0c7cf76c10
