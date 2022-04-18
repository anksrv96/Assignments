def construct_dictionary(dict_1, dict_2):
    dict1.update(dict2)
    print (dict_1)


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
construct_dictionary(dict1, dict2)