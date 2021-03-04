from decimal import Decimal, getcontext

print(Decimal(1.1) + Decimal(2.2))

getcontext().prec = 3 # estou definindo o número de casas máximo do resultado.

print(Decimal(1.1) + Decimal(2.2))

#print(dir(Decimal))
#print(dir())