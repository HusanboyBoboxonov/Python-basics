"""05-dars:STRING(MATIN).
Boboxonov Husanboy"""

ism = "Husanboy"

shahar = "Urganch"
viloyat = "Xorazim"

matn = "Men yangi 📱 oldim"
print(matn)

#STRING USTUDA AMALLAR
ism0 = "Husanboy"
print("Mening ismim " + ism0)#matinlarni qo'shish

ism1 = "Husanoy"
familya1 = "Boboxonov"
print(ism1 + " " + familya1)

#f-string

ism2 = "Husanboy"
familya2 = "Boboxonov"
ism_sharf = f"{ism2} {familya2}"
print(ism_sharf)

ism3 = "James"
familya3 = "Bond"
print(f"Salom,mening ismim {familya3}, {ism3} {familya3}")

#MAHSUS BELGILAR

print("Hello World")
print("Hello \t World")#Boshliq ochadi
print("Hello \n World")#Qator tashlaydi

#STRING METODLAR

ism4 = "jemes"
familya4 = "bond"
ism_sharf0 = f"{ism4} {familya4}"
print(ism_sharf0)
print(ism_sharf0.upper())#Hamma harf katta
print(ism_sharf0.lower())#Hamma harf kichik
print(ism_sharf0.title())#Birinchi harf  hammasi katta
print(ism_sharf0.capitalize())#Birinchi harf faqat katta


meva = "   olma   "
print(meva)
print("Men " + meva.lstrip() + " yaxshi ko'raman")#chap tomandagi boshliqni oladi
print("Men " + meva.rstrip() + " yaxshi ko'raman")#o'ng tomondagi boshliqni oladi
print("Men " + meva.strip() + " yaxshi ko'raman")#ikki tomondagi boshliqni oladi
print("Men " + meva + " yaxshi ko'raman")

#INPUT

# ism5 = input("Isminigizni kiriting>>")
# print("Assalom alekum " + ism5)
#
# ism6 = input("Isminigizni kiriting?\n>>")
# print("Assalom alekum," + ism6.title())

#AMALYIOT

# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
    # Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati

kocha = " Bog'bon "
mahalla = " Sog'bon "
tuman = " Bodomzor "
viloyat0 = " Samarqand "
print(kocha + "kocha ," + mahalla + "mahalla," + tuman + "tumani," + viloyat0 + "viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

kocha1 = str(input("kochani koriting>>"))
mahalla1 = str(input("mahallani kiriting>>"))
tuman1 = str(input("tumani kiriting>>"))
viloyat1 = str(input("viloyatni kiriting"))
print(kocha1 + "kocha ,\n" + mahalla1 + "mahalla,\n" + tuman1 + "tumani,\n" + viloyat1 + "viloyati\n")
manzil = f"{kocha1} ko'chasi, {mahalla1} mahallasi, {tuman1} tumani, {viloyat1} viloyati"
print(manzil)

# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
# Quyidagi o'zgaruvchilarni yarating:
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"

print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())


