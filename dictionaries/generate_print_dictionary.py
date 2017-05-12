# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).

n=5
d= {}  # or d=dict()

for x in range(1,n+1):
    d[x]=x*x

print(d)  #  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
