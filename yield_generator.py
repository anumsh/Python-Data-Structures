# yield

"""
The yield enables a function to comeback where it left off when it is called again.
The yield keyword helps a function to remember its state.
"""

# example
"""
The function have 3 yields and it is iterated over 3 times, and each time it comes
back to the next execution line in the function not starting
from the beginning of the function body.
"""
def foo_with_yield():
    yield 11
    yield 25
    yield 37

# iterative calls
for yield_value in foo_with_yield():
    print yield_value,   # 11 25 37

# what actually returns is a generator object.

def foo_with_yield():
    yield 100
    yield 200
    yield 300

x=foo_with_yield()
print x
# The next() function takes a generator object and returns its next value
print next(x)
print x
# Repeatedly calling next() with the same generator object resumes exactly where it left off
#and continues until it hits the next yield statement.
print next(x)
print x
#All variables and local state are saved on yield and restored on next().
print next(x)

"""
output:
 <generator object foo_with_yield at 0xb606f70c>
100
<generator object foo_with_yield at 0xb606f70c>
200
<generator object foo_with_yield at 0xb606f70c>
300
"""

# Generators- Generators are closely tied with the iteration protocol
# generator looks like a function but behaves like an iterator.

def create_counter(n):
           print('create_counter()')
           while True:
                        yield n
                        print('increment n')
                        n += 1
		
c = create_counter(2)
print c
print next(c)
print next(c)
print  next(c)

"""
output
<generator object create_counter at 0xb578a7d4>
create_counter()
2
increment n
3
increment n
4
"""
