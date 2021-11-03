import sys
import sqlite3
import math

from PyQt5.QtGui import QPixmap, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel
from PyQt5 import uic

DATA = list(sqlite3.connect('solar_objects_db.db').cursor().execute("""SELECT * FROM SolarObjects"""))
DATA = [list(i) for i in DATA]


class ModelSolarSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main_window.ui', self)
        self.repaint()
        self.earth.clicked.connect(self.run)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        k = 0
        r = 1
        for i in range(1, 10):
            qp.drawEllipse(480 - k, 330 - k, int(r * 140), int(r * 140))
            k += 35
            r += 0.5
        qp.end()

    def run(self):
        self.space_object = SpaceObject(self,)
        self.space_object.show()


class SpaceObject(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('space_object.ui', self)
        self.setWindowTitle(DATA[3][1])
        self.spaceObjectName.setText(DATA[3][1])
        self.description.setText('Земля́ — третья по удалённости от Солнца планета Солнечной системы. \nСамая плотная, пятая по диаметру и массе среди всех планет '
                                 'и крупнейшая\n среди планет земной группы, в которую входят также Меркурий, Венера\n и Марс. '
                                 'Единственное известное человеку в настоящее время тело \nСолнечной системы в частности и Вселенной вообще, населённое живыми \nорганизмами.')
        pixmap = QPixmap('earth.png')
        self.img.setPixmap(pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelSolarSystem()
    ex.show()
    sys.exit(app.exec())
