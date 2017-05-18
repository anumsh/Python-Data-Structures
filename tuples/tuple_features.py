# Tuples in Python:

# tuples are immutable, we cannot replace or delete any of items.

# 1. Tuple Example

emptytuple=()         # empty tuple
print type(emptytuple)                      # <type 'tuple'>

t= ("3")
print type(t)                                          # <type 'str'>

t1=("2",)
print type(t1)                                         # <type 'tuple'>

t2=(1,2,3,4)
print t2             # (1, 2, 3, 4)

# 2. Length of tuple

print len(t2)                    #4

# 3. Concatenation
tt= t2 + (5,6,7)
print tt                         # (1, 2, 3, 4, 5, 6, 7)

# 4. Indexing and Slicing
print tt[3]                      #4

print tt[2:]                     # (3, 4, 5, 6, 7)
print tt[1:4]                    # (2, 3, 4)
print tt[:-1]                    # (1, 2, 3, 4, 5, 6)    one less from back

#5. callable methods
t3=('a','s','f','b','y','o','t','k','e','o','h','r','v','o')
print t3.index('t')   #6

print t3.count('o')   #3

#6. Tuples are immutable
#            t3[0]='A' (you will get type error if you try to change the values of character )

#7.  support mixed types and nesting

t4=(4,"mixed", ['f',6,'hh'])
print t4[0]         # 4

# t4.append(77)  ------> you will get error 

# 8. Tuples - Packing and Unpacking

# packing example

T5=1, 'a', [{'age':5,'name':'anil'}]
print T5    # (1, 'a', [{'age': 5, 'name': 'anil'}])

# unpacking example
a,b,c=T5
print a,b,c           # 1 a [{'age': 5, 'name': 'anil'}]
"""
Tuple unpacking requires that the list of variables
on the left has the same number of elements as the length of the tuple.

"""

