password = str(input("Saisissez votre mot de passe : "))

if len(password) < 5 :
    print("MDP trop court")
elif len(password) >= 5 and len(password) <= 10:
    print("MDP moyen")
elif len(password) > 10 :
    print("MDP Ok")

