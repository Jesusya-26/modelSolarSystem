import sys

from solar_objects import SOLAR_OBJECTS, CLICKED_SOLAR_OBJECT

from PyQt5.QtCore import QPropertyAnimation, QPointF
from PyQt5.QtGui import QPixmap, QPainterPath, QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import uic
from main_window import Ui_MainWindow
from solar_object_info import Ui_SolarObjectInfo


class ModelSolarSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initButtons()
        self.initPaths()
        self.initAnimations()
        self.repaint()

    def initButtons(self):
        global SOLAR_OBJECTS
        solar_views = [self.sun, self.mercury, self.venerus, self.earth, self.mars,
                       self.jupiter, self.saturn, self.uran, self.neptun, self.pluton]
        for i in range(len(SOLAR_OBJECTS)):
            SOLAR_OBJECTS[i].objName = solar_views[i].objectName()
            SOLAR_OBJECTS[i].view = solar_views[i]
            SOLAR_OBJECTS[i].view.clicked.connect(self.show_info)
        self.up_button.clicked.connect(self.start)
        self.down_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def initPaths(self):
        self.paths, k, r = [], 0, 1
        for i in range(1, 10):
            path = QPainterPath()
            path.addEllipse(480 - k, 330 - k, int(r * 140), int(r * 140))
            k += 35
            r += 0.5
            self.paths.append(path)


    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        for p in self.paths:
            qp.drawPath(p)
        qp.end()

    def initAnimations(self):
        self.animations = []
        for i in range(9):
            anim = QPropertyAnimation(SOLAR_OBJECTS[i + 1].view, b'pos')
            anim.setDuration(10000 * (i + 1))
            values = [p / 100 for p in range(0, 101)]
            for j in values:
                anim.setKeyValueAt(j, self.paths[i].pointAtPercent(j))
            anim.setEndValue(QPointF(SOLAR_OBJECTS[i + 1].view.x(), SOLAR_OBJECTS[i].view.y()))
            self.animations.append(anim)

    def start(self):
        for a in self.animations:
            a.start()

    def stop(self):
        for a in self.animations:
            a.stop()

    def reset(self):
        pass

    def show_info(self):
        global CLICKED_SOLAR_OBJECT
        view = self.sender().objectName()
        for i in SOLAR_OBJECTS:
            if i.objName == view:
                CLICKED_SOLAR_OBJECT = i
                break
        self.space_object = SolarObjectInfo(self)
        self.space_object.show()


class SolarObjectInfo(QWidget, Ui_SolarObjectInfo):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(CLICKED_SOLAR_OBJECT.name)
        self.solar_object_name.setText(CLICKED_SOLAR_OBJECT.name)
        self.main_info.setText(CLICKED_SOLAR_OBJECT.to_main_info())
        self.other_info.setText(CLICKED_SOLAR_OBJECT.to_other_info())
        pix = QPixmap(CLICKED_SOLAR_OBJECT.image)
        self.img.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelSolarSystem()
    ex.show()
    sys.exit(app.exec())
