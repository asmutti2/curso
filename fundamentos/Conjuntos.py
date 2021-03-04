a = {1, 2, 3}
print(type(a))
b = set('angelo mutti')
print(b)
print('a' in b, 'sousa' not in b)

# o que vale são os valores que compõem o conjunto, verdadeiro
print({1, 2, 3} == {3, 2, 1, 3, 2})

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)


c3 = {1, 2, 3, 4, 5, 6}
c4 = {7, 8, 9, 10, 11, 12}
c3.update(c4)
print(c3)
print(c4)


print(c2 <= c1)

print(c1 - {2})

c1.union(c2)
print(c1)

# print(c1 -= {2})

rrr = set('1234567890')
# rrr = set(1234567890) # não funciona! por que?
print(rrr)
