def bottom_left_diamond(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or j == n or i == j:
                print("*", end=" ")
            else:
                print(end="  ")
        print()


bottom_left_diamond(8)
