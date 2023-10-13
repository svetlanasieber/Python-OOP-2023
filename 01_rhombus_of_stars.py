def printing_row(figure_size, row_size):
    for space in range(n - row_size):
        print(" ", end="")
    for star in range(1, row_size):
        print("*", end=" ")
    print("*")


def upper_part(figure_size):
    for row in range(1, figure_size + 1):
        printing_row(figure_size, row)


def bottom_part(figure_size):
    for row in range(figure_size - 1, 0, -1):
        printing_row(figure_size, row)


def rhombus(figure_size):
    upper_part(figure_size)
    bottom_part(figure_size)


n = int(input())
rhombus(n)
