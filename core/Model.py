"""

    Created by Colin Gelling on 15/08/2024 (CET)
    Using Pycharm Professional

"""

from PyQt6.QtGui import QFileSystemModel


class Model(QFileSystemModel):
	@staticmethod
	def preset():
		return {"directory_values": [], "directory_path_values": [], "file_values": [], "file_path_values": []}

	def collector(self):
		# TODO: Look for folders and files within a particular path and return them
		pass

	def store(self):
		# TODO: Use 'dataset()' and the results of 'collector()' in order to store them together as a json file
		pass
