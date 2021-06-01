"""
    - The Difference between arguments and parameters
    - Positional and keyword arguments
    - Default arguments
    - variable-length arguments (*args and **kwargs)
    - Container unpacking into function arguments
    - Local vs. global arguments
    - Parameter passing (by value or by reference)
"""

# - The Difference between arguments and parameters
def print_name(name):   # name -> parameter
    print(name)


print_name('Alex')     # 'Alex' -> argument


# - Positional and keyword arguments

def foo(a, b, c):
    print ( a, b, c)

#positional
foo(1,2,3)

#keyword arguments
foo(a=1, b=2, c=3)
foo(3, c=1, b=5)

#     - Default arguments
#  must be at the end
def foo2(a, b, c, d=4):
    print(a, b ,c ,d)


#     - variable-length arguments (*args and **kwargs)
def fooargs(a, b, *args, **kwargs):
    print('regular arguments')
    print(a, b)

    print('* start list of arguments')
    for arg in args:
        print(arg);

    print('** key value arguments , dictionary')
    for key in kwargs:
        print(key, kwargs[key])

fooargs(1,2, 3, 4, 5, six=6, sever=7)

#     - Container unpacking into function arguments
print('\n\ncontainer unpacking\n\n')

def foo_cont(a, b, c):
    print(a, b, c)


my_list = (1, 2, 3)
foo_cont(*my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
foo_cont(**my_dict)

