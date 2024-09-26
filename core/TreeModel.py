"""

    Created by Colin Gelling on 26/08/2024 (CET)
    Using Pycharm Professional

"""

from PyQt6.QtCore import QModelIndex, Qt
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView

from core.Controller import Controller


class TreeModel(QFileSystemModel):
	
	def __init__(self, parent=None):
		super(TreeModel, self).__init__(parent)
		
		self.index_model = None
		self.absolute_path = None
	
	def data(self, index: QModelIndex, role: int = ...) -> object:
		if role == Qt.ItemDataRole.DisplayRole:
			file_info = self.fileInfo(index)
			return file_info.completeBaseName()
		
		return super().data(index, role)
	
	def build(self, source):
		# Set source path as root
		self.setRootPath(source)
		
		# Build the QTreeView based on the source path
		tree_view = QTreeView()
		tree_view.setModel(self)
		tree_view.setRootIndex(self.index(source))
		
		# Tree customization, hide column names
		header = tree_view.header()
		header.setSectionHidden(0, False)
		header.setSectionHidden(1, True)
		header.setSectionHidden(2, True)
		header.setSectionHidden(3, True)
		header.hide()
		
		# Declare custom stylesheet
		tree_view.setStyleSheet(
			'background-color: #fff;'
			'color: #000;'
			'border: 0;'
			'margin: 0;'
			'selection-color: #000; '
			'selection-background-color: rgba(0, 0, 0, 0);'
		)
		
		return tree_view
	
	def collect_note_data(self, index, data):
		self.index_model = index.model()
		self.absolute_path = self.filePath(index)

		# Unpack groups of lists from the collection
		notebook_name_values = [value for key, value in data.items() if key == 'notebook_name_values']
		note_name_values = [value for key, value in data.items() if key == 'note_name_values']
		note_path_values = [value for key, value in data.items() if key == 'note_path_values']

		selected_notebook_value = [value for value in notebook_name_values[0] if f"/{value}/" in self.absolute_path]

		selected_note_path_value = [value for value in note_path_values[0] if value == self.absolute_path]

		if selected_note_path_value:
			file_content = None
			with open(selected_note_path_value[0], "r") as file:
				file_content = file.read()

			file_name = [value for value in note_name_values[0] if value in selected_note_path_value[0]]

			separate_description = file_content.split(file_name[0] + '\n\n')
			description_text = ''.join(separate_description)

			file_information = {
				"filePath": selected_note_path_value[0],
				"fileName": file_name[0],
				"parentDirectory": selected_notebook_value[0],
				"fileContent": description_text
			}

			return file_information