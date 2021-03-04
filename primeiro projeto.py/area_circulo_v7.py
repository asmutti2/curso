from math import pi


def circulo(raio):
    print('area_do_circulo', pi * float(raio) ** 2)


if __name__ == '__main__':
    raio = input("infrome o raio =")
    circulo(raio)
