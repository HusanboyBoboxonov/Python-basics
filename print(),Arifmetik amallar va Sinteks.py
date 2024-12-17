"""03-dars PRINT() funksiyasi.
  Boboxonov Husanboy"""

# Quydagi kod Hello World gapni konsilga chiqaradi
print("Hello World") #izox

print("Assalom aleykum")
print("Hello World")

# Quydagi kod xato:SyntaxError
# print(Hayirli tong!)

# Matini konsilga chiqarish uchun qo'sh tirnoq " " yoki bir tirnoq ' ' ishlatiladi
print("Hayirli tong!")
print('Hayirli tong!')

print("Men \"DEL\" markasidan kanouter sotib oldim")

print("""Odamni ersaning,demagil odami,
Oniki,yo'q xalq g'amidin g'ami """)#Qatorni ajiratishda :

print("Odamni ersaning,demagil odami,\nOniki,yo'q xalq g'amidin g'ami ")#Qatorni ajiratishda back slash ishlatilaadi"\n" :

print('Odamni ersaning,demagil odami,\nOniki,yo\'q xalq g\'amidin g\'ami ')#"\'"  enilis tilda "o'" yo'q sababli ishlatiladi , uni belgi sifatida olib ketadi

print("Odamni ersaning,demagil odami,Oniki,yo'q xalq g'amidin g'ami ")#"\'" siz yoziladigan variyat

 # PRINT() funksiyasi orqali arifmetik amallarni komsilga chiqarish mumkin

print(2+4*2)
print(19/5)
print(16//4)#Natijani konsilga butunson korinishda chiqaradi.
print(15//4)#Bunda natija 3 chiqadi,ya'ni butun qisim chiqadi konsilga.
print(2**4)#Kvadirat 2ni 4chisi bo'ladi 16.
print("To'qqiznig kvadirati", 9**2, "ga teng")
print("3*3=", 3*3)

"""Amaliyot"""

#"Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
# "Nexia", "Tico", 'Damas' ko'rganlar qilar havas"

print("'Nexi', 'Tico', 'Damas' ko'rganlar qilar havas")

#Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
# 5 ning 4-darajasini toping
# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
# Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
# Diametri 12 ga teng bo'lgan doiraning yuzini toping  (π=3.14 π=3.14 deb oling)
# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)

print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

#1 5 ning 4-darajasi
print('5 ning 4-darajasi', 5**4)

#2 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print("22 ni 4 ga bo'lganda qancha qoldiq", 22%4)

#3 Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
print("Tomonlari 125 ga teng kvadratning yuzi", 125*125, "ga, perimetri", 4*125, "teng")

#4 Diametri 12 ga teng bo'lgan doiraning yuzini toping
print('Diametri 12 ga teng bo\'lgan doiraning yuzi', 3.14*(12/2)**2, 'ga teng')

#5 Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping
print("Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasi", (6**2+7**2)**(1/2))