import json

chemin = "/private/var/mobile/Containers/Shared/AppGroup/26E32128-2B18-4FFB-935D-9813DE402DEB/File Provider Storage/Exo_py/json/test.json"

with open(chemin, "r") as f:
	donnees = json.load(f)
donnees.append(11)

with open(chemin, "w") as f:
	json.dump(donnees, f, indent=4)

print(donnees)
