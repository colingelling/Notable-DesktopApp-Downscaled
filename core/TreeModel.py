"""

    Created by Colin Gelling on 22/08/2024 (CET)
    Using Pycharm Professional

"""
from PyQt6.QtCore import Qt, QModelIndex
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView


class TreeModel(QFileSystemModel):
	
	def __init__(self):
		super(TreeModel, self).__init__()
	
	def data(self, index: QModelIndex, role: int = ...) -> object:
		if role == Qt.ItemDataRole.DisplayRole:
			file_info = self.fileInfo(index)
			return file_info.completeBaseName()
		
		return super().data(index, role)
	
	def _set_root(self, root):
		return self.setRootPath(root)
		
	def build(self, source):
		# Set source path as root
		self._set_root(source)
		
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
		