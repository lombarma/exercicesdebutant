nombre = int(input("Saisir un nombre entier : "))

somme = 0
depart = 0
while depart <= nombre:
    somme += depart
    depart += 1
print(f"La somme des nombres entre 0 et {nombre} est : {somme}")


facto = 1
n = nombre
while n != 1:
    facto *= n
    n -= 1
print(f"La factorielle de {nombre} est : {nombre}! = {facto}")
