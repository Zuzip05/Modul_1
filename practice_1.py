#Prvních 5 písmen slova "indexování"
print("Prvních 5 písmen:" )
print("indexování"[:5])

#Posledních 5 písmen slova "indexování"
print("Posledních 5 písmen:")
print("indexování"[-5:])

#Každé 3. písmeno (počínaje prvním) od 'i':
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print ("indexování"[::3])

#Převodní poměry
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

#Počet jednotek
kg_pocet = 80
km_pocet = 54
l_pocet = 5

#Výpočty
kg_vysledek=kg_lb*kg_pocet
km_vysledek=km_mile*km_pocet
l_vysledek=l_gal*l_pocet

print(kg_pocet,"kg je",kg_vysledek,"lb")
print(km_pocet,"km je",km_vysledek,"mil")
print(l_pocet,"l je",l_vysledek,"gal")

#Proměnné
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000

#Sleva
sleva_merc=5_000

#Cena za 2 merc
cena_2_merc=2*mercedes

#Cena za Mercedes a Rolls-Royce
cena_merc_a_rolls=mercedes+rolls_royce

#Cena za dva Rolls-Royce s příplatkovou výbavou (každý z nich)
cena_2_rolls_s_vybavou=2*(rolls_royce+vybava)

#Cena za Mercedes s příplatkovou výbavou
cena_merc_s_vybavou=mercedes+vybava

#Cena po slevě Mercedesu
merc_se_slevou=mercedes-sleva_merc

# výpis informací
print("Sleva na Mercedes:", sleva_merc)
print("Cena za dva Mercedesy je:", cena_2_merc)
print("Cena za Mercedes a Rolls-Royce:", cena_merc_a_rolls)
print("Cena za dva Rolls-Royce s příplatkovou výbavou:", cena_2_rolls_s_vybavou)
print("Cena za Mercedes s příplatkovou výbavou:", cena_merc_s_vybavou)
print("Cena za Mercedes po slevě:", merc_se_slevou)

#proměnné, spojení, délka
jmeno= "Lukáš"
prijmeni= "Dvořák"
cele_jmeno=jmeno+ " "+ prijmeni
delka_jmena=len(cele_jmeno)

print("Celé jméno:", cele_jmeno)
print("Délka jména:", delka_jmena)
print ("="*delka_jmena)
print (cele_jmeno)
print ("="*delka_jmena)