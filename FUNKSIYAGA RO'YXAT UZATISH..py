"""21-dars:FUNKSIYAGA RO'YXAT UZATISH.
Boboxonov Husanboy"""


def bahola(ismlar):
    baholar = {}
    while ismlar:
        ism = ismlar.pop()
        baho = input(f" Talaba {ism.title()} ni baholang:")
        baholar[ism] = int(baho)
    return baholar


talabalar = ['inomjon', 'hasanboy', 'husanboy', 'shaxliyor']
baholangan = bahola(talabalar[:])  # [:] nusha olyapdi
print(baholangan)  # Natija:

# Talaba Shaxliyor ni baholang:5
#  Talaba Husanboy ni baholang:4
#  Talaba Hasanboy ni baholang:4
#  Talaba Inomjon ni baholang:5
# {'shaxliyor': 5, 'husanboy': 4, 'hasanboy': 4, 'inomjon': 5}

print(talabalar)  # Natija: []
# ['inomjon', 'hasanboy', 'husanboy', 'shaxliyor']

"""AMALIYOT"""


# Matnlardan iborat ro'yxat qabul qilib,
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
    for matn in matnlar:
        matnlar[matn] = matnlar[matn].title()
    return matnlar


ismlar = ['ali', 'vali', 'hasan', 'husan']
katta_harf(ismlar)
print(ismlar)


# Yuoqirdagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat qaytaradigan qilib o'zgartiring

def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar


ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

# Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va
# asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

talabalar = ['ali', 'vali', 'hasan', 'husan']


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar


baholar = bahola(talabalar)
print(baholar)
print(talabalar)
