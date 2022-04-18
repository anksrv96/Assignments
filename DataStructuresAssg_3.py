def nested_list_manipulation(main_list, list_to_be_added):
    current_list = main_list
    new_list = []

    for i in range(len(main_list)):
        if type(i) is not list:
            new_list.append(main_list[i])
        else:
            main_list = main_list[i]
    for i in list_to_be_added:
        new_list.append(i)

    print(new_list)


list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sublist = ["h", "i", "j"]
nested_list_manipulation(list1, sublist)
