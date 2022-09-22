from random import randint

computer_number = randint(0,100)
number_of_test = 5

print("*** Le jeu du mystère ***")

while number_of_test > 0:
	print()
	print(f"Il vous reste {number_of_test} essai{'s' if number_of_test > 1 else ''}")
	
	#Saisie de l'utilisateur
	print()
	user_number = input("Devine le nombre : ")
	if not user_number.isdigit():
		print("Veuillez entrer un nombre entre 0 et 100")
		continue
	
	user_number = int(user_number)
	
	if computer_number < user_number:
		print(f"Le nombre mystère est plus petit que {user_number}")
	elif computer_number > user_number:
		print(f"Le nombre mystère est plus grand que {user_number}")
	else:
		break
	number_of_test -= 1
	
#Gagné ou Perdu

if number_of_test == 0:
	print(f"Dommage! Vous avez perdu. Le nombre était : {computer_number}")
else:
	print(f"Félicitation! Le nombre mystère était bien {computer_number}")
	print(f"Vous avez trouvé le nombre en {6-number_of_test} essai")
	
print("Fin de la partie")
