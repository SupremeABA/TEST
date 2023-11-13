# найти номер строки с мах суммой
import random
arr = [[random.randint(-100,100)for j in range(5)]for i in range(5)]
print(arr)
sum = 0
maxsum = 0
index = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum+=arr[i][j]
        print(sum)


    
