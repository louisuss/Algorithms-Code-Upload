from collections import defaultdict

user_input = list(input().split())

def group_anagrams(s):
    anagrams = defaultdict(list)

    for word in s:
        # sorted(word) -> ['a', 'e', 't'] 같이 리스트 형태로 정렬됨 -> 문자열로 쓰기 위해서는 join으로 합쳐야함
        # print(sorted(word))
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(group_anagrams(user_input))