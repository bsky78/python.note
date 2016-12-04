def log(func):
    def wrapper(*a,**b):
        print('call %s()' % func.__name__)
        return func(*a,**b)
    return wrapper

@log
def r():
    print('???')

r()