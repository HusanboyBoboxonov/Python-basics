"""12-dars:Xatolar bilan ishlash.
 Boboxonov Husanboy"""

#SyntaxError:
# print"Hello World!"
# print("Hello World"
# print("Assolom alaykum!")

#IndentationError:
# print("Hello World!")
#
# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)

#Run time Error

#TypeError:
son = input("Istalgan son kiriting: ")
print(f"{son} ing kvadirati {son**2}")

#NameError
# prit("Hello World")
mevalar = ['olma', 'uzum', 'nok', 'anor', 'anjir']
# for meva in mvalar:
#     print(meva)

#ValueError:
son = int(input('Istalgan son kiritng>>'))#float
if son >= 0:
    print("Musbat son")
else:
    print('Manfiy son')

#IndexError:
mevalar = ['olma', 'anor', 'uzum']
print(mevalar[3])

#ZeroDivisionError:
x, y = 50, 50
z = 250/(x-y)

#Mantiqiy xatolar
radius = 5
pi = 4.14
aylana_yuzi = pi*radius**2
print(aylana_yuzi)

son1 = float(input("Isatalgan son kiriting"))
ildiz = son1**1/2#9.0 ning ildizi 4.5ga teng
print(f"{son1} ning ildizi {ildiz}ga teng")

mevalar = ['olama', 'uzum', 'nok', 'anor', 'anjir']
for meva in mevalar:
    print(meva)
    print("Dastur tugandi")

"""AMALIYOT"""
"""Xatoni topish"""

# 1-misol
son = float(input("Juft son kiriting: "))
if son % 2 == 0:
    print("Bu son juft emas.")
else:
    print("Rahmat!")

# 2-misol
yosh = int((input("Yoshingiz nechida?")))

if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
    print(f"Chipta {narh} so'm")

# 3-misol
x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x}={y}")
elif x < y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")

# 4-misol
mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")

# 5-misol
mahsulotlar1 = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

savat1 = []
for n in range(5):
    savat.append(input(f'Savatga {n + 1}-mahsulotni qo\'shing: '))
    bor_mahsulotlar = []
    mavjud_emas = []
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            bor_mahsulotlar.append(mahsulot)
        else:
            mavjud_emas.append(mahsulot)
            if mavjud_emas:
                print("Do'konimizda quyidagi mahsulotlar yo'q:")
            for mahsulot2 in mavjud_emas:
                print(mahsulot2)
            else:
                print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# 6-misol
users = ['alisher1983', 'aziza', 'yasina' 'umar']
login = input("Yangi login tanlang:")
if login in users:
    print('Login band, yangi login tanalng!')
else:
    print("Xush kelibsiz!")