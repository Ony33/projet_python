import json
from pathlib import Path

chemin = Path.cwd() / "liste.json"
#print(chemin.suffix) .json 

menu = "Choisissez parmi les 5 options suivantes : \n"
menu += "1: Ajouter un élément à la liste\n"
menu += "2: Retirer un élément de la liste\n"
menu += "3: Afficher la liste\n"
menu += "4: Vider la liste\n"
menu += "5: Quitter"

liste_de_course = []
choix = ""
separateur = "-*-" * 13
while choix != "5":
	print(menu)
	print(separateur)
	choix = input("Votre choix : ")
	if choix == "1":
		print(separateur)
		ajout = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
		liste_de_course.append(ajout)
		print(f"=> L'élément {ajout} a bien été ajouté à la liste")
		with open(chemin, "r") as f:
			liste_de_course = json.load(f)
			liste_de_course.append(ajout)
		with open(chemin, "w") as f:
			json.dump(liste_de_course, f, indent=4)
	elif choix == "2":
		print(separateur)
		soustrait = input("Quel élément voulez vous enlever : ")
		for j in liste_de_course:
			if soustrait == j:
				liste_de_course.remove(soustrait)
				print(f"=> L'élément {soustrait} a bien été enlevé")
				with open(chemin, "r") as f:
					liste_de_course = json.load(f)
					liste_de_course.remove(soustrait)
				with open(chemin, "w") as f:
					json.dump(liste_de_course, f, indent=4)
	elif choix == "3":
		with open(chemin, "r") as f:
				liste_de_course = json.load(f)
		if len(liste_de_course) != 0:
			print("Voici le contenu de la liste :")
			a = 1
			
			for i in liste_de_course:
				print(f"{a}: {i}")
				a += 1

		else:
			print("Votre liste de course est vide")
	elif choix == "4":
		liste_de_course.clear()
		with open(chemin, "r") as f:
			liste_de_course = json.load(f)
			liste_de_course.clear()
		with open(chemin, "w") as f:
			json.dump(liste_de_course, f, indent=4)
		print("=> Votre liste de course a été vidé")
	elif choix == "5":
		print("A bientôt!")
	else:
		print(menu)
		choix = int(input("Votre choix : "))
    
        
    
