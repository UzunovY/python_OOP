def logged(func):
    def wrapper(*args):
        return f"you called {func.__name__}({', '.join(str(el) for el in args)})\nit returned {func(*args)}"

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
