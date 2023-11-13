# функция сравнивает два целых числа
def cump (a,b):
    if a>b:
        return ">"
    elif a<b:
        return "<"
    else:
        return "="
print(cump(10,5))
print(cump(10,11))
print(cump(10,10))