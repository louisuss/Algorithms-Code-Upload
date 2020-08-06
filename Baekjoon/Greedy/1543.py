user_input = input()
search = input()
cnt = 0
start = 0

while start+len(search) <= len(user_input):
    if user_input[start:start+len(search)] == search:
        start = start + len(search)
        cnt += 1
    else:
        start += 1

print(cnt)