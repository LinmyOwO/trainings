import functools


# decorators
def null_decorator(func):
    return func


def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: calling {func.__name__}() '
              f'with {args}, {kwargs}')
        original_result = func(*args, **kwargs)

        print(f'TRACE: {func.__name__}() '
              f'returned "{original_result}"')

        return original_result
    return wrapper


# functions
@null_decorator
@uppercase
def greet():
    return "Hello, World!"


@trace
def say(name, words):
    return f'{name}: {words}'


say("Mike", "I want cookies")
