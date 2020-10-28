test = int(input())
prime_list = list(map(int, input().split()))
total = 0
for i in range(test):
    cnt = 0
    if prime_list[i] == 1:
        continue
    for k in range(2, (int(prime_list[i]/2))+1):
        if prime_list[i] % k == 0:
            cnt+=1
    if cnt == 0:
        total+=1

print(total)

