# string features-

"""
every thing in python is an object. String is a object. Function is an object.
Modules are an object. Class is an object
even class instance is an object.
"""

# 1.  String Example

name="anumsharma"

print name  #  anumsharma


# 2. Length of String

print len(name)  # 10

# 3. fetch its components with indexing expressions:

print name[0]  # a
print name[6]  # a

#4. We can index backward, from the end.
# Positive indexes count from the left, and negative indexes count back from the right:
print name[-3]  # r
print name[len(name) -1]  # a

#5. slicing
# basic syntax:  s[start:end:jump/step]
# name=anumsharma
print name[1:4]                  # num
print name[:]                      # anumsharma
print name [:6]                  # anumsh
print name [5:]                  # harma
print name [::2]                 #ausam
print name [::-1]                # amrahsmuna   (reverse)
print name[2:9:2]             #usam 
print name[-8: :-1]           # una ( from back)

# 6. concatenation

a= "anum"
b= a + "'s choice"
print b  #  anum's choice

# 7. Repetition

forgive = "sorry"
repeat3times= forgive*3
print repeat3times    # sorrysorrysorry

#  8. Immutability

n= "Piya"
# n[0]="R"         (if we try to change the character value of n , it will give an error)
print n   #TypeError: 'str' object does not support item assignment

# you cann't change in-place after you create.
# # But we can run expressions to make new objects
b = "R" + n[1:]
print b   # Riya   so here b is new object 

# 9. Strings - Type-Specific Methods

S= "university"
print S.find('i')  #2

print S.replace("university","institute")   # institute

# 10. Split & Strip 

line = "aaa,bbb,ccc,ddd"
print line.split(",")            # ['aaa', 'bbb', 'ccc', 'ddd']

line2="   aaa,bbb,ggg,hhh     \n"
print line2.strip()              # aaa,bbb,ggg,hhh

# 11. Formatting
print '%s is programming %s' % ('python','language')  # python is programming language

print '{} is a programming {}'.format('python','language')   # python is programming language


