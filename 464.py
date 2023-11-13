results=[]

def logger(func):
    def wrapper(*args, **kwargs):
            result = func(*args,**kwargs)
            print(f'{func.__name__},args - {args,kwargs}')
            return result        
    return wrapper

@logger
def sum(a,b):
    return a+b

@logger
def hello():
    print('Hello world')
    return True

sum(10,56)
sum(20,44)
hello()
