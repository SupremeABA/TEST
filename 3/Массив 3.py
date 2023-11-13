import random
arr = [[random.randint(-100,100)for j in range(5)]for i in range(5)]
print(arr)
sum = 0
maxsum = 0
index = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        sum+=arr[i][j]
    if maxsum<sum:
        maxsum=sum
        index=i
    sum=0
print(f"номер строки с мах  суммой-{index}")        
    
