n = int(input())

arr = []

for _ in range(n):
    input_data = input().split(' ')
    arr.append((int(input_data[0]), input_data[1]))

arr.sort(key=lambda x:x[0])

for i in arr:
    print(i[0],i[1])