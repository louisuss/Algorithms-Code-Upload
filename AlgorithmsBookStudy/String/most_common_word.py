from collections import Counter, defaultdict
import re

paragraph = input()
banned = ["hit"]


def mostCommonWord(p):
    words = [word for word in re.sub(
        r'[^\w]', ' ', p).lower().split() if word not in banned]
    counts = Counter(words)
    return counts.most_common(1)[0][0]
    # counts = defaultdict(int)
    # for word in words:
    #     counts[word] += 1
    # return max(counts, key=counts.get)


print(mostCommonWord(paragraph))
