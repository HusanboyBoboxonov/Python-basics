"""09-dars:FOR LOOP.
 Boboxonov Husanboy"""

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
print('Salom ', mehmonlar[0])#Natija:Salom  Ali
print('Salom ', mehmonlar[1])#Natija:Salom  Vali
print('Salom ', mehmonlar[2])#Natija:Salom  Hasan
print('Salom ', mehmonlar[3])#Natija:Salom  Husan
print('Salom ', mehmonlar[4])#Natija:Salom  Olim

for mehmon in mehmonlar:
    print('Salom ', mehmon)


"""MISOL"""

#1-misol

mehmonlar1 = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon1 in mehmonlar1:
    print(f"Hurmatli {mehmon1},sizni 20-dekanr kuni naxorgi oshga taklif qilamiz ")
print(f"Hurmat bilan, Husanovlar oilasi\n")

#2-misol

sonlar = list(range(1, 11))
for son in sonlar:
    print(f"{son} ning kvadirti {son**2} ga teng")

#3-misol

sonlar1 = list(range(11))
kvadirati = []
for son1 in sonlar1:
    kvadirati.append(son1**2)

print(sonlar1)
print(kvadirati)

#4-misol

dostlar = []
print("5 ta dostingizni kiriting")
for n in range(5):
    dostlar.append(input(f"{n+1}-dostingizni kiriting>>"))
print(dostlar)

"""AMALIYOT"""

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

ismlar = ['Husan', 'Olim', 'Vali', 'Jamshit', 'Jasur']
n = 0
for ism in ismlar:
    n += 1
    print(f"{ism} ertaga bazimga kel.")
print(f"{n}ta odamga aytingiz")


# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

toq_sonlar = list(range(11, 101, 2))
for son in toq_sonlar:
    print(f"{son} ning kubi {son**3} ga teng")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.

kinolar = []
print("5ta sevimli kinoni kiriting")
for n in range(5):
    kinolar.append(input(f"{n+1}-kinoni kiriting "))
print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.

shaxs_son = int(input("Bugun necha kishi bilan shubatlashdingiz>>"))
shaxs = []
for n in range(shaxs_son):
    shaxs.append(input(f"{n+1}-suxbatdoshni kiriting>>"))
print(shaxs)