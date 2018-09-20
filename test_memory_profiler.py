# from memory_profiler import profile
import os

@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2*10**7)
    del b
    return a

@profile
def function():
    lst = []
    for i in range(1000000):
        lst.append(i)
    return lst

def function_with_shortcut():
    lst = []
    append = lst.append
    for i in range(1_000_000):
        append(i)
    return lst

def function_list_comprehension():
    return [i for i in range(1_000_000)]

def function_convert_to_list():
    return list(range(1_000_000))


if __name__ == '__main__':
    for i in range(10):
        my_func()
