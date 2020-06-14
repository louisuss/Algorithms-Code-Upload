n = int(input())
sum = 1
count = 1
if n <= 1:
    print('1/1')

while n>1:
    count += 1
    sum = sum + count

    if sum >= n:
        sum = sum - count
        if count % 2 == 0:
            a = n - sum
            b = count + 1 - a
            print('{}/{}'.format(a,b))
            break
        else:
            a = n - sum
            b = count + 1 - a
            print('{}/{}'.format(b,a))
            break