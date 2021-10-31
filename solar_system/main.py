import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic


class ModelSolarSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.space_object = SpaceObject(self)
        self.space_object.show()


class SpaceObject(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('space_object.ui', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelSolarSystem()
    ex.show()
    sys.exit(app.exec())
