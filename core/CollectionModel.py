"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

import os.path
import json


class CollectionModel:
	
	def __init__(self):
		super(CollectionModel, self).__init__()
		self.source = None
		
		self.collection = None
		self.notebook_path = None
		
		self.data_path = None
		self.json_file = None

	def build_notebook_collection(self):
		# Declare and create the source as a usable resource path
		self._set_source()
		
		# Collect folders and files on system-level, put them into _preset()'s dictionary
		self._collector(self.source)
		
		# Store the full dictionary as a json file
		self._store_collection(self.source, self.collection)

	def _set_source(self):
		self.source = "/home/colin/Desktop/notebook-app"
		
		# Create the directory
		if not os.path.exists(self.source):
			os.mkdir(self.source)

	def _collector(self, source):
		# Dictionary declaration
		self.collection = {"notebook_name_values": [], "notebook_path_values": [], "note_name_values": [], "note_path_values": []}
		self.notebook_path = f"{source}/notebooks"
		
		# Scan for directories and files, build the collection with that information
		for root, dirs, files in os.walk(self.notebook_path):
			for directory in dirs:
				self.collection["notebook_name_values"].append(directory)
				self.collection["notebook_path_values"].append(os.path.join(source, directory))
			for file in files:
				self.collection["note_name_values"].append(file.replace('.txt', ''))
				self.collection["note_path_values"].append(os.path.join(source, file))

	def _store_collection(self, source, collection):
		self.data_path = f"{source}/data/"
		
		# Create the data directory
		if not os.path.exists(self.data_path):
			os.mkdir(self.data_path)
	
		# Declaration because of reusable purposes
		self.json_file = f"{self.data_path}/notebook_collection.json"
		
		# Store the collected information in a file
		with open(self.json_file, 'w', encoding='utf-8') as f:
			json.dump(collection, f, ensure_ascii=False, indent=4)
