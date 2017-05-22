# example - 1
print list(range(-5,5))   # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

print list(filter((lambda x: x <0), range(-5,5)))  # [-5, -4, -3, -2, -1]
 
# example-2

a = [1,2,3,5,7,9]
b = [2,3,5,6,7,8]
print filter(lambda x: x in a, b)  # prints out [2, 3, 5, 7]
