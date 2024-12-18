"""07-dars:LIST
Boboxonov Husanboy"""

mevalar = ['olam', 'anjir', ' shaftoli', "o'rik"]#mevalar ro'yxati(matin)
narhlar = [1200, 1800, 10900, 22000]#narhlar ro'yxati(sonlar)
sonlar = ['bir', 'ikki', 3, 4, 5]#sonlar va matin ro'yxati
ismlari = []#bo'sh ro'yxat

print(mevalar[-1])#konsilga:o'rik
print(mevalar[-2])#konsilga:shaftoli
print(mevalar[0].upper())#konsilga:OLAM
print(mevalar[0].title())#konsilga:Olam

#Element o'zgartirish

mevalar[0] = 'banan'
print(mevalar)#['banan', 'anjir', ' shaftoli', "o'rik"]
mevalar[-1] = 'anor'
print(mevalar)#['banan', 'anjir', ' shaftoli', 'anor']

#Qo'shish.append()

mevalar.append('tarvuz')
print(mevalar)#['banan', 'anjir', ' shaftoli', 'anor', 'tarvuz']

#.insert

mevalar.insert(0,'uzum')
print(mevalar)#['uzum', 'banan', 'anjir', ' shaftoli', 'anor', 'tarvuz']

mevalar.insert(3,'ananas')
print(mevalar)#['uzum', 'banan', 'anjir', 'ananas', ' shaftoli', 'anor', 'tarvuz']

cars = []
cars.append('Lacetti')
cars.append('Malibu')
cars.append('Tracker')
print(cars)#['Lacetti', 'Malibu', 'Tracker']

#O'chirish,del

del cars[0]
print(cars)#['Malibu', 'Tracker']

cars.insert(0,'Lacetti')
print(cars)#['Lacetti', 'uMalib', 'Tracker']

del cars[1]
print(cars)#['Lacetti', 'Tracker']

#remove()

cars.remove('Lacetti')
print(cars)#['Tracker']

#pop()

hayvonlar = ['it', 'mushuk', 'sigir', "qo'y", 'quyon', 'mushuk']
hayvonlar.remove('mushuk')
print(hayvonlar)#['it', 'sigir', "qo'y", 'quyon', 'mushuk']

bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(1)
# print(mahsulot)#un
# print(bozorlik)#["yog'", 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + "sotib oldim")
print("Olinmagan mahsulot:  ", bozorlik)

"""AMALIYOT"""

# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting

ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', "G'ani"]

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:

print("Salom " + ismlar[0] + " ishlaring yaxshimi?")
print(f"{ismlar[2]} va {ismlar[3]} egizaklar")
print(ismlar[-1] + " g'ildirakni g'izillatib g'ildratti")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).

sonlar1 = [-1, 24, 33, 8.3, -5]
print(sonlar1)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.

sonlar[0] = sonlar[0]+sonlar[-1]
sonlar[1] = -67.8
sonlar[4] = sonlar[4] + 37
del sonlar[5]
print(sonlar)

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

t_shaxslar = ['Amir Temur','Imom Buxoriy', 'Napoleon']
z_shaxslar = ['Bill Gates', 'Elon Musk', 'Doasnald Trump']

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:

print(f"\nMen tarixiy shaxslardan {t_shaxslar.pop(1)} bilan,\n\
zamonaviy shaxslardan esa {z_shaxslar.pop(0)} bilan\n\
suhbat qilishni istar edim\n")

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append('John')
friends.append('Alex')
friends.append('Danny')
friends.append('Sobirjon')
friends.append('Vanya')
print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang.

friends.remove('John')
friends.remove('Alex')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.

friends.append('Hasan')
friends.insert(0, 'Husan')
friends.insert(2, 'Ivan')
print(friends)


# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.

mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)