import time


def runtime_calculator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")

    return wrapper_function


@runtime_calculator
def fast_function():
    for i in range(10000000):
        i * i


@runtime_calculator
def slow_function():
    for i in range(100000000):
        i * i


if __name__ == "__main__":
    current_time = time.time()
    fast_function()
    slow_function()
