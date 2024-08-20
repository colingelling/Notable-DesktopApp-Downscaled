"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

from core.Views import Views


class Controller:
	
	def __init__(self):
		self.views_model = Views(self)
		
		self.active_view = None  # Track the active QMainWindow
		self.active_dialog = None  # Track the active QDialog
	
	def overview(self):
		# Initialize and show the QMainWindow view
		self.active_view = self.views_model.overview()
		self.active_view.show()
	
	def options(self):
		# Initialize and show the QDialog view
		self.active_dialog = self.views_model.options()
		self.active_dialog.setModal(True)
		self.active_dialog.exec()
	
	def add_notebook(self):
		pass
	
	def delete_notebook(self):
		pass
	
	def add_note(self):
		pass
	
	def edit_note(self):
		pass
	
	def delete_note(self):
		pass
