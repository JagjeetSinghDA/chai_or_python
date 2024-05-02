import time 

def timer(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"{function.__name__} ran in {end_time - start_time}")
        return result
    return wrapper 

@timer
def example_function(n):
    time.sleep(n)

example_function(5)