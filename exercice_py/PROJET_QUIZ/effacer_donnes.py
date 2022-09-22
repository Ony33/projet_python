import json
from pathlib import Path

chemin = Path.cwd() / "questionnaire_01.json"

with open(chemin, 'r') as f:
	donnes = json.load(f)
with open(chemin, 'w') as f:
	del donnes
