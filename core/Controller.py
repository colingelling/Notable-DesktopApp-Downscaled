"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QDialog


class Controller(QtWidgets.QMainWindow, QDialog):

	# TODO: Use a minimized version of the WindowController functionality for 'navigate', load views within the other functions
	# Reminder, use these functions to intercept the data-model before passing it to views

	def overview(self):
		qt_creator_file = "src/ui/OverviewWindow.ui"
		uic.loadUi(qt_creator_file, self)  # Load the .ui file
		self.show()

	def options(self):
		pass

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
