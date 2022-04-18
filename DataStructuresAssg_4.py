def construct_dictionary(keys, values):
    my_dict = dict()
    for i in range(len(keys)):
        my_dict.update({keys[i] : values[i]})
    print(my_dict)


list1 = ["Ten", "Twenty", "Thirty"]
list2 = [10, 20, 30]
construct_dictionary(list1, list2)
