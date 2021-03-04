a = '123'
b= ' de Oliveira 4'

print(a + b)
print(a.__add__(b))


print(len(a))
print(b.__len__())

print('1' in a)
print(a.__contains__('1'))