import random

# gondolt_szam = random.randint(1,3)

# #print(f"a gondolt szam:{gondolt_szam}" )

# bekert_szam= int(input("kérem a tippet: "))

# if gondolt_szam == bekert_szam:
#     print("eletalaltad!!!!")

# elif gondolt_szam>bekert_szam:
#     print("nagyobbra gondoltam!!")
# else:
#     print("kissebre gondoltam!!!")

#készits függvényt elojel neven ami atvesz egy egssz szamot és az elojelet adja vissza

szam = int(input("kerek egy szamot elojellel: "))

def elojel(szam):
    if szam >= 0:
        return "+"
    else:
        return "-"

print(f"a {szam} elojele: {elojel(szam)},")

def tesztesetek():
    teszt(5,"+"):
    teszt(-3,"-")
    teszt(-1"-")
    teszt(0"+")
    teszt(1"+")
    #...

def teszt(szam, elvart_elojel):
    if elojel (szam) == elvart_elojel:
        print(f"elojel({szam}))== {elvart_elojel} true")
    else:
        print(f"elojel({szam}))== {elvart_elojel} false")




