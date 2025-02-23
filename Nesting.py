"""16-dars:NESTING.
Boboxonov Husanboy"""

# Lug'atlar ro'yxati
car0 = {
    'model': 'lacetti',
    'rang': 'oq',
    'yil': 2018,
    'narh': 13000,
    'km': 50000,
    'karobka': 'avtomat'
}

car1 = {
    'model': 'nexia 3',
    'rang': 'qora',
    'yil': 2015,
    'narh': 9000,
    'km': 89000,
    'karobka': 'mexanika'
}

car2 = {
    'model': 'gentra',
    'rang': 'qizil',
    'yil': 2019,
    'narh': 15000,
    'km': 20000,
    'karobka': 'mexanika'
}
car = car0
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, {car['narh']}$")  # Natija:Lacetti,oq rang,2018-yil, 13000$

car = car2
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, {car['narh']}$")  # Natija:Gentra,qizil rang,2019-yil, 15000$

car = car1
print(f"{car['model'].title()},"
      f"{car['rang']} rang,"
      f"{car['yil']}-yil, {car['narh']}$")  # Natija:Nexia 3,qora rang,2015-yil, 9000$

cars = [car0, car1, car2]
for car3 in cars:
    print(f"{car3['model'].title()},"
          f"{car3['rang']} rang,"
          f"{car3['yil']}-yil, {car3['narh']}$")  # Natija:
# Lacetti,oq rang,2018-yil, 13000$
# Nexia 3,qora rang,2015-yil, 9000$
# Gentra,qizil rang,2019-yil, 15000$

print(cars[0]['model'])  # Natija:lacetti

print(f"{cars[2]['rang'].title()} "
      f"{cars[2]['model']}")  # Natija:Qizil gentra

malibus = []
for i in range(10):
    new_car = {
        'model': 'malibu',
        'rang': None,
        'yil': 2020,
        'narh': None,
        'km': 0,
        'karobka': 'avto'
    }
    malibus.append(new_car)

# for malibu in malibus:
#     print(malibu)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

for malibu in malibus[6:]:
    malibu['rang'] = 'qora',
    malibu['karobka'] = 'mexakia'

for malibu in malibus:
    print(malibu)  # Natija:
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': None, 'km': 0, 'karobka': 'mexakia'}

for malibu in malibus:
    if malibu['karobka'] == 'avto':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000

for malibu in malibus:
    print(malibu)  # Natija:
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qizil', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': 'qora', 'yil': 2020, 'narh': 40000, 'km': 0, 'karobka': 'avto'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexakia'}
# {'model': 'malibu', 'rang': ('qora',), 'yil': 2020, 'narh': 35000, 'km': 0, 'karobka': 'mexakia'}

# LUG'AT ICHIDA RO'YXAT

dasturchilar = {
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quydagi dasturlash tillarni biladi ")
    for til in tillar:
        print(f"{til.upper()}", end='')  # Natija:
# Ali quydagi dasturlash tillarni biladi
# PYTHONC++
# Vali quydagi dasturlash tillarni biladi
# HTMLCSSJS
# Hasan quydagi dasturlash tillarni biladi
# PHPSQL
# Husan quydagi dasturlash tillarni biladi
# PYTHONPHP
# Maryam quydagi dasturlash tillarni biladi
# C++C#

# LUG'AT ICHIDA LUG'AT
hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }
for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f"{info['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti: {info['malumot']}. \n"
          "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(til.upper())

"""AMALIYOT"""

olim1 = {
    'ism': 'Alisher Navoiy',
    't_yil': 1441,
    'v_yil': 1501,
    'y_joy': 'Hirot',
    'asarlar': ['Xamsa', 'Lison ut-Tayr', 'Mahbub Al-Qulub']
}
olim2 = {
    'ism': 'Ibn Ismoil',
    't_yil': 810,
    'v_yil': 870,
    'y_joy': 'Buxoro',
    'asarlar': ['Al-jome', 'as-sahih', 'Al-adab', 'al-mufrad']
}
olim3 = {
    'ism': 'Avdulla Qodiriy',
    't_yil': 1894,
    'v_yil': 1938,
    'y_joy': 'Toshkent',
    'asarlar': ['Otkan kunlar', 'Mehrobdan chayon', 'obit ketmon']
}
olim4 = {
    'ism': 'Erkin Vohidov',
    't_yil': 1936,
    'v_yil': 2016,
    'y_joy': 'Fargona',
    'asarlar': ['Tong nafasi', 'Qoshiqlarim sizga', 'Ozbegim', 'Qiziquvchan Matmusa']

}
olimlar = [olim1, olim2, olim3, olim4]
for olim in olimlar:
    print(f"{olim['ism'].title()},{olim['t_yil']}-yilda"
          f" {olim['y_joy'].title()} tavallud topgan,{olim['v_yil']- olim['t_yil']} yil umur korgan.")
# Alisher Navoiy,1441-yilda Hirot tavallud topgan,60 yil umur korgan.
# Ibn Ismoil,810-yilda Buxoro tavallud topgan,60 yil umur korgan.
# Avdulla Qodiriy,1894-yilda Toshkent tavallud topgan,44 yil umur korgan.
# Erkin Vohidov,1936-yilda Fargona tavallud topgan,80 yil umur korgan.

olimlar = [olim1, olim2, olim3, olim4]
for olim in olimlar:
    print(f" {olim['ism'].title()}nig mashur asarlari:")
    for asar in olim['asarlar']:
        print(asar)
#  Alisher Navoiynig mashur asarlari:
# Xamsa
# Lison ut-Tayr
# Mahbub Al-Qulub
#  Ibn Ismoilnig mashur asarlari:
# Al-jome
# as-sahih
# Al-adab
# al-mufrad
#  Avdulla Qodiriynig mashur asarlari:
# Otkan kunlar
# Mehrobdan chayon
# obit ketmon
#  Erkin Vohidovnig mashur asarlari:
# Tong nafasi
# Qoshiqlarim sizga
# Ozbegim
# Qiziquvchan Matmusa



kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)





davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }

for davlat, info in davlatlar.items():
    if davlat.lower()=='aqsh':
        davlat = davlat.upper()
    else:
        davlat = davlat.capitalize()
    print(f"\n{davlat}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul birligi']}")