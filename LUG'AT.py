"""14-dars:Lug'at.
Boboxonov Husanboy"""

car_0 = {'model': 'ferrari', 'rang': 'qizil'}
print(car_0['model'])#Natija:ferrari
print(car_0['rang'])#Natija:qizil

en_uz = {'apple': 'olma', 'apricot': "O'rik", 'banana': 'banan'}
print(en_uz['apple'])#Natija:olma

mevalar = {'olma': 10000, 'tarvuz': 8000, 'qovun': 10000}
print(f"Olmaning narxi :{mevalar['olma']} so'm")#Natija:Olmaning narxi :10000 so'm

talaba_0 = {'ism': 'boboxonov husanboy', 'yosh': 19, 't_yil': 2005}
print(f"{talaba_0['ism'].title()}, \
{talaba_0['t_yil']}-yil tug'ilgan,\
{talaba_0['yosh']}-yoshda")#Natija:Boboxonov Husanboy, 2005-yil tug'ilgan, 19-yoshda


#yangi kalit qo'shish
talaba_0['kurs'] = 2
talaba_0['fakulted'] = 'kamputer injenering'
talaba_0['ism'] = 'hasan'
print(talaba_0)#Natija:
# {'ism': 'hasan', 'yosh': 19, 't_yil': 2005, 'kurs': 2, 'fakulted': 'kamputer injenering'}

#Bosh lug'at
talaba_1 = {}
talaba_1['ism'] = 'husanboy'
talaba_1['yosh'] = 19
talaba_1['kurs'] = 2
print(talaba_1)#Natija:{'ism': 'husanboy', 'yosh': 19, 'kurs': 2}
print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']} - kurs ")#Natija:Talaba Husanboy, 2 - kurs

#qiymatni yangilash
talaba_1['kurs'] = 4
print(f"Talaba {talaba_1['ism'].title()}, {talaba_1['kurs']} - kurs ")#Natija:Talaba Husanboy, 4 - kurs

#o'chirish
del talaba_1['yosh']
print(talaba_1)#Natija:{'ism': 'husanboy', 'kurs': 4}

#LUG'ATNI QATORLARGA BO'LIB YOZISH
telefonlar = {
    'ali': 'iphone x',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310'
    }

# get() metodi
phone = telefonlar['ali']
print(f"Alining telfoni {phone}")#Natija:Alining telfoni iphone x


phone1 = telefonlar.get("hasan", "Bunday iasm mavjud emas")
print(phone1)#Natija:Bunday iasm mavjud emas

phone2 = telefonlar.get('hasan')
print(phone2)#Natija:None

"""AMALIYOT"""
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu
# inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin,
# 1954-yilda, Samarqand viloyatida tug'ilgan

ukam = {
    'ism': 'husan',
    'yoshi': 14,
    't_yil': 2007,
    'shahri': 'urganch',
}
print(f"Ukamning ismi {ukam['ism'].title()},tug'ilgan yil {ukam['t_yil']},shahar {ukam['shahri']}")#Natija:
# Ukamning ismi husan,tug'ilgan yil 2007,shahar urganch

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing.
# Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
taomlar = {
    'hasan': 'osh',
    'husan': 'manti',
    'kamron': 'baliq',
    'sulaymon': 'shorva',
    'ruxshona': 'log\'mon'
}
print(f"Hasannig taomi {taomlar['hasan']}")#Natija:Hasannig taomi osh

# Python izohli lu'gati tuzing:
# Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
lugat = {
    'integer': 'Buton son',
    'float': 'haqiqiy son',
    'string': 'matin',
    'if': 'shart',
    'else': 'agar'
 }

# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
matn = input('Biror soz kiriting>>')
tarjima = lugat.get(matn.lower(), 'Bunday soz yoq ')
print(tarjima)

# Yuqoridagi vazifani if-else yordamida qiling va
# natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

kalit = input("Kalit so'z kiriting:")
tarjima = lugat.get(kalit.lower())
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
