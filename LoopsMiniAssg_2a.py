
def get_current_row (row, spaces):
    temp_row = str(11**row)
    for i in range(spaces):
        temp_row = temp_row+"0"
    return [char for char in temp_row]


def print_pascal_triangle(n):
    spaces = n-1
    for i in range(n):
        temp_row = get_current_row(i, spaces)
        for j in temp_row:
            print(j, end=' ')
        spaces = spaces-1
        print()


n = 3
print_pascal_triangle(n)

