import ui
from pathlib import Path
import json

fenetre_principal = ui.View()
fenetre_principal.name = 'Quiz'
fenetre_principal.background_color = '#D8DCE2'

fichier = input('Question : ')
chemin = Path.cwd() / fichier
		
def button_01_tapped(sender):
	fenetre_secondaire = ui.View()
	fenetre_secondaire.name = 'Questionnaire 01'
	fenetre_secondaire.background_color = '#D8DCE2'
	
	fenetre_secondaire.present('full_screen')
	
		
def add_bouton(question, x, y):
	bouton = ui.Button(title = question)
	bouton.tint_color = '#FFFFFF'
	bouton.x = x
	bouton.y = y
	bouton.flex = 'BW'
	bouton.width = 25
	bouton.height = 35
	bouton.corner_radius = 5
	bouton.background_color = '#426283'
	bouton.action = button_01_tapped
	fenetre_principal.add_subview(bouton)
	return
	
buton_1 = add_bouton('questionnaire 1', 35, 20)
buton_2 = add_bouton('questionnaire 2', 35, 60)
buton_3 = add_bouton('questionnaire 3', 35, 100)
buton_4 = add_bouton('questionnaire 4', 35, 140)
buton_5 = add_bouton('questionnaire 5', 35, 180)
buton_6 = add_bouton('questionnaire 6', 35, 220)
buton_7 = add_bouton('questionnaire 7', 35, 260)
buton_8 = add_bouton('questionnaire 8', 35, 300)

print(buton_1)

fenetre_principal.present('full_screen')
