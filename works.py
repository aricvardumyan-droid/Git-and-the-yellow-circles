import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.pushButton.clicked.connect(self.add_circle)

        self.circles = []

    def add_circle(self):
        diameter = random.randint(20, 100)

        max_x = self.centralWidget().width() - diameter
        max_y = self.centralWidget().height() - diameter

        if max_x > 0 and max_y > 0:
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)

            self.circles.append({
                'x': x,
                'y': y,
                'diameter': diameter
            })

            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        pen = QPen(QColor(255, 255, 0))
        pen.setWidth(2)
        painter.setPen(pen)

        for circle in self.circles:
            painter.drawEllipse(
                circle['x'],
                circle['y'],
                circle['diameter'],
                circle['diameter']
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
