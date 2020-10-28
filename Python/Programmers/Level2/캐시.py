from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cities = [city.lower() for city in cities]

    if cacheSize == 0:
        return 5*len(cities)

    lst = deque()

    for city in cities:
        if len(lst) == cacheSize:
            if city in lst:
                lst.remove(city)
                lst.append(city)
                answer += 1
            else:
                lst.popleft()
                lst.append(city)
                answer += 5
        else:
            if city in lst:
                lst.remove(city)
                lst.append(city)
                answer += 1
            else:
                lst.append(city)
                answer += 5

    return answer
