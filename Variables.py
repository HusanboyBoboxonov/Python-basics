"""04-dars: O'zgaruvchilar.
Boboxonov Husanboy"""

ism = "Husanboy"
yosh = 19

print(ism)
print(yosh)


ism1 = "Husanboy"
print(ism1)
ism1 = "Hasanboy"#Bu yerda o'zgaruchiga ya'nigi matin joylandi.
print(ism1)

#O'zgarivchilar turi ikki xil bo'ladi:
#str,int,float qisqacha

a = 6
b = 7
c = (a+b)**2
print(c)#c=169

ism0 = "Husanboy"
print(ism0)
ism0 = "Hasanboy"
print(ism0)

ism_sharif = "Husanboy Boboxonov"
# print(Ism0)#NameError: name 'Ism0' is not defined. Did you mean: 'ism0'?
print(ism0)

yosh = 19
y = 19

#help() keyin keywords quydagi so'zlar o'zgaruvchi sifatida foydalanmaslik kerak.

"""Amalyiot"""
# Quyidagi mashqlarni bajaring:

# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring

matn = "Hello World"
print(matn) #Natija:Hello World


# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.

xabar = "Husan 19-yoshda"
print(xabar)#Natija:Husan 19-yoshda
xabar = "Hasan 19-yoshda"
print(xabar)#Natija:Hasan 19-yoshda

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)

# class = "I am a programmer"
# print(class)#SyntaxError: invalid syntax

# Quyidagi kodni bajaring:

# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)#Natija:Radiusi 5 ga teng aylananing yuzi= 78.53975
