#--------------ÚKOL 1------------------
# #V této úloze vytvoř program, který spočítá kolik samohlásek a souhlásek obsahuje zadaný string

# #Vytvoř proměnnou veta, typu str, která obsahuje hodnotu: "Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu"
# veta = 'Zvuk řeči je produkován poměrně otevřenou konfigurací vokálního traktu'

# #vytvoř proměnou samohlásky, která bude obsahovat 'aeiouáéíóú'
# samohlasky='aeiouáéíóú'

# #proměnnou souhlasky, typu str, která obsahuje 'bcčdďfghjklmnňprřsštťvzžcdž'
# souhlasky='bcčdďfghjklmnňprřsštťvzžcdž'

# #proměnnou vysledek, typu dict, který obsahuje klíče "souhlasky" a "samohlasky". Slovník bude evidovat výskyty těchto hodnot
# vysledek={'souhlasky':0, 'samohlasky':0}

# #iteraci přes všechny znaky v proměnné veta
# for pismeno in veta:
# #pokud znak není ani samohláska, ani souhláska, tak jej přeskoč
#     if not pismeno.isalpha ():
#         continue
# # pokud je znak samohláska nebo souhláska, inkrementuj ve slovníku vysledek správný klíč
# # pokud je samohláska
#     elif pismeno.lower () in samohlasky:
#         vysledek['samohlasky'] +=1
# #pokud jsou souhlásky
#     elif pismeno.lower() in souhlasky:
#         vysledek ['souhlasky'] +=1
# # nakonec vypiš konečný stav podle ukázky níže.
# print ('Počet souhlásek: ',vysledek['souhlasky'], ' | Počet samohlásek: ',vysledek['samohlasky'])

#--------------ÚKOL 2------------
# Vytvoř program, který sečte všechna sudá a všechna lichá čísla
# Vypiš absolutní hodnotu rozdílu těchto součtů

# #Zapiš hodnoty do proměnné 
# cisla = [1, 2, 3, 4, 5, 6, 7, 8]
# licha=0
# suda=0

# #sečti všechna sudá čísla
# for cislo in cisla:
#     if cislo % 2 == 0:
#         suda=suda+cislo

# #sečti všechna lichá čísla
#     else:
#         licha=licha+cislo

# #rozdíl mezi těmito dvěma součty (proměnná vysledek)
# vysledek=abs(suda - licha)

# print ('Rozdíl je:', vysledek)

#--------------ÚKOL 3------------
#program, který potřebuje od uživatele start, stop a delitel
#Po zapracování vypíše všechna celá čísla v intervalu od start, do stop, která jsou dělitelná hodnotou v delitel

# #Zapiš hodnoty do proměnné uvedené výš.
# vysledek = []
# start = 3
# stop = 9
# delitel = 3

# #ověř jestli jsou proměnné start, stop a delitel datový typ int (pomocí built-in funkce isinstance),pokud jsou int, vypiš oznámení dle ukázky níž
# if isinstance(start,int) \
#         and isinstance (stop,int) \
#         and isinstance (delitel,int):
#     print ('Zadaný rozsah:<',start,', ',stop,'>')
## Iteruj skrze rozsah zadaných čísel
#     for number in range(start,stop+1):
# # .. pokud je vybrané číslo dělitelné hodnotou v prom. "delitel"
#         if number % int(delitel)==0:
# # .. přidej jej do seznamu "vysledek"
#             vysledek.append(number)
# # doplň výpis hodnot v proměnné 'vysledek'
#     print ('Čísla dělitelná',delitel,':',vysledek)
# else:
#     print ('Zadané vstupy musí být čísla.')

#------------------Úkol 4-----------------
# #Pomocí slovníkové komprehence spočítej délky slov v zadané sekvenci
# seznam_slov=["jablko", "pomeranč", "banán", "kiwi", "hruška"]
# delky_slov={slovo:len(slovo)for slovo in seznam_slov}
# print (delky_slov)