
def my_func():
    a = [1] * (10**6)
    b = [2] * (2*10**7)
    del b
    return a


# slow 0.5
def my_function():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst


# a liiittle better 0.5
def function_with_shortcut():
    lst = []
    append = lst.append
    for i in range(1_000_000):
        append(i)
    return lst


# much better! 0.07
def function_list_comprehension():
    return [i for i in range(1_000_000)]


# even better ! 0.01
def function_convert_to_list():
    return list(range(1_000_000))


if __name__ == '__main__':
    my_function()
    function_with_shortcut()
    function_list_comprehension()
    function_convert_to_list()
