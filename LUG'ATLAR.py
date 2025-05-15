talaba_0 = {
    'ism': 'husanboy',
    'familyasi': 'boboxonov',
    'yosh': 19,
    'fakulted': 'kamputerinjenering',
    'kurs': 2
}
print(talaba_0.items())  # Natija:
# dict_items([('ism', 'husanboy'), ('familyasi', 'boboxonov'), ('yosh', 19), ('fakulted', 'kamputerinjenering'),
# ('kurs', 2)])

for kalit, qiymat in talaba_0.items():
    print(f"Kalit : {kalit} ")
    print(f"Qiymat: {qiymat}\n")  # Natija:
# Kalit : ism
# Qiymat: husanboy

telfonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokiya 3310'
}
for k, q in telfonlar.items():
    print(f"{k.title()}ning telfoni {q}")  # Natija:
    # Alining telfoni iphone x
    # Valining telfoni galaxy s9
    # Olimning telfoni mi 10 pro
    # Orifning telfoni nokiya 3310

# keys
mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}

print(mahsulotlar.keys())  # Natija:
# dict_keys(['olma', 'anor', 'uzum', 'anjir', 'shaftoli'])

print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())  # Natija
# Do'kondagi mahsulotlar:
# Olma
# Anor
# Uzum
# Anjir
# Shaftoli

print("Do'kondagi mahsulotlar:")
for mahsulot in mahsulotlar:
    print(mahsulot.title())  # Natija
# Do'kondagi mahsulotlar:
# Olma
# Anor
# Uzum
# Anjir
# Shaftoli

bozorlik = ['anor', 'uzum', 'non', 'baliq']
for mahsulo in mahsulotlar:
    if mahsulo in bozorlik:
        print(f"{mahsulo.title()} {mahsulotlar[mahsulo]} so'm")  # Natija:
# Anor 20000 so'm
# Uzum 40000 so'm

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos,dokonigizga {buyum}  mahsulotlarni ham olib keling")  # Natija:
# Iltimos,dokonigizga non  mahsulotlarni ham olib keling
# Iltimos,dokonigizga baliq  mahsulotlarni ham olib keling

# sorted()
print("Do'kondagi mahsulorlar:")
for mahsulot1 in sorted(mahsulotlar):
    print(mahsulot1.title())  # Natija:
# Do'kondagi mahsulorlar:
# Anjir
# Anor
# Olma
# Shaftoli
# Uzum

# values
print(telfonlar.values())  # Natija:
# dict_values(['iphone x', 'galaxy s9', 'mi 10 pro', 'nokiya 3310'])

print("Foydalanuchilar quydagi telfonlarni ishlatadi:")
for telfon in telfonlar.values():
    print(telfon)  # Natija:
# Foydalanuchilar quydagi telfonlarni ishlatadi:
# iphone x
# galaxy s9
# mi 10 pro
# nokiya 3310


telfonlar1 = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokiya 3310',
    'hamida': 'galaxy s9',
    'maryam': 'huawei p30',
    'tohir': 'iphone x',
    'umar': 'iphone x'
}
print("Foydalanuchilar quydagi telfonlarni ishlatadi:")
for telfon in telfonlar1.values():
    print(telfon)  # Natija:
# Foydalanuchilar quydagi telfonlarni ishlatadi:
# iphone x
# galaxy s9
# mi 10 pro
# nokiya 3310
# galaxy s9
# huawei p30
# iphone x
# iphone x

# set()
print("Foydalanuchilar quydagi telfonlarni ishlatadi:")
for telfon in set(telfonlar1.values()):
    print(telfon)  # Natija:
# Foydalanuchilar quydagi telfonlarni ishlatadi:
# galaxy s9
# iphone x
# mi 10 pro
# nokiya 3310
# huawei p30

toys = {'ball', 'car', 'lamp', 'ball'}
print(type(toys))  # Natija:<class 'set'>
print(toys)  # Natija:{'ball', 'lamp', 'car'}

"""AMALIYOT"""

# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli
# qilib konsolga chiqaring.
izohlar = {
    'for': 'tsikl',
    'if': 'shart',
    'else': 'agar',
    'tuple': 'o\'zgarmas',
    'list': 'royxat',
    'boolean': 'mantiqiy qiymat',
    'float': 'haqiqiy sonlar',
    'int': 'butun sonlar',
}
for k, q in sorted(izohlar.items()):
    print(f"{k.title()}-{q.title()}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing.
# Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.
davlat_putaxtlar = {
    'uzbekiston': 'toshkent',
    'russiya': 'maskava',
    'angilya': 'london',
    'AQSH': 'Washington',
    'xitoy': 'pekin',
    'eron': 'tehron',
    'turkiya': 'anqara',
    'fransiya': 'parij',
    'hindiston': 'dehli'
}
print("Dunyo davlatlar:")
for davlat in davlat_putaxtlar.keys():
    print(davlat.title())

print('Davlatlar poytaxtlari:')
for poytaxt in davlat_putaxtlar.values():
    print(poytaxt.title())

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
davlat_kir = input("Istalga davlatni kikriting:")
if davlat_kir in davlat_putaxtlar.keys():
    print(f"{davlat_kir.title()}ning poytaxti: {davlat_putaxtlar[davlat_kir]}")
else:
    print("Bizda bunday ma'lumot yo'q.")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang.
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating,
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
menu = {
        'osh': 20000,
        "lag'mon": 22000,
        'non': 4000,
        'choy': 5000,
        'shashlik': 12000,
        'somsa': 6000,
        'tabaka': 15000
        }
print('3 ta taom buyurtma bering.')
buyurtmalar  = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")