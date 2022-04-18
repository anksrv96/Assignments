lst1=[-1000, 500, -600, 700, 5000, -90000, -17500]

expectedList = list(map(lambda b : b*(-1),(list (filter(lambda a : a<0,lst1)))))

print(expectedList)