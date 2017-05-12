#  Write a Python script to sort (ascending and descending) a dictionary by value

import operator

d = {1:2 , 3:4 , 4:3, 2:1, 0:0}

print ('original dictionary: ',d)

sorted_d = sorted(d.items(), key=operator.itemgetter(0))

print ('dictionary in ascending order by value :',sorted_d)

sorted_d = sorted(d.items(), key=operator.itemgetter(0),reverse=True)

print ('dictionary in ascending order by value :',sorted_d)


"""
output:

('original dictionary: ', {0: 0, 1: 2, 2: 1, 3: 4, 4: 3})
('dictionary in ascending order by value :', [(0, 0), (1, 2), (2, 1), (3, 4), (4, 3)])
('dictionary in ascending order by value :', [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)])

"""
