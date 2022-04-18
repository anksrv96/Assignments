def merge_two_lists(lst1, lst2):
    resultant_list = []
    for i in lst1:
        for j in lst2:
            resultant_list.append(i+j)

    print(resultant_list)


list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
merge_two_lists(list1, list2)
