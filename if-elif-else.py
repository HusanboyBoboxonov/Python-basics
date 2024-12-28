"""11-dars:TARMOQLAR.
 Boboxonov Husanboy"""

yosh = int(input('Yoshingizni kiriting>>'))
if yosh <= 4:
    narh = 0#print("Sizga kirish bepul.")
elif yosh <= 12:
    narh = 5000#print('Sizga kirish 5000 ming so\'m.')
elif yosh <= 18:
    narh = 8000#print("Sizga kirish 8000 ming so\'m.")
else:
    narh = 10000#print("Sizga kirish 10000 ming so\'m.")
print(f"Sizga kirish {narh} so'm")#Natija:
#Yoshingizni kiriting>>19
# Sizga kirish 10000 so'm

#or amali
kun = input("Bugun qaysi kun?>>")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun damolish kuni.")
else:
    print("Bugun ish kuni.")#Natija:
# Bugun qaysi kun?>>shanba
# Bugun damolish kuni.

#and amali
kun0 = input("Bugun qaysi kun?>>")
harorat = float(input("Havo harorati qanday?>>"))
if kun0.lower() == "yakshanba" and harorat >= 30:
    print("Chomilishga ketdik!")
elif kun0.lower() == "yakshanba" and harorat < 30:
    print("Uyda dam olamiz!")#Natija:
# Bugun qaysi kun?>>yakshanba
# Havo harorati qanday?>> 29
# Uyda dam olamiz!

#or and amalari
kun1 = input("Bugun qaysi kun?>>")
kun1 = kun1.lower()
harorat1 = float(input("Havo harorati qanday?>>"))
if (kun1 == 'shanba' or kun1 == 'yakshanba') and harorat1 >= 30:
    print("Chomilishga ketdik!")
elif (kun1 == 'shanba' or kun1 == 'yakshanba') and harorat1 < 30:
    print("Uyda dam olamiz!")
else:
    print("Bugun ish kuni!")#Natija:
# Bugun qaysi kun?>>dushanba
# Havo harorati qanday?>>21
# Bugun ish kuni!

#BOOLEAN ma'lumotlar turi
narh = 15000
salat = False
choy = True
if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000
print(f"Jami {narh} so'm")#Jami 20000 so'm

narh0 = 15000
choy0 = True
salat0 = False
non = True
kompot = True
assortiy = False

if choy0:
    print("Mijoz choy sotib oldi.")
    narh0 = narh0 + 3000
if salat0:
    print("Mijoz salat  sotib oldi.")
    narh0 = narh0 + 5000
if non:
    print("Mijoz non sotib oldi.")
    narh0 = narh0 + 2000
if kompot:
    print("Mijoz kompot sotib oldi.")
    narh0 = narh0 + 5000
if assortiy:
    print("Mijoz assortiy sotib oldi.")
    narh0 = narh0 + 15000
print(f"Jami {narh0} so'm")#Natija:
# Mijoz choy sotib oldi.
# Mijoz non sotib oldi.
# Mijoz kompot sotib oldi.
# Jami 25000 so'm

#in operator
menu1 = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>')
if ovqat.lower() in menu1:
    print("Buyurtma qabul qilindi.")
else:
    print("Afsus bunday ovqat yo'q bizda.")#Natija:
# Nima ovqat yeysiz?>>manti
# Afsus bunday ovqat yo'q bizda.

#not in operator
menu0 = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
ovqat = input('Nima ovqat yeysiz?>>')
if ovqat.lower() not in menu0:
    print("Afsus bunday ovqat yo'q bizda.")
else:
    print("Buyurtma qabul qilindi.")#Natija:
# Nima ovqat yeysiz?>>manti
# Afsus bunday ovqat yo'q bizda.

menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
buyurtmalar = ['osh', 'somsa', 'manti', 'shahslik']
for taom in buyurtmalar:
    if taom in menu:
        print(f"Menda {taom} bor.")
    else:
        print(f"Kechirasiz bu {taom} yo'q.")#Natija:
# Menda osh bor.
# Kechirasiz bu qazonkabob yo'q.
# Kechirasiz bu shashlik yo'q.
# Kechirasiz bu norin yo'q.
# Menda somsa bor.

"""AMALIYOT"""

# Foydalanuvchidan juft son kiritishni so('rang. Agar foydalanuvchi '
# 'juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.)
jutf_son = int(input("Juft son kiriting:"))
print("Rahmat!") if jutf_son % 2 == 0 else print("Bu son juft emas.")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
yosh = int(input("Yoshingiz nechida?"))
if yosh <= 4 or yosh >= 60:
    narh = 0
elif yosh < 18:
    narh = 10000
else:
    narh = 20000
print(f"Chipta {narh} so'm")

# Foydalanuvchidan ikita son kiritishni so('rang'
# ''sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring)
son1 = float(input("Birinchi soni kiriting>>"))
son2 = float(input("Ikkinchi soni kiriting>>"))
if son2 > son1:
    print(f"{son2} > {son1}")
elif son2 < son1:
    print(f"{son2} < {son1}")
else:
    print(f"{son2} = {son1}")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
# Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta
# mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring
# va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda,
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
mahsulotlar = ['uzum', 'olma', 'anor', 'baliq', 'non', 'tuxum', 'yog', 'tort', 'shakr', 'guruch']
savat = []
for n in range(5):
    savat.append(input(f"{n+1} - mahsulotni kiriting>>"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f"Bu {mahsulot} mahsulot do'konimizda bor")
    else:
        print(f"Bu {mahsulot} mahsulot do'konimizda yo'q")

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang.
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga,
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
# Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan
# xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
mahsulotlar = ['uzum', 'olma', 'anor', 'baliq', 'non', 'tuxum', 'yog', 'tort', 'shakr', 'guruch']
savat = []
mavjud_emas = []
bor_mahsulotlar = []
for n in range(5):
    savat.append(input(f"{n+1} - mahsulotni kiriting>>"))
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
if not mavjud_emas:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print(f"Do'konda quyidagi mahsulotlar do'konimizda yo'q:")
    for x in mavjud_emas:
        print(x)

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing.
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni
# foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday
# login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz,
# foydalanuvchi!" xabarini chiqaring.
foydalanuchi = ['hasan', 'abror', 'jamshid', 'sulaymon', 'aziz']
shaxs = input('Yangi login tanlang:')
if shaxs in foydalanuchi:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz,{shaxs.title()}")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha
# bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.
son7 = int(input("Butun son kiriting?>>"))
for n in range(2, 11):
    if son7 % n == 0:
        # if not (son7%n):
        print(f"{son7} soni {n} ga qoldiqsiz bo'linadi.")
