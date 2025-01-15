def log_decorator(func):
    def inner():
        print("This comes from decorator")
        func()
        print("This comes after the fonction")
    return inner
 
@log_decorator
def function_test():
    print("Cette fonction ne prend pas d'arguments.")

function_test()
