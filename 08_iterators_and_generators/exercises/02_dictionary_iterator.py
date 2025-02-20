class dictionary_iter:

    def __init__(self, my_dict: dict) -> None:
        self.my_dict = my_dict
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == len(self.my_dict) - 1:
            raise StopIteration

        self.idx += 1

        return list(self.my_dict.items())[self.idx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)
