"""06-dars:Sonlar.
Boboxonov Husanboy"""

a = 20 #int
b = 5.5 #float
temp = 36.6

#TYPE()

print(type(temp)) #konsilga:<class 'float'>
print(type(a))#konsilga:<class 'int'>

aholi_soni = 7_594_376_567
print("Aholi soni : ", aholi_soni)#Aholi soni :  7594376567

x, y, z = 10, 5.5, -43

c = a*b
print(c)#110.0 float* int = float
print(type(c))#<class 'float'>

d = 100/2
print(type(d))#<class 'float'>
d = 100//2
print(type(d))#<class 'int'>

#O'zgarmas qiymat

radius = 20
PI = 3.14159
diametr = 2 * radius
print("Aylana uzunligi= ", PI*diametr)

# misol
# ism = "Husanboy"
# yosh = 19
# xabar = ism + " " + yosh + "yoshda"
# print(xabar)#TypeError: tipda xatolik bor

ism1 = "Husanboy"
yosh1 = 19
yosh1 = str(yosh1)
xabar1 = ism1 + " " + yosh1 + " yoshda"
print(xabar1)#Husanboy 19 yoshda

# t_yil3 = input("Tug'ilgan yilni yozing")
# yosh3 = 2024 - t_yil3
# print("Siz ", yosh3, " yoshdasiz")#TypeError:tipda xatolik bor


t_yil = int(input("Tug'ilgan yilni yozing"))
yosh2 = 2024 - t_yil
print("Siz ", yosh2, " yoshdasiz")#Siz  19  yoshdasiz

d = int("10")
f = float("5.5")
temp = str(36.6)

"""AMALIYOT"""

# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur

son1 = float(input("Biror bir son kiriting>>"))
print(f"{son1} ning kvadirati {son1**2} ga teng")
print(f"{son1} ning kub {son1**3}ga teng")

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
yosh3 = int(input("Yoshingizni kiriting>>"))
t_yil3 = 2024 - yosh3
print(f"Siznig tug'ilgan yil {t_yil3}")

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
print(f"{a}+{b}=", a+b)
print(f"{a}-{b}=", a-b)
print(f"{a}x{b}=", a*b)
print(f"{a}/{b}=", a/b)