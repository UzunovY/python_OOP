def print_row(spaces, stars):
    print(" " * spaces + "* " * stars)


def print_upper_part(n):
    for row in range(1, n + 1):
        spaces = n - row
        stars = row
        print_row(spaces, stars)


def print_bottom_part(n):
    for row in range(1, n):
        spaces = row
        stars = n - row
        print_row(spaces, stars)


def print_rhombus(n):
    print_upper_part(n)
    print_bottom_part(n)


num = int(input())
print_rhombus(num)
