"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor, QFont


class Views(QtWidgets.QMainWindow):

	# TODO: Load ui, alter properties and connect window functionality within each function

	def __init__(self, controller):
		super(Views, self).__init__()
		self.controller = controller  # Keep a reference to the controller

	def overview(self):
		qt_creator_file = "src/ui/OverviewWindow.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, self)  # Load the .ui file

		# Load the stylesheet file
		with open("src/css/overview.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			self.setStyleSheet(stylesheet)
		
		font_id = QFontDatabase.addApplicationFont("src/fonts/FontAwesome6-Free-Regular-400.otf")

		if font_id == -1:
			print("Failed to load font.")
		else:
			font_families = QFontDatabase.applicationFontFamilies(font_id)
			if font_families:
				font_family = font_families[0]  # Get the font family name
				font = QFont(font_family)
				self.setFont(font)

		# Set static window information
		self.setWindowTitle(f"Overview: Managing my notebooks")
		self.setMinimumSize(1400, 844)
		
		# Modify widget sizes
		ui.windowWidget.setMinimumSize(16777215, 844)
		ui.windowWidget.setMaximumSize(16777215, 16777215)
		ui.contentWidget.setMinimumSize(16777215, 826)
		ui.contentWidget.setMaximumSize(16777215, 16777215)
		ui.topContentWidget.setMinimumSize(16777215, 325)
		ui.topContentWidget.setMaximumSize(16777215, 325)
		ui.midContentWidget.setMinimumSize(16777215, 315)
		ui.midContentWidget.setMaximumSize(16777215, 315)
		
		ui.notebookManagerWidget.setMinimumSize(400, 600)
		ui.notebookManagerHeaderWidget.setMinimumSize(395, 40)
		ui.notebookManagerHeaderWidget.setMaximumSize(395, 40)
		
		ui.notebookManagerTitleLabel.setText("My notebooks")
		ui.notebookManagerTitleLabel.adjustSize()
		
		plus_icon_unicode = " \uf067"
		
		ui.createButton.setText(plus_icon_unicode)
		ui.createButton.setGeometry(335, 5, 51, 31)
		ui.createButton.clicked.connect(self.controller.options)
		ui.createButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		
		# Return this instance (current QMainWindow)
		return self

	def options(self):
		dialog = QtWidgets.QDialog()  # Create a new QDialog instance
	
		qt_creator_file = "src/ui/CreatorOptionsDialog.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, dialog)  # Load the .ui file
		
		window_title = "Options window"
		
		# Set static window information
		self.setWindowTitle(f"{window_title}")
		
		ui.HeadlineLabel.setText(window_title)
		ui.HeadlineLabel.adjustSize()
		
		# ui.CreateNotebookButton.clicked.connect(WindowController.create_notebook_dialog)
		ui.CreateNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		ui.CreateNotebookButton.setText("A notebook")
		
		# ui.CreateNoteButton.clicked.connect(WindowController.create_note_dialog)
		ui.CreateNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		ui.CreateNoteButton.setText("A note")
		
		return dialog  # Return the QDialog instance

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
