"""17-dars:INPUT() VA WHILE.
Boboxonov Husanboy"""

input()
ism = input('Ismingizni nima?')
savol = f'Assalomu alekum, {ism.title()}. Yoshingiz nechada?'
yosh = input(savol)
yosh = int(yosh)
height = input('Boyingiz necha?')
height = float(height)  # Natija:
# Ismingizni nima?Husanboy
# Assalomu alekum, Husanboy. Yoshingiz nechada?19
# Boyingiz necha?1.69

# while
son = 1
while son <= 2:
    print(son, end=' ')
    son += 1
print('Dastur tugadi:')  # Natija:1 2 3 4 5 Dastur tugadi:

# while and input
print('Kiritgan soning kvadiratni qaytaruvchi dastur.')
savol = 'Istalgan soni kiriting,'
savol += "(dasturnni toxtatish uvhun 'exit' deb yozing)"
qiymat = ''
while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(f'{qiymat}ning kvadirati {float(qiymat) ** 2}ga teng')  # Natija:
# Kiritgan soning kvadiratni qaytaruvchi dastur.
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)4
# 4ning kvadirati 16.0ga teng
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)exit

# ishora
print('Kiritgan soning kvadiratni qaytaruvchi dastur.')
savol = 'Istalgan soni kiriting,'
savol += "(dasturnni toxtatish uvhun 'exit' deb yozing)"
ishora = True
while ishora:
    savol1 = input(savol)
    if savol1 == 'exit':
        ishora = False
    else:
        print(f'{savol1}ning kvadirati {float(savol1) ** 2}ga teng') # Natija:
# Kiritgan soning kvadiratni qaytaruvchi dastur.
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)6
# 4ning kvadirati 36.0ga teng
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)exit

# break while
print('Kiritgan soning kvadiratni qaytaruvchi dastur.')
savol = 'Istalgan soni kiriting,'
savol += "(dasturnni toxtatish uvhun 'exit' deb yozing)"

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(f'{qiymat}ning kvadirati {float(qiymat) ** 2}ga teng')
        print('Dastur tugadi:')  # Natija:
# Kiritgan soning kvadiratni qaytaruvchi dastur.
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)6
# 4ning kvadirati 36.0ga teng
# Istalgan soni kiriting,(dasturnni toxtatish uvhun 'exit' deb yozing)exit

# break for
sonlar = list(range(1, 11))
for i in sonlar:
    if i == 5:
        break
    else:
        print(f'{i}ning kvadiratini {i * i}')  # Natija:
# 1ning kvadiratini 1
# 2ning kvadiratini 4
# 3ning kvadiratini 9
# 4ning kvadiratini 16

# Continue while
sonlar = list(range(1, 11))
for i in sonlar:
    if i == 5:
        continue
    else:
        print(f'{i}ning kvadiratini {i * i}')  # Natija:
# 1ning kvadiratini 1
# 2ning kvadiratini 4
# 3ning kvadiratini 9
# 4ning kvadiratini 16
# 6ning kvadiratini 36
# 7ning kvadiratini 49
# 8ning kvadiratini 64
# 9ning kvadiratini 81
# 10ning kvadiratini 100

son = 0
while son <= 10:
    son += 1
    if son % 2 != 0:
        continue
    print(son, end=' ')  # Natija:2 4 6 8 10

# infinite Loop
son = 0
while son <= 10:
    if son % 2 != 0:
        continue
    print(son, end=' ')

son = 0
while son <= 10:
    if son % 2 != 0:
        continue
    print(son, end=' ')
    son += 1

son = 0
while son > 10:
    son += 1
    if son % 2 != 0:
        continue
    print(son, end=' ')

"""AMALIYOT"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

kitob = 'Yaxshi korgan kitobizni kiriting>>'
kitob += "(dastur 'stop' so'zini  yozsangiz toxtaydi.)"
qiymat = ''
while True:
    qiymat = input(kitob)
    if qiymat.lower() == 'stop':
        break
print('(dastur toxtadi)')

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm,
# 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini
# so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni
# ham tekshiring).

savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)

    if yosh < 7:
        narh = 2000
    elif 7 <= yosh < 18:
        narh = 3000
    elif 18 <= yosh < 65:
        narh = 10000
    else:
        narh = 0

    if narh == 0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")

# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda.
# Xatolarni to'g'rilay olasizmi?

savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    elif float(qiymat) < 0:
        continue  # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
    else:
        ildiz = float(qiymat) ** 0.5
        print(f"{qiymat} ning ildizi {ildiz} ga teng")
