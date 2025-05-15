"""23-dars:MODULLAR.
Boboxonov Husanboy"""

"""avto_info_mod"""


def avto_info(kompaniy, model, rang, karobka, yili, narh=None):
    avto = {
        'kompaniy': kompaniy,
        'model': model,
        'rang': rang,
        'karobka': karobka,
        'yili': yili,
        'narh': narh,
    }
    return avto


def avto_kirit():
    print("Saytimizdagi avtolar  ro'yxatini shakllantiramiz")
    avtolar = []
    while True:
        print("\nQuydagi ma'lumotlarni  kiriting:", end='')
        kompaniy = input("Ishlab chiqaruvchi:")
        model = input('Model:')
        rang = input('Rangi:')
        karobka = input('Karobka:')
        yili = input('Ishlab chiqrilgan yili:')
        narh = input('Narhi:')
        avtolar.append(avto_info(kompaniy, model, rang, karobka, yili, narh))
        javob = input("Yana avto qo'shizmi?(yes/no):")
        if javob != 'yes':
            break


def info_print(avto_info):
    print("\nSalonimizdagi avtolar:")
    print(f"{avto_info['rang'].title()}, {avto_info['model'].title()}, {'karobka'} karobka. Narhi:{'narh'}")


import math

x = 400
print(math.sqrt(x))  # Natija:20.0
print(math.pow(5, 2))  # Natija:25.0
print(math.pi)  # Natija:3.141592653589793
print(math.log2(8))  # Natija:3.0
print(math.log10(100))  # Natija:2.0


import random as r

# randint()
son = r.randint(0, 100)
print(son)  # Natija:84,28..

# Choice()
ismlar = ["olim", 'anavar', 'hasan', 'husan']
ism = r.choice(ismlar)
print(ism)  # Natija:anavar,husan..olim
print(r.choice(ism))  # Natija:l
x = list(range(0, 51, 5))
print(x)  # Natija:[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print(r.choice(x))  # Natija:15

# Shuffle()
x = list(range(11))
print(x)  # Natija:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r.shuffle(x)
print(x)  # Natija:[3, 7, 10, 6, 0, 4, 9, 1, 5, 2, 8]
