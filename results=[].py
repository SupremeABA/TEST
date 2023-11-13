from datetime import datetime
def logger(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args,**kwargs)
            file = open(f'./log_{datetime.now().date()}.txt','a+')
            file.write(f'{func.__name__}-{datetime.now().strftime("%H:%M:%S")}\nresults={result}\n\n')
            file.close()
            return result
        except Exception as ex:
            file = open(f'./log_{datetime.now().date()}.txt','a+')
            file.write(f'{func.__name__}-{datetime.now().strftime("%H:%M:%S")}\nERROR={ex}\n\n')
            file.close()
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

