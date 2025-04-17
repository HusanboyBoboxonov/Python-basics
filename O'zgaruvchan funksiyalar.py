"""22-dars:*args va **kwargs.
Boboxonov Husanboy"""


# *args
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi += son
    return yigindi


print(summa(1, 2))  # Natija:3
print((summa(1, 3, 4, 5, 2)))  # Natija:15
print(summa(4, 5, 6, 7))  # Natija:22


def summa1(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)


print(summa1(1, 2))  # Natija:3
print((summa1(1, 3, 4, 5, 2)))  # Natija:15
print(summa1(4, 5, 6, 7))  # Natija:22

def summa1(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x + y + sum(sonlar)


print(summa1(1, 2))  # Natija:3
print((summa1(1, 3, 4, 5, 2)))  # Natija:15
print(summa1(4, 5, 6, 7))  # Natija:22


# print(summa1(4))  # Natija:TypeError: summa1() missing 1 required positional argument: 'y'

# **kwargs

def avto_info(kompanya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    malumotlar['kompanya'] = kompanya
    malumotlar['model'] = model
    return malumotlar


avto1 = avto_info("GM", "malibu", rang="qora", yil=2018)
avto2 = avto_info("Kia", "K5", rang="qizil", narhi=35000, yil=2020)

print(avto1)  # Natija:{'rang': 'qora', 'yil': 2018, 'kompanya': 'GM', 'model': 'malibu'}


"""AMALIYOT"""


# Istalgancha sonlarni qabul qilib, hujjat ko'paytmasini qaytaruvchi funksiya yozing
def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))  # Natija:120


# Talabalar haqida ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing.
# Talabaning va familiyasi samarali argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda boshqariladigan boshqa mumkin bo'lsin.

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism'] = ism
    kwargs['familiya'] = familiya
    return kwargs


talaba = talaba_info('olim', 'olimov', tyil=1995, fakultet='IT', yonalish='AT')
print(talaba)  # Natija:{'tyil': 1995, 'fakultet': 'IT', 'yonalish': 'AT', 'ism': 'olim', 'familiya': 'olimov'}
