
def print_duplicates(matrix):
    for i in matrix:
        print_for_current_row(i)


def print_for_current_row(lst):
    occurences = {}
    for i in lst:
        occurences[i] = lst.count(i)
    all_keys = occurences.keys()
    for i in all_keys:
        if occurences[i] > 1:
            print(i, "->", occurences.get(i), end='   ')
    print()


list_of_list = [[1, 1, 3, 2], [9, 8, 8, 1], [0, 4, 5, 0, 0, 1, 4]]
print_duplicates(list_of_list)
