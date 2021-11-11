import sys
import sqlite3

from solar_objects import SOLAR_OBJECTS

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from main_window import Ui_MainWindow


class ModelSolarSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initButtons()

    def initButtons(self):
        solar_views = [self.sun, self.mercury, self.venerus, self.earth, self.mars,
                       self.jupiter, self.saturn, self.uran, self.neptun, self.pluton]
        for i in range(len(SOLAR_OBJECTS)):
            SOLAR_OBJECTS[i].view = solar_views[i]
            SOLAR_OBJECTS[i].view.clicked.connect(self.show_description)

    def show_description(self):
        self.space_object = SpaceObject(self,)
        self.space_object.show()


class SpaceObject(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('space_object.ui', self)
        self.setWindowTitle(SOLAR_OBJECTS[3].name)
        self.spaceObjectName.setText(SOLAR_OBJECTS[3].name)
        self.description.setText(str(SOLAR_OBJECTS[3]))
        pix = QPixmap(SOLAR_OBJECTS[3].image)
        self.img.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelSolarSystem()
    ex.show()
    sys.exit(app.exec())
