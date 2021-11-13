import sys

from solar_objects import SOLAR_OBJECTS, CLICKED_SOLAR_OBJECT, START_POSITION

from PyQt5.QtCore import QPropertyAnimation, Qt, QPointF
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
        self.initOrbits()
        self.initAnimations()
        self.repaint()

    def initButtons(self):
        global SOLAR_OBJECTS
        global START_POSITION
        solar_views = [self.sun, self.mercury, self.venerus, self.earth, self.mars,
                       self.jupiter, self.saturn, self.uran, self.neptun, self.pluton]
        for i in range(len(SOLAR_OBJECTS)):
            SOLAR_OBJECTS[i].objName = solar_views[i].objectName()
            SOLAR_OBJECTS[i].view = solar_views[i]
            SOLAR_OBJECTS[i].view.clicked.connect(self.show_info)
        for i in range(1, 10):
            START_POSITION.append((solar_views[i].x(), solar_views[i].y()))
        self.up_button.clicked.connect(self.start)
        self.down_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    def initOrbits(self):
        self.orbits = []
        k, r = 0, 1
        for i in range(1, 10):
            orbit = QPainterPath()
            orbit.addEllipse(480 - k, 330 - k, int(r * 140), int(r * 140))
            k += 35
            r += 0.5
            self.orbits.append(orbit)

    def initAnimations(self):
        self.animations = []
        for i in range(9):
            anim = QPropertyAnimation(SOLAR_OBJECTS[i + 1].view, b'pos')
            anim.setDuration(10000 * (i + 1))
            values = [p / 100 for p in range(0, 101)]
            for j in values:
                anim.setKeyValueAt(j, self.orbits[i].pointAtPercent(j))
            anim.setLoopCount(10000)
            self.animations.append(anim)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for p in self.orbits:
            qp.drawPath(p)
        qp.end()

    def start(self):
        for a in self.animations:
            if self.sender().objectName() == 'down_button':
                a.setDirection(0)
            else:
                a.setDirection(1)
            a.start()

    def stop(self):
        for a in self.animations:
            a.pause()

    def reset(self):
        for a in self.animations:
             a.stop()
        for i in range(9):
            SOLAR_OBJECTS[i + 1].view.move(START_POSITION[i][0], START_POSITION[i][1])

    def show_info(self):
        global CLICKED_SOLAR_OBJECT
        view = self.sender().objectName()
        for i in SOLAR_OBJECTS:
            if i.objName == view:
                CLICKED_SOLAR_OBJECT = i
                break
        self.space_object = SolarObjectInfoWindow(self)
        self.space_object.show()


class SolarObjectInfoWindow(QWidget, Ui_SolarObjectInfo):
    def __init__(self, *args):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(CLICKED_SOLAR_OBJECT.name)
        self.solar_object_name.setText(CLICKED_SOLAR_OBJECT.name)
        self.solar_object_name.resize(self.solar_object_name.sizeHint())
        self.main_info.setText(CLICKED_SOLAR_OBJECT.to_main_info())
        self.main_info.resize(self.main_info.sizeHint())
        self.other_info.setText(CLICKED_SOLAR_OBJECT.to_other_info())
        self.other_info.resize(self.other_info.sizeHint())
        pix = QPixmap(CLICKED_SOLAR_OBJECT.image)
        self.img.setPixmap(pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ModelSolarSystem()
    ex.show()
    sys.exit(app.exec())
