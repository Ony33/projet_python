import json
from pathlib import Path

class CreationJson:
	def __init__(self, fichier, question, proposition):
		self.fichier = fichier
		self.question = question
		self.proposition = proposition
		
	def write_question(self, fichier, question, proposition):
		with open(self.fichier, 'r') as f:
			donnes = json.load(f)
		with open(self.fichier, 'w') as f:
			donnes[question] = []
			donnes[question] = proposition
			json.dump(donnes, f, indent = 4)
			
choix = ""
			
fichier_input = input("Veuillez choisir un fichier de questionnaire: ")
			
chemin = Path.cwd() / fichier_input

while choix != "n":
	
	question = input("Question: ")
	
	proposition_1 = input("Proposition: ")
	proposition_2 = input("Proposition: ")
	proposition_3 = input("Proposition: ")
	proposition_4 = input("Proposition: ")
	proposition = [proposition_1,
								 proposition_2,
								 proposition_3,
								 proposition_4
								]
	
	data_1 = CreationJson(chemin, question, proposition)
	data_1.write_question(chemin, question, proposition)
	
	choix = input("o/n: ")

