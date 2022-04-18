def dictionary_to_list(my_dict):
    keys_list = my_dict.keys()
    new_list =[]
    for i in keys_list:
        temp_list = []
        temp_list.append(i)
        for j in my_dict.get(i):
            temp_list.append(j)
        new_list.append(temp_list)
    print(new_list)


dict = {"HuEx": [1, 3, 4], "is": [7, 6], "best": [4, 5]}
dictionary_to_list(dict)

