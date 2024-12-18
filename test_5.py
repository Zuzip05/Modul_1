# # co bude vystupem?
# adjectives = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for adjective in adjectives:
#     for fruit in fruits:
#         print(adjective, fruit)

# # co bude vystupem?
# animals = ["cat", "dog", "rabbit"]

# for index, animal in enumerate(animals):
#     print(index, animal)


# #sudá čísla
# even_numbers = []
# for i in range(20):
#   if (i % 2) == 0:
#     even_numbers.append(i)
# print(even_numbers)

# #slovník
# cze2eng = {}
# cze = "Ahoj auto cervene".split(" ")
# eng = "Hi car red".split(" ")
# for cz, en in zip(cze, eng):
#   cze2eng[cz] = en
# print(cze2eng)

# #slovník zjednodušení - zrychlení
# cze2eng = {cz: en for cz, en in zip(cze, eng) if cz.islower() or en.islower()}
# print(cze2eng)

# # if podminka nekolikrat = while podminka
# #SNAKE
# for _ in range(100_000_000_000):
#   # detekuj jestli uzivatel nezmackl tlacitko
#   # uprav smer
#   # posun se o 1 prvek ve smeru
#   if board[new_y][nex_x] != " ":
#     break
#   # vykresleni situace
# # zobrazeni skore


# # piskvorky
# # 3x3
# for _ in range(3*3)
# # ==
# while board_is_empty:
  
# #while cyklus x for cyklus
# index = 1

# while index < 6:
#     print("Ještě nemáš 6, ale ", index, ", pokračuji..", sep="")
#     index += 1 # index = index + 1

# print("Hotovo, máš 6!")

# # to same pomoci for cyklu
# iterovatelny_objekt = range(1, 6)
# for index in iterovatelny_objekt:
#     print("Ještě nemáš 6, ale ", index, ", pokračuji..", sep="")
# print("Hotovo, máš 6!")

# # Napiseme si program ktery generuje cisla Fibonaciho posloupnosti (prvnich 15)
# N = 15
# fib_sequence = [0,1]
# while len(fib_sequence) < 15:
#   fib_sequence.append(fib_sequence[-2] + fib_sequence[-1])
# print(fib_sequence)

# #while/else
# index = 0

# znaky = "slakdfkjs dlhfksdlkfjskladjflkajslkdjflkasdklfasj9"
# is_found = False

# while not is_found and index < len(znaky):
#     if znaky[index] == "8":
#       print("Nasel jsem!")
#       is_found = True
#       break
#     index += 1

# else:
#     print("Nenasel jsem.")

# print(">Pokračuji pod smyčkou<")


# # jak pomoci while/else otestovat jeslti je nejake cislo prvocislo - znate prvocisla?
# maybe_prime = 683 # OK
# # maybe_prime = 684 # Neni

# n = maybe_prime - 1

# while n > 1:
#   if (maybe_prime % n) == 0:
#     print("Neni prvocislo")
#     break
#   n = n - 1
# else:
#   print(maybe_prime, " je prvocislo")

#řízené nekonečné smyčky - Kde bych ale chtěl nekončnou smyčku vlastně používat? Nejčastěji pokud se čeká na nějaky vstup od uživatele 
#a nebo obecně pokud provádíme opakovanou činnost bez předchozí znalosti kolik bude iterací.

# while True:
#     uziv_vstup = input("Zapiš libovolný text [nebo 'q' pro ukončení]: ")

#     if uziv_vstup == "q":
#         break
#     print(uziv_vstup.upper())

# print("Ukončuji ukázku!")

# #walrus operátor
# TEXT = "Zapiš jméno: ".upper()

# if (jmeno := input(TEXT)) == "Matouš":
#     print("Toto je ", jmeno, sep="")
# else:
#     print("Tak ", jmeno, ", toho neznám.", sep="")

# #zkrácené zápisy
# x += 2 #stejné jako x=x+2

#úkol
pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
prompt = "ktere písmeno chceš vyhodit?"

print("Začátek", pismena)
while len(pismena):
# while len(pismena) != 0:
    input_user = input("ktere písmeno chceš vyhodit?")
    if input_user not in pismena:
        print(input_user, "není součástí písmen!")
    else:
        pismena.remove(input_user)
    if len(pismena) != 0:
        print("Zbývají písmena", pismena)

print("Seznam je prázdný!")
