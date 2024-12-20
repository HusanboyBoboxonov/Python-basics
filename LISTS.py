"""08-dars:LISTS
Boboxonov Husanboy"""

#Tartiblash.sort()
cars = ['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']
cars.sort()
print(cars)#['bmw', 'general motoros', 'mercesec benz', 'tesla', 'volvo']

#teskari tartibda
cars1 = ['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']
cars1.sort(reverse=True)
print(cars1)#['volvo', 'tesla', 'mercesec benz', 'general motoros', 'bmw']

#sorted()
cars2 = ['bmw', 'mercesec benz', 'volvo', ' general motoros', 'tesla']
print(sorted(cars2))#['bmw', 'general motoros', 'mercesec benz', 'tesla', 'volvo']

#teskari tartibda
cars3 = ['bmw', 'mercesec benz','volvo','general motoros', 'tesla']
print(sorted(cars3, reverse=True))#['volvo', 'tesla', 'mercesec benz', 'general motoros', 'bmw']

sonlar =[-1, 32, 43, 2, -5]
print(sorted(sonlar))#[-5, -1, 2, 32, 43]
print(sorted(sonlar, reverse=True))#[43, 32, 2, -1, -5]

#LEN
print(len(cars3))#Natija:5
print(len(sonlar))#Natija:6

#range()
sonlar0 = list(range(0, 10))
print(sonlar0)#Natija:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

toq_sonlar = list(range(1, 20, 2))#Qadam soni:2
print(toq_sonlar)#Natija:[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

sanash = list(range(0, 101, 10))#Qadam soni:10
print(sanash)#Natija:[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#MAX(), MIN(), SUM() funksiyalari

toq_sonlar1 = list(range(1, 20, 2))
print(toq_sonlar1)#Natija:[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

max_qiymat = max(toq_sonlar1)
print(max_qiymat)#Natija:19

min_qiymat = min(toq_sonlar1)
print(min_qiymat)#Natija:1

sum_qiymat = sum(toq_sonlar1)
print(sum_qiymat)#Natija:100

"""MISOL"""

narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh: ", arzon, "Eng qimat narh: ", qimat, "Jami narh: ", jami)

#LISTNI KESISH

cars1 = ['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']
print(cars1[0:3])#Natija:['bmw', 'mercesec benz', 'volvo']
print(cars1[2:4])#Natija:['volvo', 'general motoros']
print(cars1[:3])#Natija:['bmw', 'mercesec benz', 'volvo']
print(cars1[0:])#Natija:['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']

#LISTDAN nusxa olish

cars2 = ['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']
my_cars = cars2[:]#Kesish usuli
my_cars.append('bmw')
print(my_cars)#Natija:['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla', 'bmw']
print(cars2)#Natija:['bmw', 'mercesec benz', 'volvo', 'general motoros', 'tesla']

#TUPLE

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])#Natija:bus
print(toys[-1])#Natija:lizard
print(toys[2:5])#Natija:('bear', 'dino', 'snake')
# toys[0] = 'teddy'#TypeError: 'tuple' object does not support item assignment
# print(toys[0])
toys = list(toys)
toys.append('teddiy')
print(toys)#Natija:['bus', 'car', 'bear', 'dino', 'snake', 'lizard', 'teddiy']

"""AMALIYOT"""

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring

davlatlar = ['Qozog\'iston', 'Turkmaniston', 'Rassiya', 'O\'zbekiston']
print(davlatlar)#Natija:[ "Qozog'iston", 'Turkmaniston', 'Rassiya', "O'zbekiston"]

# Ro'yxatning uzunligini konsolga chiqaring

print(len(davlatlar))#Natija:4

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring

print(sorted(davlatlar))#Natija:["O'zbekiston", "Qozog'iston", 'Rassiya', 'Turkmaniston']

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

print(sorted(davlatlar,reverse=True))#Natija:['Turkmaniston', 'Rassiya', "Qozog'iston", "O'zbekiston"]


# Asl ro'yxatni qaytadan konsolga chiqaring

davlatlar = ['Qozog\'iston', 'Turkmaniston', 'Rassiya', 'O\'zbekiston']
print(davlatlar)#Natija:[ "Qozog'iston", 'Turkmaniston', 'Rassiya', "O'zbekiston"]

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.

davlatlar.sort()
print(davlatlar)#Natija:["O'zbekiston", "Qozog'iston", 'Rassiya', 'Turkmaniston']
davlatlar.sort(reverse=True)
print(davlatlar)#Natija:['Turkmaniston', 'Rassiya', "Qozog'iston", "O'zbekiston"]

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120, 1201, 2))
print(juft_sonlar)

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring

sum1 = sum(juft_sonlar)
print(sum1)#Natija:357060

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring

max_qiymat1 = max(juft_sonlar)
min_qiymat1 = min(juft_sonlar)
print(max_qiymat1 - min_qiymat1)#Natija:1080

# Ro'yxatdagi elementlar sonini hisoblang

print(len(juft_sonlar))#Natija:541

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

print(juft_sonlar[:21])
print(juft_sonlar[-20:])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# nonushta degan yangi ro'yxatga taomlardan nusxa oling

taomlar = ['manti', 'somsa', "baliq", "sho'rva", 'palov']
nonushta = taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing

taomlar.append('shashlik')
taomlar.append('kavib')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

print(taomlar)#Natija:['manti', 'somsa', 'baliq', "sho'rva", 'palov', 'shashlik', 'kavib']
print(nonushta)#Natija:['manti', 'somsa', 'baliq', "sho'rva", 'palov']

nonushta = tuple(nonushta)
nonushta.append("qaymoq va non")
print(nonushta)