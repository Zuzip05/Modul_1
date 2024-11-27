# #Datový typ:int,str,float,list,tuple

# #Objekt = je všechno co někde je, co má hodnotu. VŠECHNO CO MÁ DATOVÝ TYP JE OBJEKT -má to hodnotu a tu můžu vyvolat jako id(False) a vidím číslo specifické pouze pro tohle. Když dám type (False) vidím typ boll

# #BOOLEAN - TRUE=1, FALSE=0 (každé číslo kladné i záporné bude True, false je jen 0 a „none“ - stejné jako null ale to v pythonu není tady se používá none)


# #jak uživateli Matouš omezím přístup?
# jmeno="Matouš"
# vek=11


# #jak potvrdím, že osoba Ladislav Dvořák patří zaměstnanci firmy?
# zamestnanci=("Ladislav Dvořák","Nikola Lehká", "Jitka Adamová")

# print (bool (1))
# print (bool (0))

# #True je vždy pokud obsahuje nějaká data, má nějaké hodnoty, délka výrazu je větší než 0
# print (bool("matous"))
# print (bool(["a", "b"]))

# #False je vždy pokud je obsah prázdný
# print (bool(""))
# print (bool([]))

# #co tady uvidím? vždycky true je jedno co tam je napsáno není to prázdný!
# print (bool("0"))
# print (bool("False"))


# #srovnávací operace (== rovnost, != nerovnost)
# print(bool(144 > 1))     # True
# print(bool(144 == 142))  # False
# print(bool(144 != 100))  # True

# #lze porovnat int a float ale nelze srovnávat se str - pozor funkce input vzdy vrati string musí se prevest na int
# print (bool("1"==1)) #False

# #operátory ke spojování - and, or, not (prioritu má prvně not, pak and, pak or)
# a=10
# print (bool(a>0 and a<100))
# print (bool(a==0 or a==100))

# #srovnání identit (is, is not)
# list1=[1,2,3]
# list2=[1,2,3]
# print(list1 is list2) # false - každý list má svoje id

list1=[1,2,3]
list2=list1
print (list1 is list2) #true - seznam je jen jeden druhý odkazuje na první, je to stejné