n = int(input())

person = []
person_number = 0
for _ in range(n):
    age, name = input().split()
    age = int(age)
    person.append((age, person_number, name))
    person_number += 1

person.sort(key=lambda x: (x[0], x[1]))
for p in person:
    print(p[0], p[2])