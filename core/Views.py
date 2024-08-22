"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

from PyQt6 import uic, QtWidgets
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFontDatabase, QCursor, QFont


class Views:
	
	# TODO: Load ui, alter properties and connect window functionality within each function

	def __init__(self, controller):
		super(Views, self).__init__()
		self.controller = controller  # Keep a reference to the controller
	
	def overview(self, resource, dataset):
		window = QtWidgets.QMainWindow()  # Create a new QMainWindow instance
	
		qt_creator_file = "src/ui/OverviewWindow.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, window)  # Load the .ui file
		
		# Load the stylesheet file
		with open("src/css/overview.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			window.setStyleSheet(stylesheet)
		
		font_id = QFontDatabase.addApplicationFont("src/fonts/FontAwesome6-Free-Regular-400.otf")
		
		if font_id == -1:
			print("Failed to load font.")
		else:
			font_families = QFontDatabase.applicationFontFamilies(font_id)
			if font_families:
				font_family = font_families[0]  # Get the font family name
				font = QFont(font_family)
				window.setFont(font)
		
		# Set static window information
		window.setWindowTitle(f"Overview: Managing my notebooks")
		window.setMinimumSize(1400, 844)
		
		# Modify widget sizes
		ui.windowWidget.setMinimumSize(16777215, 844)
		ui.windowWidget.setMaximumSize(16777215, 16777215)
		ui.contentWidget.setMinimumSize(16777215, 826)
		ui.contentWidget.setMaximumSize(16777215, 16777215)
		ui.topContentWidget.setMinimumSize(16777215, 325)
		ui.topContentWidget.setMaximumSize(16777215, 325)
		ui.midContentWidget.setMinimumSize(16777215, 315)
		ui.midContentWidget.setMaximumSize(16777215, 315)
		
		# Widget sizes for the notebook manager
		ui.notebookManagerWidget.setMinimumSize(400, 600)
		ui.notebookManagerHeaderWidget.setMinimumSize(395, 40)
		ui.notebookManagerHeaderWidget.setMaximumSize(395, 40)
		
		# Set headline
		ui.notebookManagerTitleLabel.setText("My notebooks")
		ui.notebookManagerTitleLabel.adjustSize()
		
		# Declare button icon
		plus_icon_unicode = " \uf067"
		
		# Button setup
		ui.createButton.setText(plus_icon_unicode)
		ui.createButton.setGeometry(335, 5, 51, 31)
		ui.createButton.clicked.connect(self.controller.options)
		ui.createButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		
		# Begin TreeView
		from core.TreeModel import TreeModel
		model = TreeModel()
		tree = model.build(resource)
		
		# Set up the layout and parent widget
		from PyQt6.QtWidgets import QVBoxLayout
		layout = QVBoxLayout()
		parent_widget = ui.treeWidget
		layout.addWidget(tree)
		parent_widget.setLayout(layout)
		
		# Return this instance (current QMainWindow)
		return window
	
	def options(self):
		dialog = QtWidgets.QDialog()  # Create a new QDialog instance

		qt_creator_file = "src/ui/CreatorOptionsDialog.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, dialog)  # Load the .ui file

		# Load the stylesheet file
		with open("src/css/options-dialog-create.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			dialog.setStyleSheet(stylesheet)
		
		window_title = "Options window"
		
		# Set static window information
		dialog.setWindowTitle(f"{window_title}: What do you want to create?")
		
		ui.HeadlineLabel.setText(window_title)
		ui.HeadlineLabel.adjustSize()
		
		ui.CreateNotebookButton.clicked.connect(self.controller.add_notebook)
		ui.CreateNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		ui.CreateNotebookButton.setText("A notebook")
		
		ui.CreateNoteButton.clicked.connect(self.controller.add_note)
		ui.CreateNoteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		ui.CreateNoteButton.setText("A note")
		
		return dialog  # Return the QDialog instance
	
	def add_notebook(self):
		dialog = QtWidgets.QDialog()  # Create a new QDialog instance

		qt_creator_file = "src/ui/CreateNotebookDialog.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, dialog)  # Load the .ui file

		# Load the stylesheet file
		with open("src/css/dialog-create-notebook.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			dialog.setStyleSheet(stylesheet)
		
		window_title = "Notebook creator"
		
		# Set static window information
		dialog.setWindowTitle(f"{window_title}: Create a notebook")
		
		ui.titleWidget.setMaximumSize(744, 144)
		ui.creatorWidget.setMaximumSize(744, 144)
		
		ui.HeadlineLabel.setText(window_title)
		ui.HeadlineLabel.adjustSize()
		
		ui.WhatIsYourNotebookNameLabel.setText("What will the name of your new notebook be?")
		ui.WhatIsYourNotebookNameLabel.adjustSize()
		
		ui.AddNotebookButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		# ui.AddNotebookButton.clicked.connect(self.add_notebook_button)

		return dialog  # Return the QDialog instance
	
	def delete_notebook(self):
		pass
	
	def add_note(self):
		dialog = QtWidgets.QDialog()  # Create a new QDialog instance
		
		qt_creator_file = "src/ui/CreateNoteDialog.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, dialog)  # Load the .ui file
		
		# Load the stylesheet file
		with open("src/css/dialog-create-note.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			dialog.setStyleSheet(stylesheet)
		
		window_title = "Note creator"
		
		# Set static window information
		dialog.setWindowTitle(f"{window_title}: Create a note")
		
		ui.headlineLabel.setText(window_title)
		ui.headlineLabel.adjustSize()
		
		# Adding content
		ui.descriptionText.setText("Add a note by entering the title, a description and confirm by pressing the button if you're done!")
		ui.descriptionText.adjustSize()
		
		ui.noteName_lineEdit.setPlaceholderText("What should the title of your note be?")
		
		# Declare label content for the ComboBox into selecting a notebook for binding purposes
		ui.notebookSelectorLabel.setText("Select a notebook for this note")
		ui.notebookSelectorLabel.adjustSize()
		
		return dialog  # Return the QDialog instance
	
	def edit_notebook(self):
		pass
	
	def note_viewer(self):
		dialog = QtWidgets.QDialog()  # Create a new QDialog instance
		
		qt_creator_file = "src/ui/OpenedNoteDialog.ui"  # Define the .ui file
		ui = uic.loadUi(qt_creator_file, dialog)  # Load the .ui file
		
		# Load the stylesheet file
		with open("src/css/note-viewer-dialog.css", "r") as stylesheet_file:
			stylesheet = stylesheet_file.read()
			dialog.setStyleSheet(stylesheet)
		
		window_title = "Viewing note"
		
		# Set static window information
		dialog.setWindowTitle(f"{window_title}: Name of the note")
		
		return dialog  # Return the QDialog instance
	
	def delete_note(self):
		pass
