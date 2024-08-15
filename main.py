"""

    Created by Colin Gelling on 15/08/2023 (CET)
    Using Pycharm Professional

"""

from PyQt6 import QtWidgets


def main():
	# App window declaration
	app = QtWidgets.QApplication(sys.argv)

	from core.Controller import Controller
	controller = Controller()
	controller.overview()
	
	# Startup
	sys.exit(app.exec())


# Instantiate app
if __name__ == '__main__':
	import sys
	main()
