#https://colab.research.google.com/drive/1ScqfWg5DTt-cl4oSEBdIzHwJyDMCzX8r?usp=sharing#scrollTo=kDpZKkkW_ahp

# heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
# heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
# heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
# heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
# heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
# heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
# heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

# heslo = heslo_4
# je_spravne = True

# if len(heslo) < 8:
#   print("FAIL -> \"Heslo musí být alespoň 8 znaků dlouhé\"")
#   je_spravne = False

# if heslo[0].isnumeric():
#   print("FAIL -> \"Heslo nesmí začínat číselným znakem\"")
#   je_spravne = False

# else:
#   print("PASS -> \"Heslo je v pořádku\"")

# #slovníky
# muj_prvni_slovnik={"klic":"hodnota"}
# muj_prvni_slovnik ["klic"]

# cze_to_eng = {"ahoj": "hi", "jak":"how", "mesto":"city", "dvojka":2 }
# print (cze_to_eng["ahoj"])
# print (cze_to_eng ["jak"])

# jmeno=input ("Zadej jmeno:")
# {"jmeno":jmeno}

# # zmenitelny
# muj_druhy_slovnik = dict(klic="hodnota")
# muj_druhy_slovnik["klic"] = "nova_hodnota"
# muj_druhy_slovnik["klic"]

# # nema poradi
# muj_druhy_slovnik = dict(klic="hodnota")
# muj_druhy_slovnik[0]

# osoba = ("Matouš", "Holinka", "matous@holinka.com", "+420 777 666 555")

# # klic -> hodnotu
# # jmeno -> "Matouš"
# # prijmeni -> "Holinka"
# # email -> "matous@holinka.com"
# # telefon -> "+420 777 666 555"

# osoba = {
#     "jmeno": "Matouš",
#     "prijmeni": "Holinka",
#     "email": "matous@holinka.com",
#     "cislo": "+420 777 666 555"
# }
# print(osoba)


# # klic se nemuze menit
# # klic musi byt unikatni
# # hodnota vsechno

# osoba = {
#     "jmeno": "Petr",
#     "prijmeni": "Lorenc",
#     "vek": 28,
#     "navstivene_zeme": ("Nemecko", "Malta"),
#     "email": {
#         "jmeno": "xxx",
#         "domena": "seznam.cz"
#     }
# }

# # ktery zapis je lepsi, a proc? nejake nazory
# uzivatele = [
#     {"name": "Petr", "surname": "x1"},
#     {"name": "pavel", "surname": "x2"},
# ]

# #ingredience jsou list, nástroje je slovník
# recept_palacinka={
#     "ingredients":[
#         "eggs",
#         "salt",
#         "flour",
#         "milk"
#         ],
#     "tools": {
#         "main_tool": "pan",
#         "stirring_tool": "spoon"
#         },
#     "prep time": 5
#   }

#---------------------------------------------------------

# mrazena_pizza = {
#     "peceni": {
#         "doba": {
#             "hodnota": 20,
#             "jednotka": "minut"
#         },
#         "teplota": {
#             "hodnota": 180,
#             "jednotka": "C"
#         }
#     },
#     "ingredience": ["testo", "sugo", "mozzarella", "parmezan", "rajcatka", "bazalka"]
# }

# aktualni_teplota=100

# if aktualni_teplota <= 0.8*mrazena_pizza ['peceni'] ['teplota'] ['hodnota']:
#     print ("Pridej vykon")
# elif aktualni_teplota <=1.5* mrazena_pizza ['peceni'] ['teplota'] ['hodnota']:
#     print ("Uber vykon")
# else:
#     print ("Nesahej na to.")

#--------------------------------------------------------------------------------------

# hockey = {
#     "league": "NHL",
#     "Teams": 32,
#     "Players": [
#         {"name": "Rudy Gay", "position": "Center", "goals": 38},
#         {"name": "Lewis Carroll", "position": "Left Wing", "goals": 29},
#         {"name": "Matt Gasparro", "position": "Defense", "goals": 22},
#         {"name": "Dave Carroll", "position": "Goalie", "goals": 0}
#     ]
# }

# print(hockey["Players"])

#-------------------------------------------------------------------------

# key = "cislo"
# if key in osoba:
#   print(osoba[key])
# else:
#   print("Klic zde neni")

#   key = "cislo"
# osoba.get(key, "Klic zde neni")

# #----------------------------------------------------

# #setdaufalt frekvence v projetku
# {'jmeno': 'Pavel',
#  'prijmeni': 'Lorenc',
#  'vek': 28,
#  'navstivene_zeme': ('Nemecko', 'Malta'),
#  'email': {'jmeno': 'xxx', 'domena': 'seznam.cz'},
#  'puvodni_jmeno': 'Petr'}
# osoba.setdefault("puvodni_prijmeni", "Lorenc")

#----------------------------------------------------------

#PRO PROJEKT ZAPAMATOVAT
# {}.get()
# {}.setdefault()

# #množina {} po spuštění se smažou duplicity a změní pořadí - chlupaté závorky, v množině je rychlejší vyhledávání obsahu
# #slovník {klíč:hodnota}
# #list [] oproti množině nechá všechno i duplicity i pořadí - hranaté závorky
# #tuple () to stejné jako list, ale nelze změnit - kulaté závorky
# zensky_rod {"žena","růže","píseň", "kost", "kost"}
# suda_cisla {2,4,6,8,0}
# pismena {"a","b","c","d"}


# #----------------------------------------------------------------------
# #sjednocení = UNION -> odstraní duplicity ale nechá jinak úplně všechno
# muj_set_A = {"žena", "růže", "píseň", "kost", "Lucie", "Matouš"}
# muj_set_B = {"žena", "růže", "píseň", "kost", "Lukáš"}

# print(muj_set_B.union(muj_set_A))
# print(muj_set_A | muj_set_B)

# #průnik -> jenoom to stejné
# print(muj_set_B.intersection(muj_set_A))
# print(muj_set_A & muj_set_B)

# #rozdíl-> hraje roli pořadí! zůstane jenom to co v druhém není co je unikátní v dané množině
# print(muj_set_A.difference(muj_set_B))
# print(muj_set_A - muj_set_B)

# #symetrický rozdíl-> prvky, které nejsou společné
# print(muj_set_B.symmetric_difference(muj_set_A))
# print(muj_set_A ^ muj_set_B)

#--------------------------------------------------------------

