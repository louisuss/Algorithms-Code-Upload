str = input()
word = input()

idx = 0
result = 0
len_word = len(word)

while True:
    if len(str)-idx < len_word:
        break
    if str[idx:idx+len_word] == word:
        result += 1
        idx += len_word
    else:
        idx += 1
print(result)
