# объединение и сортировка
# sort-сортировать
# extened-объединить
import random
arr = [random.randint(-100,100) for i in range(10)]
arr2 = [random.randint(-100,100) for i in range(10)]
print(arr)
print(arr2)
arr.sort()
arr2.sort()
print(arr)
print(arr2)
arr.extend(arr2)
print(arr)
arr.sort()
print(arr)
