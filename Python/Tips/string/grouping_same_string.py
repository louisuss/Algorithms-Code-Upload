from collections import defaultdict

lst = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 정렬해서 비교
def group_anagram(lst):
    anagrams = defaultdict(list)

    # 문자를 정렬해서 키로 설정 후 같은 키 값끼리 추가
    for word in lst:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()

print(group_anagram(lst))