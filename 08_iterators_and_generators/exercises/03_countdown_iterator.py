class countdown_iterator:

    def __init__(self, count: int):
        self.count = count
        self.iteration = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iteration == 0:
            raise StopIteration

        self.iteration -= 1

        return self.iteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

