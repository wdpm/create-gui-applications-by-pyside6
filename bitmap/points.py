import sys

from random import choice, randint  # <1>

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel()
        self.canvas = QPixmap(400, 300)
        self.canvas.fill(Qt.GlobalColor.white)
        self.label.setPixmap(self.canvas)
        self.setCentralWidget(self.label)
        self.draw_something()

    # tag::draw_something[]
    def draw_something(self):
        painter = QPainter(self.canvas)
        pen = QPen()
        pen.setWidth(3)
        painter.setPen(pen)

        for n in range(1000):
            painter.drawPoint(
                200 + randint(-100, 100),
                150 + randint(-100, 100),  # x  # y
            )
        painter.end()
        self.label.setPixmap(self.canvas)

    # end::draw_something[]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
