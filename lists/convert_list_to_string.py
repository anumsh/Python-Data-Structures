# How To Convert A List To A String

# String List 
stringList=["anum","kamal","lalit","surya","arjun"]

# converting list to string
namesinstring="".join(stringList)
print namesinstring


# Number List
numberList=[1,2,3,4,5,6]


# converting list into number
numberstring="".join(str(n) for n in numberList)
print numberstring

"""
output:
anumkamallalitsuryaarjun
123456

"""
