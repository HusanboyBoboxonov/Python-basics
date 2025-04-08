"""20-dars:FUNKSIYADA QIYMAT QAYTARISH.
Boboxonov Husanboy"""


def toliq_ism_yasa(ism, familya):
    """Tolliq ismni qaytaruvchi fuksiya"""
    toliq_ism = f'{ism} {familya}'
    return toliq_ism


talaba1 = toliq_ism_yasa('husanboy', 'boboxonov')
talaba2 = toliq_ism_yasa('inomjon', 'bozorboyev')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechigib keldi.")  # Natija:
# Darsga kelmagan talabalar: husanboy boboxonov va inomjon bozorboyev
# husanboy boboxonov darsga kechigib keldi.


def toliq_ism_yas(ism, familya, otasingi_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasingi_ismi:
        toliq_ism = f"{ism} {otasingi_ismi} {familya}"
    else:
        toliq_ism = f"{ism} {familya}"

    return toliq_ism.title()


talaba1 = toliq_ism_yas('husanboy', 'boboxonov')
talaba2 = toliq_ism_yas('inomjan', 'boboxonov', 'jorabekovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
print(f"{talaba1} darsga kechigib keldi.")  # Natija:
# Darsga kelmagan talabalar: Husanboy Boboxonov va Inomjan Jorabekovich Boboxonov
# Husanboy Boboxonov darsga kechigib keldi.

#
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


avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanik', 2016, 150000)
avtolar = [avto1, avto2]
for avto in avtolar:
    if avto['narh']:
        narh = avto['narh']
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")  # Natija:
# Qora Malibu. Narhi: Noma'lum
# Oq Gentra. Narhi: 150000

range

def oraliq(min, max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar


print(oraliq(1, 6))  # Natija:[1, 2, 3, 4, 5, 6]

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

print("\nSalonimizdagi avtolar:")
for avto in avtolar:
    if avto['narh']:
        avto['narh'] = narh
    else:
        avto['narh'] = "Noma'lum"
    print(f"{avto['rang'].title()}, {avto['model'].title()}, {'karobka'} karobka. Narhi:{'narh'}")

"""AMALIYOT"""


# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va
# telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing.
# Lug'atda foydalanuvchu yoshi ham bo'lsin.
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring.
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.

def shaxs_haqida(ismi, familya, tugilgan_yili, yoshi, email=None, manzil=None):
    malumotlar = {
        'ismi': ismi,
        'familya': familya,
        'tugilgan_yili': tugilgan_yili,
        'email': email,
        'manzil': manzil,
        'yoshi': yoshi
    }
    return malumotlar


shaxslar = []
while True:
    joriy_yil = 2025
    ism = input('Ismingini kiriting:')
    familya = input('Familyagizni kiriting:')
    tugilgan_yili = int(input('Tugilgan yilingini kiriting:'))
    email = input('Emailingini kiriting:')
    manzil = input('Turar joyigiz kiritng:')
    yoshi = joriy_yil - tugilgan_yili,
    shaxslar.append(shaxs_haqida(ism, familya, tugilgan_yili, yoshi, email, manzil))
    takrorlash = input("Yana kiritasizmi:(ha/yo'q)")
    if takrorlash == "yo'q":
        break
for shaxs in shaxslar:
    print(f"{shaxs['ism'].title()} {shaxs['familya'].title()}")


# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

def eng_katta(son1, son2, son3):
    son = 0
    if son1 > son2 > son3:
        son = son1
    elif son1 > son3 > son2:
        son = son1
    elif son2 > son3 > son1:
        son = son2
    elif son2 > son1 > son3:
        son = son2
    elif son3 > son2 > son1:
        son = son3
    elif son3 > son2 > son1:
        son = son3
    return son


#  son = son1
#     if son2 > son:
#         son = son2
#     if son3 > son:
#         son = son3
#     return son

print(eng_katta(4, 5, 6))

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini,
# perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing

from math import pi


def aylana_yuz_per(radus):
    aylan = {
        'radus': radus,
        'diyametr': radus / 2,
        'yuzasi': pi * radus * radus,
        'peremetr': 2 * pi * radus,
    }
    return aylan


print(aylana_yuz_per(5))

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

sonlar_tub = []


def tubmi(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def tubsonlar_oraliq(boshi, oxiri):
    while boshi < oxiri:
        if tubmi(boshi):
            sonlar_tub.append(boshi)
        boshi += 1
    return sonlar_tub


print(tubsonlar_oraliq(2, 7))

