"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

import os.path
import json

from PyQt6.QtGui import QFileSystemModel


class Model(QFileSystemModel):
	
	def __init__(self):
		super(Model, self).__init__()
		self.collection = None
		self.source = None

	def build_notebook_collection(self):
		# Declare and create the source as a usable resource path
		self._set_source()
		
		# Collect folders and files on system-level, put them into _preset()'s dictionary
		self._collector(self.source)
		
		# Store the full dictionary as a json file
		self._store_collection(self.source, self.collection)

	def _set_source(self):
		source = "/home/colin/Desktop/notebook-app"
		self.source = source
		
		# Create the directory
		if not os.path.exists(source):
			os.mkdir(source)

	def _collector(self, source):
		# Dictionary declaration
		self.collection = {"notebook_name_values": [], "notebook_path_values": [], "note_name_values": [], "note_path_values": []}
		
		# Scan for directories and files, build the collection with that information
		for root, dirs, files in os.walk(f"{source}/notebooks"):
			for directory in dirs:
				self.collection["notebook_name_values"].append(directory)
				self.collection["notebook_path_values"].append(os.path.join(source, directory))
			for file in files:
				self.collection["note_name_values"].append(file.replace('.txt', ''))
				self.collection["note_path_values"].append(os.path.join(source, file))

	def _store_collection(self, source, collection):
		path = f"{source}/data/"
		
		# Create the data directory
		if not os.path.exists(path):
			os.mkdir(path)
	
		# Declaration because of reusable purposes
		self.json_file = f"{path}/notebook_collection.json"
		
		# Store the collected information in a file
		with open(self.json_file, 'w', encoding='utf-8') as f:
			json.dump(collection, f, ensure_ascii=False, indent=4)
