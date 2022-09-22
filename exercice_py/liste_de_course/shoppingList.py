import ui



def menuButton(sender):
	sender.title = ''
	tableau = ui.TableView()
	tableau.background_color = '#b29e84'
	cell = ui.TableViewCell()
	cell.text_label.text = 'Ajouter'
	
	
	#tableau.data_source = 'Ajouter'
	v.add_subview(tableau)
	v.add_subview(cell)
	
	
	
	
v = ui.load_view()

v.name = 'Liste de course'

button = ui.Button()

button.action = menuButton

v.add_subview(button)

v.present('sheet')
