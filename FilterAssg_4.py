from functools import reduce

myList = [2, 4, 6, 8, 10]
prod = reduce(lambda a, b: a*b, myList)
print(prod)
