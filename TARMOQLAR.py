"""10-dars:TARMOQLAR.
 Boboxonov Husanboy"""

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

#Tengmi sharti

ism = 'Husan'
print(ism.lower() == 'husan')#Natija:True

#Tengemas sharti

# ism = input('Ismingizni kiriting>>')
if ism.lower() != 'husan':
    print(ism.title(), ', uzur biz husani kutyapmiz.')
else:
    print('Salom Husan ')#Natija:
#Ismingizni kiriting>>husan
#Salom Husan

javob = float(input('12x6 nechaga teng?>>'))
if javob != 72:
    print('Javob xato')#Natija:
#12x6 nechaga teng?>>32
#Javob xato

yosh = int(input('Yoshingizni kiriting>>'))
if yosh >= 18:
    print('Xush kelibsiz')
else:
    print('Kirish mumkin emas')#Natija:
# Yoshingizni kiriting>>19
# Xush kelibsiz

login = input('logini kiriting')
if len(login) <= 5:
    print('login 5ta harif dan kop bo\'lishi kerkak')#Natija:
# logini kiritingsdfs
# login 5ta harif dan kop bo'lishi kerkak

yil = int(input('Tug\'lganyilni kiriting>>'))
if 2024 - yil < 18:
    print(f'Sizning yoshingiz {2024 - yil} da ekan')
    print('Sizga kirish mumkinmas!')
else:
    print('Xush kelibsiz')#Natija:
# # Tug'lganyilni kiriting>>2005
# Xush kelibsiz

#Kodingiz qisaqa bolsa shunday yozishingiz mumukin

yosh = int(input('Yoshingiz nechada?>>'))
if yosh > 65: print('Siz COVID-19 risk guruhida ekansiz')

x, y = 25, 50
print('x>y') if x > y else print("x<y")#Natija:x<y

"""AMALIYOT"""

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing,
# ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring.
# GM uchun ikkala harfni katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car.lower() == 'gm':
        print(car.upper())
    else:
        print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.

for car in cars:
    if car.lower() != 'gm':
        print(car.title())
    else:
        print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin.
# Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!
# "  matnini konsolga chiqaring.
login = input('Logini kiriting>>')
if login.title() == 'Admin':
    print("Xush kelibsiz, Admin. ")
else:
    print(f"Xush kelibsiz, {login}!")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa,
# "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
son1 = float(input('Birinchi soni kiriting>>'))
son2 = float(input('Ikkinchi soni kiriting>>'))
if son2 == son1:
    print("Sonlar teng")


# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga
# "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
son0 = float(input('Istalgan son kiriting>>'))
print("Musbat son") if son0 > 0 else print("Manfiy son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring.
# Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
sonn = float(input('Istalgan son kiriting>>'))
print(f"{sonn**1/2}") if sonn > 0 else print("Musbat son kiriting")