print(2 + 3)
print('2' + "3")

a = 2
b = '3'

print(type(a))
print(type(b))

print(a + int(b))

print(str(a) + b)

c = 3.4

print(float(a))

#print(-2(0.5))

a_x_b = a * int(b)

print(a_x_b)

print(1.1 + 2.2)

from decimal import Decimal, getcontext

print(Decimal(1.1) + Decimal(2.2))

getcontext().prec = 3

print(Decimal(1.1) + Decimal(2.2))