# функция которая выводит на экоан строку символов(длина строки и символ является парам функции)
repeat = lambda l,s : s*l
l = int(input("введите длину->"))
s = input("введите строку->")
print(repeat(l,s))