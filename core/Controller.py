"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

from core.CollectionModel import CollectionModel
from core.Views import Views


class Controller:
	
	def __init__(self):
		self.data_model = CollectionModel()
		self.views_model = Views(self)
		
		self.active_view = None  # Track the active QMainWindow
		self.active_dialog = None  # Track the active QDialog
		
		self.notebook_collection = self.data_model.collection
		self.notebook_path = self.data_model.notebook_path
		self.json_file = self.data_model.json_file
	
	def overview(self):
		self.data_model.build_notebook_collection()  # Initialize and build the data model
		
		self.notebook_collection = self.data_model.collection
		self.notebook_path = self.data_model.notebook_path
		self.json_file = self.data_model.json_file
		
		# Initialize and show the QMainWindow view
		self.active_view = self.views_model.overview(self.notebook_path, self.notebook_collection)
		self.active_view.show()
	
	def options(self):
		# Initialize and show the QDialog view
		self.active_dialog = self.views_model.options()
		self.active_dialog.setModal(True)
		self.active_dialog.exec()
	
	def add_notebook(self):
		if self.active_dialog:
			self.active_dialog.hide()
			
		self.active_dialog = self.views_model.add_notebook()
		self.active_dialog.setModal(True)
		self.active_dialog.exec()
	
	def add_note(self):
		if self.active_dialog:
			self.active_dialog.hide()
			
		self.active_dialog = self.views_model.add_note()
		self.active_dialog.setModal(True)
		self.active_dialog.exec()
		
	def delete_notebook(self):
		pass
	
	def delete_note(self):
		pass
	
	def edit_notebook(self):
		pass
	
	def note_viewer(self):
		self.active_dialog = self.views_model.note_viewer()
		self.active_dialog.setModal(True)
		self.active_dialog.exec()
