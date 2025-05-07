def decorator(func):
    def wrapper():
        print('I will let you know the func is about to  be called')
        func()
        print('I am the output that will let you lnow that the func has been called')
    return wrapper
@decorator
def get_called():
    print('I am the function and I am being called')

# get_called = decorator(get_called)
get_called()