n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1

print(count)

result = 0
for i in range(n+1):
    if i == 3:
        result += 3600
        continue
    for j in range(60):
        if '3' in str(j):
            result += 60
            continue
        for k in range(60):
            if '3' in str(k):
                result += 1
print(result)
