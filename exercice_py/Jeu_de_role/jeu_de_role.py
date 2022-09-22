

from random import randint


# Vie
vie = 50
vie_eni = 50

potion = 3

separateur = "-*-"*29

print(f" Vous et l'ennemi vous disposez de {vie} points de vie chacun")
print()
while vie > 0 and vie_eni > 0:
	
	# Action à mener
	mon_attaque = randint(5, 10)
	attaque_eni = randint(5, 15)
	vie_potion = randint(15, 50)
	
	action = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
	print(separateur)
	
	print()
	
	if not action.isdigit():
		print(separateur)
		
		#action = input("Souhaitez vous attaquer (1) ou utiliser une potion (2) ? ")
		continue
		
	elif action == "1":
		vie_eni -= mon_attaque
		vie -= attaque_eni
		print(f"Vous avez infligé {mon_attaque} points de dégât à l'ennemi. ⚔️")
		print(f"L'ennemi vous a infligé {attaque_eni} points de dégât. ⚔️")
		print()
		if vie > 0:
			print(f"Il vous reste {vie} points de vie.")
		else:
			print("Il ne vous reste plus de point de vie. \U0001F643")
		if vie_eni > 0:
			print(f"Il reste {vie_eni} points de vie à l'ennemie.")
		else:
			print("L'enemmi n'a plus de point de vie.")
		print(separateur)
		print()
	
	elif action == "2":
		
		vie -= attaque_eni
		potion -= 1
		print(f"Vous avez passé votre tour...")
		if potion > 0:
			vie += vie_potion
			print(f"Il vous reste {potion} ♥ potion.")
		else:
			print(f"Attention!Il ne vous reste plus de potion.")
			#vie_potion = 0
		print(f"L'ennemi vous a infligé {attaque_eni} points de dégât. ⚔️")
		print()
		if vie > 0:
			print(f"Il vous reste {vie} points de vie.")
		else:
			print("Vous n'avez plus de vie.")
		print(f"Il reste {vie_eni} points de vie à l'ennemie.")
		print(separateur)

		
#Résultats
if vie_eni <= 0:
	print("Vous avez gagné! 💪")
elif vie <= 0:
	print("Vous avez perdu!")	
