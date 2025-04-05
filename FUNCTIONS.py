"""19-dars:FUNCTIONS (FUNKSIYALAR).
Boboxonov Husanboy"""


def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")


salom_ber()  # Natija:Assalomu alaykum!


def salom_ber(ism):
    """Foydalanuching ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalomu alaykum, hurmatli {ism.title()}")


salom_ber('husan')
salom_ber('olim')  # Natija:
# Assalomu alaykum, hurmatli Husan
# Assalomu alaykum, hurmatli Olim

print(salom_ber.__doc__)  # Natija:


# # Foydalanuching ismini qabul qilib,
# #     unga salom beruvchi funksiya

def toliq_ism(ism, familya):
    """Foydalanuchi ism va familyasini jamlab chiqaruvchi   funksiya"""
    print(f"Foydalanuchi familyasi: {familya.title()}")
    print(f"Foydalaunchi ism:{ism.title()}")


toliq_ism('husanboy', 'boboxonov')  # Natija:


# # Foydalanuchi familyasi: Boboxonov
# # Foydalaunchi ism:Husanboy


def yosh_hisobla(ism, tugulgan_yil):
    """Foydalannuchining yoshini hisoblaydi dastru"""
    print(f'{ism.title()} {2025 - tugulgan_yil}-yoshda')


yosh_hisobla('husan', 2005)  # Natija:Husan 20-yoshda


# yosh_hisobla(ism='husan', tugulgan_yil=2005)  # Natija:Husan 20-yoshda


def yosh_hisob(tugilgan_yil, joriy_yil=2025):
    """Foydalanuvchi togilgan yildan uning yoshini hisoblaydi"""
    print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz")


yosh_hisob(2005)  # Natija:Siz 20 yoshdasiz

"""AMALIYOT"""


# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def tugulgan_yil_hisoblatdi(ism, yosh, jotiy_yil=2025):
    print(f"{ism.title()}  {jotiy_yil - yosh} - yilda tug'ilgan")


tugulgan_yil_hisoblatdi('husanboy', 20)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kvadirat_kub_hisoblaydi(son):
    print(f"{son} ning kvadirati {son ** 2} ga teng")
    print(f"{son} ning kubi {son ** 3} ga teng")


kvadirat_kub_hisoblaydi(4)


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_toq_topish(son):
    if son % 2 == 1:
        print(f"{son} toq son.")
    else:
        print(f"{son} juft son.")


juft_toq_topish(7)


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def katta_kichik_topish(son1, son2):
    if son1 > son2:
        print(f"{son1}, {son2} da katta.")
    elif son1 < son2:
        print(f"{son2},{son1}da katta. ")
    else:
        print("Sonlar teng")


katta_kichik_topish(7, 7)


# Foydalanuvchidan x va y sonlarini olib, x daraj(y)ni konsolga chiqaruvchi funksiya yozing.

def misol(x, y):
    print(x ** y)


misol(4, 2)


# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

def misol1(x, y=2):
    print(pow(x, y))


misol1(4)


# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
# qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
# Natijalarni konsolga chiqaring.

def bolinish_alomatlari(son):
    for i in range(1, 11):
        if son % i == 0:
            print(f"{son} {i} ga qoliqsiz bo'linadi.")


bolinish_alomatlari(70)
