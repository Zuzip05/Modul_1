# #Vytvoří nový prázdný slovník user_1,
# user_1={}
# #doplní do slovníku user_1 klíč name (hodnota "Marek") a surname (hodnota "Parek")
# user_1["name"]="Marek"
# user_1["surname"]="Parek"
# #pomocí vhodné metody rozšíří stávající slovník user_1 o zadanou proměnnou user_email
# user_email={'email':'marek.parek@gmail.com'}
# user_1.update(user_email)
# #vypiš hodnoty nového slovníku user_1 s úvodním textem "User #01:".
# print ('User #01:', user_1)


#------------------------------------------

# #zapiš proměnné
# jmeno = 'Marek'
# heslo = '1234'
# uzivatel = {'Marek': '1234'}

# #zapiš podmínku, která zkontroluje, jestli se hodnoty v proměnných jmeno a heslo shodují s klíčem a hodnotou ve slovníku uzivatel
# if uzivatel.get(jmeno) == heslo:
# # ... pokud SOUHLASÍ, přivítej uživatele jménem
#     print ('Ahoj ', jmeno, 'vítej v aplikaci! Pokračuj...')

# #pokud nesouhlasí, upozorni uživatele o omylu
# else:
#     print ('Uživatelské jméno nebo heslo nejsou v pořádku')


#-------------------------------------------------------
# #zapiš proměnné
# cisla_1 = (1, 1, 2, 3, 4)
# cisla_2 = (5, 6, 7, 7, 8)

# #vytvoř ze zadaných proměnných sety
# set_1=set(cisla_1)
# set_2=set(cisla_2)

# #udělá sjednocení hodnot obou nově vzniklých setů a uloží jej do proměnné sjednocene_hodnot
# sjednocene_hodnoty=set_1.union(set_2)

# #vypíše výsledek s ohlášením "Sjednocené hodnoty ze zadání:".
# print('Sjednocené hodnoty ze zadání:',sjednocene_hodnoty)

#---------------------------------------------------------

cisla_1 = {1, 2, 3, 4}
cisla_2 = {3, 4, 5, 6}

#vytvoř ze zadaných proměnných sety
set_1=set(cisla_1)
set_2=set(cisla_2)

#zjistí jaké hodnoty prvního setu jsou rozdílné oproti setu druhému a uloží hodnoty do proměnné rozdil_cisel
rozdil_cisel=set_1.difference(set_2)

#vypíše výsledek s ohlášením
print ("Rozdílné hodnoty prvního setu oproti druhému:",rozdil_cisel)