import functools


def start_end_decorator(func):
    def wrapper():
        print('Start')
        func()
        print('end')

    return wrapper


@start_end_decorator
def print_name():
    print('Alex')


print_name()


def decorator_arguments(func):
    def wrapper(*args, **kwargs):
        print('Start Args Decorator')
        result = func(*args, **kwargs)
        print('End Args Decorator')
        return result

    return wrapper


@decorator_arguments
def add5(x):
    return x + 5


print('\n\nError in name, fixed on next example\n\n')
print(help(add5))
print(add5.__name__)

# import functools

print('\nFix Decorator func name\n')


def decorator_arguments_fix_name(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start Args Decorator')
        result = func(*args, **kwargs)
        print('End Args Decorator')
        return result

    return wrapper


@decorator_arguments_fix_name
def add10(x):
    return x + 10


print(add10.__name__)

print('\n\nDecorator with arguments\n')


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f'Hello {name}')


greet("Fluf")


print('\n\nDecorator of decorator example\n')


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {func.__name__}({signature})')
        result = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {result!r}')
        return result
    return wrapper


@debug
@decorator_arguments_fix_name
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting


say_hello("Nil")



print('\n\nClass Decorator\n')


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_howdy():
    print('Howdy')

say_howdy()
say_howdy()


#Decorator Usage
# Time decorator
# Debug Decorator
# Check Decorator
# Register function - like plugin
# update states
