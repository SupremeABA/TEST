dict = [100,60,70]
cofe =int(input("выберите кофе:\n1.Latte\n2.Espresso\n3.Americano\n->"))
total = dict[cofe-1]
mul = [1,1.5,2]
cofe = int(input("Выберите размер порции:\n1.Маленькая\n2.Средняя\n3.Большая\n->"))
total *= mul[cofe-1] 
print(f"Ваш кофе готов, стоимость  {total}")
