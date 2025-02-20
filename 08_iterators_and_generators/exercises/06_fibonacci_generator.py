def fibonacci():

    first = 0
    last = 1

    while True:
        yield first
        first, last = last, first + last


generator = fibonacci()
for i in range(5):
    print(next(generator))
