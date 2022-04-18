
def print_diamond_star_pattern(rows):
    for i in range(rows):
        for j in range(0, i + 1):
            print('*', end='')
        print()

    for i in range(1, rows):
        for j in range(i, rows):
            print('*', end='')
        print()


total_rows = 6
print_diamond_star_pattern(total_rows)
