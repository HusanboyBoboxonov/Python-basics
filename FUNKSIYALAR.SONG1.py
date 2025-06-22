"""24-dars:FUNSIYALAR SO'NGISOZ.
Boboxonov Husanboy"""

import math

# def nom(argument):
#     return ifoda

"""lambda argument1, argument2:ifoda = argument1+argument2"""

uzunlik = lambda pi, r: 2 * pi * r
print(uzunlik(math.pi, 10))  # Natija:62.83185307179586

kvadrat = lambda x, y: x ** y
print(kvadrat(3, 2))  # Natija:9


def daraja(n):
    return lambda x: x ** n


# kvadirat
kvadirat = daraja(2)

print(kvadirat(8))  # Natija: 64

# kub
kub = daraja(3)

print(kub(8))  # Natija: 512

print(f"3-ning kvadirati {kvadirat(3)} ga, kubi {kub(3)} ga teng")
# Natija: 3-ning kvadirati 9 ga, kubi 27 ga teng

"""map funksiya"""

from math import sqrt  # sqrt - kvadirat ildiz hisoblaydigan fuksiya

sonlar = list(range(11))
ildiz = list(map(sqrt, sonlar))
print(
    ildiz)  # Natija: [0.0, 1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979, 2.449489742783178, 2.6457513110645907, 2.8284271247461903, 3.0, 3.1622776601683795]


def daraja2(x):
    """Berilgan soning kvadiratini qaytaruvchi funksiya"""
    return x * x


print(list(map(daraja2, sonlar)))  # Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# lambda bilan ishlash

kvadrat1 = list(map(lambda x: x ** 2, sonlar))
print(kvadrat1)  # Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# for bilan ishlanilishi

kvadrat2 = []
for son in sonlar:
    kvadrat2.append(son ** 2)

print(kvadrat2)  # Natija: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# listlar bilan ishlash

a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x + y, a, b))
print(a_plus_b)  # Natija: [11, 13, 15]

"""filter funksiya"""
import random as r

sonlar3 = r.sample(range(100), 10)
print(sonlar3)  # Natija: [27, 3, 37, 61, 6, 25, 98, 90, 33, 95]


def juftmi(x):
    """x ning juft bo'lsa True, aksa holda False qaytaruvchi fuksiya"""
    return x % 2 == 0


juft_sonlar = list(filter(juftmi, sonlar3))
print(juft_sonlar)  # Natija: [6, 98, 90]

# lambda bilan ishlatish

juft_sonlar1 = list(filter(lambda son: son % 2 == 0, sonlar3))
print(juft_sonlar1)  # Natija: [6, 98, 90]

# matnlar bilan ishlash

mevalar = ['olma', 'anor', 'anjir', 'shaftoli', "o'rik", 'tarvuz', "qovun", "banan"]
harf = "b"
mevalr_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(mevalr_b)  # Natija: ['banan']


mevalar2 = list(filter(lambda meva: len(meva) < 5, mevalar))
print(mevalar2)  # Natija: ['olma', 'anor']

list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))