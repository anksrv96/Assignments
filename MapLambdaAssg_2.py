

lst1 = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
list_occurence_of_a = list(map(lambda a : a.count("a")+a.count("A"), lst1))
print(list_occurence_of_a)