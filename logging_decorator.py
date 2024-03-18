# inputs = eval(input("Enter"))
# ToDo: Create the logging_decorator() function


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print(f"Function name: {function.__name__} ,args: {args},kwargs: {kwargs}")
        print(f"Result: {function(*args, *kwargs)}")

    return wrapper


# ToDo: Use the decorator


@logging_decorator
def a_function(a, b, c):
    return a * b * c


if __name__ == "__main__":
    a_function(1, 2, 3)
    a_function(5, 6, 7)
