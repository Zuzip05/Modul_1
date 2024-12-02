# zamestnanci=[ 
#     'František', 'Bruno',
#     'Anna', 'Jakub',
#     'Klára', 'Anežka',
#     'Anežka', 'Anežka'
#     ]

# # Zjisti kolikátý je poslední index
# posledni_index=len(zamestnanci)-1

# # Hodnota na druhém indexu
# print('Na indexu 2 je:'+zamestnanci[2])

# # Vypiš jméno na posledním indexu
# print ('Na ', posledni_index, ' indexu je:', zamestnanci[posledni_index])

# #vypiš jména od indexu 2 do 5
# print ('V intervalu od 2 do 5 je: ', zamestnanci[2:6])

# vypiš každý třetí prvek listu zamestnanci počínaje hodnotou 'František
# print('Každý třetí člen je:', zamestnanci [::3])
#----------------------------------------------------------------------------------------------

# jmeno='Martin'
# vaha=80
# vyska=200/100
# bmi=vaha/(vyska**2)
# if bmi<18.5:
#     kategorie= 'podvýživa'
# elif bmi>18.5 and bmi<25: 
#     kategorie= 'zdravá váha'
# elif bmi>25 and bmi<30: 
#     kategorie='mírná nadváha'
# elif bmi>30 and bmi<40:
#     kategorie='obezita'
# elif bmi>40: 
#     kategorie='těžká obezita'
# else: print ('error')


# print(jmeno, 'tvé BMI je', bmi, ', což spadá do kategorie ', kategorie, '.')
#--------------------------------------------------------------------------------------------

# # Vytvoření seznamu "zamestnanci"
# zamestnanci= ['František', 'Anna', 'Jakub', 'Klára']

# # Výpis seznamu "zamestnanci"
# print ('Zaměstnanci na začátku: ', zamestnanci)

# # Přidání nových jmen
# zamestnanci_a=zamestnanci
# zamestnanci_a.extend(['Bruno', 'Anežka'])

# # # Přidání nových jmen - verze2 
# # zamestnanci_a = zamestnanci.copy()
# # zamestnanci_a.append('Bruno')
# # zamestnanci_a.append('Anežka')

# # Výpis aktualizovaného obsahu "kandidati"
# print ('Nová jména přidána: ',zamestnanci_a)

# # Vlož string na index
# zamestnanci_b=zamestnanci
# zamestnanci_b.insert (1,"Bruno")

# # Výpis seznamu "zamestnanci"
# print ('Nová jména vložena: ', zamestnanci_b)

#-----------------------------------------------------------

# Zadané hodnoty
vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

# Vytvoř proměnnou 'cislo_dne'
cislo_dne=3

# Ověř, jestli jde o hodnotu z proměnné 'vstupni_cisla'
if cislo_dne in vstupni_cisla:
    print('Správná vstupní hodnota!')
else:
    print ('Špatná vstupní hodnota!')

# ... pokud ano, hodnotu uprav a použij jako index
    # ... u 'tyden' (1 --> 'pondělí', 2 --> 'úterý', ..)
den_tydne=tyden[cislo_dne-1]
if den_tydne.startswith(vstupni_pismena[cislo_dne-1]):
    print ("Správné písmeno")
else:
    print ("Špatné písmeno")