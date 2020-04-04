
# first case

def decorator_list(fnc):
    def inner(list_of_tuples):
        return [fnc(val[0], val[1]) for val in list_of_tuples]
    return inner

@decorator_list
def add_together(a, b):
    return a + b

print(add_together([(1, 3), (2, 3)]))


# second case, with parameters in the decorator

def meta_decorator(power):
    def decorator_list(fnc):
        def inner(list_of_tuples):
            return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
        return inner
    return decorator_list

@meta_decorator(2)
def second_add_together(a, b):
    return a + b

print(second_add_together([(1, 3), (2, 3)]))