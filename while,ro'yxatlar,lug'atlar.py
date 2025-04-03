"""18-dars:WHILE VA RO'YXATLAR.
Boboxonov Husanboy"""

#  Whlie va Ro'yxat
print("Yaqin do'stlar ro'yxatini tuzmiz")
ismlar = []
n = 1
while True:
    savol = f"{n}-do'stingizni kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    n += 1
    takrorlash = input("Yana ism qo'shasizmi.(ha/yo'q)")
    if takrorlash != 'ha':
        break

print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())  # Natija:
#    Yaqin do'stlar ro'yxatini tuzmiz
# 1-do'stingizni kiriting:Inomjan
# Yana ism qo'shasizmi.(ha/yo'q)ha
# 2-do'stingizni kiriting:Shaxliyor
# Yana ism qo'shasizmi.(ha/yo'q)yo'q
# Do'stlaringiz ro'yxati:
# Inomjan

#  Whlie va Lug'at
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stimgiz ismni kiriting:")
    yosh = input(f"{ism.title()}ning yoshini kiriting:")
    dostlar[ism] = int(yosh)
    javob = input("Yana ma'lumot qo'shasizmi.(ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")  # Natija:
# Do'stlaringiz yoshini saqlaymiz.
# Do'stimgiz ismni kiriting:Inomjan
# Inomjanning yoshini kiriting:20
# Yana ma'lumot qo'shasizmi.(ha/yo'q)ha
# Do'stimgiz ismni kiriting:Shaxliyor
# Shaxliyorning yoshini kiriting:19
# Yana ma'lumot qo'shasizmi.(ha/yo'q)yo'q
# Inomjan 20 yoshda
# Shaxliyor 19 yoshda

# O'chirish
cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
car = 'nexia'
while car in cars:
    cars.remove(car)

print(cars)  # Natija:['lacetti', 'toyota', 'audi', 'malibu']

#  Whlie , Ro'yxat va  Lug'at
talabalar = ['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting:")
    print(f"{talaba.title()} baholandi.")
    baholangan_talabalar[talaba] = int(baho)

for talaba, baho in baholangan_talabalar.items():
    print(f"{talaba.title()}ning bahosi {baho}")  # Natija:
# Botirning bahosini kiriting:4
# Botir baholandi.
# Olimning bahosini kiriting:5
# Olim baholandi.
# Husanning bahosini kiriting:2
# Husan baholandi.
# Hasanning bahosini kiriting:3
# Hasan baholandi.
# Botirning bahosi 4
# Olimning bahosi 5
# Husanning bahosi 2
# Hasanning bahosi 3

"""AMALIYOT"""

# foydadan buyurtma qabul qilish dastur yozing.
# Ular nomini birma-bir qabul qilib, yangi ro' mahsulotlar joylang

# print("Buyumlarni saqlavchi dastur:")
# buyumlar = []
# n = 1
# while True:
#     buyum = input(f"{n}-buyumni kiriting:")
#     buyumlar.append(buyum)
#     n += 1
#     takror = input("Ya'na buyum kirigizasizmi.(ha/yo'q)")
#     if takror == "yo'q":
#         break
#
# print("Mana sizning buyumlaringiz:")
# for buyum in buyumlar:
#     print(buyum, end=' ')

# e-bozor uchun mahsulotlar va hujjat narhlari lug'atini shakllantiruvchi dastur yozing.
# samaralidan lug'atga bir nechta mahsulot (mahsulot va uning narhi) tizimini so'rang.

print("e-bozor uchun mahsulotlar va hujjat narhlari dasturi:")
mahsulotlar = {}
ishora = True
n = 1
while ishora:
    mahsulot = input(f"{n}-mahsulotni nomini kiriting: ")
    narxi = input(f"{mahsulot}ning narxini kiriting:")
    mahsulotlar[mahsulot] = float(narxi)
    takror = input("Ya'na buyum kirigizasizmi.(ha/yo'q)")
    n += 1
    if takror != "ha":
        break

print("Mana siz kiritgan masulotlar va narxlar bilan:")
for mahsulot, narxi in mahsulotlar.items():
    print(f"{mahsulot}ning narxi {narxi}")

# Yuqoridagi ikki dasturni jamlaymiz. samarali buyurtmasi ro'yxatidagi
# har qanday e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxatini olishingiz mumkin).
# Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring,
# aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

buyurtmalar = ['olma', 'anjir', 'uzum', 'qovun']
mahsulotlar = {'olma': 20000,
               'shaftoli': 25000,
               'tarvuz': 18000,
               'uzum': 22000}
n += 1
while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narxi = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()}-{narxi} so'm")
    else:
        print("Bizda bu mahsulot yo'q")

