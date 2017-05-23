# decorators

"""
A decorator is a function that takes a function object as its argument,
and returns a function object, and in the process,
makes necessary modifications to the input function, possibly enhancing it.

Features:
Adds functionality of the function.
Modifies the behavior of the function.
"""
#example- Adding $ to the return value from price() function

def dollar(fn):
    def new(*args):
        return '$' + str(fn(*args))
    return new

@dollar
def price(amount, tax_rate):
    return amount + amount*tax_rate
   
print price(100,0.1)
