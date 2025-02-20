def type_check(type_allowed):
    def decorated(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_allowed):
                    return "Bad Type"
            return func(*args)
        return wrapper
    return decorated


@type_check(int)
def times2(num):
    return num * 2


print(times2(4))
print(times2('Not A Number'))
