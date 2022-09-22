import json
import random
from pathlib import Path

fichier = Path.cwd() / "questionnaire_01.json"

class DictQuestion:
	def __init__(self, question, proposition, correct_answer, other_answer):
		self.question = question
		self.proposition = proposition
		self.correct_answer = correct_answer
		self.other_answer = other_answer

with open(fichier, 'r') as f:
	donnes = json.load(f)
	serie_question = DictQuestion(donnes[])
