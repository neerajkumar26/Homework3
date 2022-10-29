# Name: - Neeraj Kumar
# ID: - 2047559

arr = input().split()
arr = [int(i) for i in arr]
result= []

for val in arr:
    if val>=0:
        result.append(val)
        pass

result.sort()
for i in range(len(result)):
    if i == len(result)-1:
        print(f'{result[i]}',end =" ")
    else:
        print(f'{result[i]} ',end='')

