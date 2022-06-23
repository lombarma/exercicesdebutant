print("Vous allez acheter : saucisson, lait et croquettes.")
wallet = 50
print(f"Vous avez {wallet} $ dans votre porte monnaie.")
value_saucisson = int(input("Prix du saucisson ? "))
value_croquettes = int(input("Prix des croquettes ? "))
value_lait = int(input("Prix du lait ? "))
wallet = wallet - value_saucisson - value_lait - value_croquettes
if wallet < 0:
    print("Transaction annulée. Vous n'avez pas assez d'argent sur le compte.")
else:
    print(f"Transaction effectuée, il vous reste {wallet} $. ")

