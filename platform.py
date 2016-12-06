import random
from PyQt4 import QtGui, QtCore
from coordinate import Coordinate
from sprite import Sprite
from ball import Ball

# eventfilter stuff ++
from PyQt4.QtCore import QEvent, pyqtSignal, QRect, Qt, QRectF, QPoint
from PyQt4.QtGui import QPen, QColor, QBrush, QImage, QPixmap
from PyQt4.QtGui import QGraphicsScene, QGraphicsView


class Platform(QtGui.QWidget):
    
    def __init__(self):
        super(Platform, self).__init__()
        self.initUI()
        self._sprite = Sprite(Coordinate(250,250), 'spiritus sanctii')
        self._ball   = Ball(Coordinate(300, 550))
        self._keymap = {Qt.Key_Q:      self.noop,
                        Qt.Key_Escape: self.noop,
                        Qt.Key_W:      self._sprite.jump,
                        Qt.Key_Up:     self._sprite.jump,
                        Qt.Key_S:      self._sprite.right,
                        Qt.Key_Down:   self.noop,
                        Qt.Key_Space:  self._sprite.jump,
                        Qt.Key_H:      self._help,
                        Qt.Key_A:      self._sprite.left,
                        Qt.Key_D:      self._sprite.right
        }

        self.installEventFilter(self)

    def _help(self):
        print('Sprite: %s' % self._sprite)
    def noop(self):
        pass

    def tick(self):
        self._sprite.tick(1/10.0)
        self._ball.tick(1/10.0)
        self.collision_detect()
        self.update()

    def collision_detect(self):
        p = self._sprite.pos
        b = self._ball.pos
        if p.distance(b) < 100:
            print('Collision')

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Jumpers crumpers')
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(p)
        self.show()

    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawSprite(qp)
        self.drawBall(qp)
        qp.end()
        
    def drawSprite(self, qp):
        pos = self._sprite.pos
        dra = self._sprite.drawable()
        p = qp.pen()
        p.setWidth(10)
        nx = pos.x - 5
        ny = 580-pos.y

        # images
        url = dra
        qi = QPixmap(url)
        pnt = QPoint(nx,ny)

        qp.drawPixmap(pnt, qi);

    def drawBall(self, qp):
        if not self._ball.is_alive():
            return False
        pos = self._ball.pos
        qp.setBrush(Qt.black)
        nx = pos.x - 5
        ny = 580-pos.y
        qp.drawEllipse(nx, ny, 10, 10)

    def eventFilter(self, obj, event):
        """We catch and absorb all key presses"""
        if event.type() == QEvent.KeyPress:
            k = event.key()
            if k in self._keymap:
                self._keymap[k]()
            return True
        else:
            return False
