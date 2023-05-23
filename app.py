# LOOPAR


for a in range(2023,1972,-4):
    print(a)


x = 12
y = 20

for a in range(x,y+1,3):
    print(a)


x = 12
y = 20
a = x
while a <= y:
    print(a)
    a = a + 3


print("")
# # Skriv ett program som matar in texter. ¨
# # Skriver man in "Slut" (case insensitive"!) 
# # ska programmet avslutas och den LÄNGSTA texten man matat in skrivs ut

# # Ange en text: ste
# # Ange en text: he
# # Ange en text: Slut

# # Längsta texten du skrev in var : hejsan hoppsan

longestSoFar = ""
while True:
    text = input("Ange en text:")
    text = text.upper()
    if text == "Slut":
        break
    if len(text) > len(longestSoFar):
        longestSoFar = text

# print(f"Längsta texten du skrev in var :{longestSoFar}")



# # Utifrån denna kravspec, skriv en funktion som räknar ut 
# # bonus på lön
# # calculateBonus(grundLön, fler parametrar??? )

# # Om man är mer än 30 år har man 4% bonus
# # Om man är  chef så har man 1000 kr bonus
# def calculateBonus(baseSalary,age,isboss):
#     bonus = 0
#     if age >= 30: 
#         bonus = bonus + (baseSalary*0.04)        
#     if isboss == True:
#         bonus = bonus + 1000
#     return bonus        

# print(calculateBonus(1000,30,False))
# print(calculateBonus(1000,29,False))
# print(calculateBonus(1000,30,False))







def berakna_area(figur, param1, param2=None):
    if figur == "rektangel":
        langd = param1
        bredd = param2
        area = langd + bredd
        return area
    elif figur == "triangel":
        bas = param1
        hojd = param2
        area = 0.5 * bas * hojd
        return area
    else:
        return "Okänd geometrisk figur"
print(berakna_area("rektangel",10,10))
print(berakna_area("triangel",10,10))

#Tydligen finns en bugg i koden, Fix it :)