# #opakování listu (nelze opakovat celá a desetinná čísla ale pokud jsou v listu nebo tuple tak to jde)
# for cislo in [1, 2, 3, 4, 5]:
#    print(cislo)

# #opakování stringu
# for pismeno in "abcd":
#     print(pismeno)

# #opakování slovníku
# for klic in {"jmeno": "Matous", "vek": 100, "email": None}:
#    print(klic)

# #opakování set
# for symbol in {"#", "$", "%", "&"}:
#    print(symbol)

# #program pracuje se sudými čísli, ukládá do seznamu nové hodnoty
# suda_cisla = list()

# for cislo in (1, 2, 3, 4, 5):
#     if cislo % 2 == 0:      # pokud je hodnota v proměnné "cislo" sudá
#         suda_cisla.append(cislo)  # ... přidej ji do seznamu "suda_cisla"

# # po skončení smyčky vypíšeme obsah proměnné 'suda_cisla'
# print(suda_cisla)

# #sude/liche cislo
# for cislo in (1, 2, 3, 4, 5):
#     if cislo % 2 == 0:
#         print("Sude cislo")
#     elif cislo % 2 != 0:
#         print("Liche cislo")

# #break - nechceš ve smyčce pokračovat
# for pismeno in ("a", "b", "c", "d"):
#     if pismeno == "c":
#         print("Nasel jsem 'c', preskakuji cyklus..")
#         break
#     print(pismeno)

# #continue - preskoci "a" a "b" a napsíše že hodnota "c" a "d" je důležitá
# for pismeno in ("a", "b", "c", "d"):
#     if pismeno in {"a", "b"}:
#         continue
#     print("Hodnota", pismeno, "je dulezita")


# #podmínkový zápis for - else
# for pismeno in ("a", "b", "c", "d"):
#     print(pismeno.upper())
# else:
#     print("Vsechna pismena vypsana")

# #zanořená funkce for
# jmena = [
#     ["Matous", "Marek", "Lukas", "Jan"],
#     ["Lucie", "Aneta", "Eva", "Lenka"],
#     ["Helmut", "Hammet", "Hetfield", "Harold"],
# ]

# for seznam in jmena:
#     for jmeno in seznam:
#         print(jmeno)


# for pismeno in ("a", "b", "c", "d"):
#     print(pismeno.upper())
# else:
#     print("Vsechna pismena vypsana")

# for pismeno in ("a", "b", "c", "d"):
#     if pismeno == "c":
#         print("Nasel jsem 'c', preskakuji cyklus..")
#         break
# else:
#     # kvůli 'break' se tento text nevypíše po ukončení smyčky
#     print("Vsechna pismena vypsana")

# print("Pokracuji po smycce")

# print(
#     tuple(range(11)),
#     tuple(range(1, 11)),
#     tuple(range(1, 11, 3)),
#     sep="\n"
# )

# jmena = ("Java", "C", "Rust", "Python")
# print(tuple(enumerate(jmena)))

# # Nachystáš proměnnou, stejně jako u obyčejné smyčky
# # místo prázdné struktury `list` dovnitř závorek dopíšeš celý předpis 
# # Pokud například chceš uložit všechny hodnoty jako velká písmena
# # můžeš se jménem proměnné při ukládání dodatečně pracovat

# nova_pismena = [pismeno.upper() for pismeno in "Matous"]
# print(nova_pismena)

# # dictionary comprehension
# druhe_mocniny = {cislo: cislo**2 for cislo in (1, 2, 3, 4, 5)}
# print(f"Dict: {druhe_mocniny}")

# původní slovník se všemi městy
# mesta = {
#     "Praha": 1_335_084, 
#     "Brno": 382_405, 
#     "Ostrava": 284_982,
#     "Plzen": 175_219, 
#     "Liberec": 104_261
# }

# # klasická smyčka 'for'
# nad_sto_tisic_obyv = dict()

# for mesto in mesta:
#     if mesta[mesto] > 200_000:
#         nad_sto_tisic_obyv[mesto] = mesta[mesto]
# else:
#     print(f"Klasicka smycka: {nad_sto_tisic_obyv}")

# # dict comprehensions
# nad_sto_tisic_obyv_compr = {
#     mesto: mesta[mesto]
#     for mesto in mesta
#     if mesta[mesto] > 200_000
# }
# print(f"Dict comprehension: {nad_sto_tisic_obyv_compr}")

# zadaný list listů
# jmena = [
#     ["Matous", "Marek", "Lukas", "Jan"],
#     ["Lucie", "Aneta", "Michaela", "Lenka"],
#     ["Helmut", "Hammet", "Hetfield", "Harold"]
# ]

# # klasická nestovaná smyčka
# hledana_jmena = list()

# for seznam in jmena:
#     for jmeno in seznam:
#         if jmeno.startswith("He"):
#             hledana_jmena.append(jmeno)

# print(f"klasicky postup: {hledana_jmena}")

# # nestovaná komprehence
# hledana_jmena_compr = [
#     jmeno
#     for radek in jmena
#     for jmeno in radek
#     if jmeno.startswith("He")
# ]
# print(f"Comprehension: {hledana_jmena_compr}")