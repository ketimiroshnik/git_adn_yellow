import sys
from random import randrange
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setGeometry(200, 200, 800, 500)
        self.pushButton.clicked.connect(self.run)
        self.obj = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setBrush(QBrush(QColor(255, 186, 0)))
        for e in self.obj:
            painter.drawEllipse(e['x'], e['y'], e['d'], e['d'])
        painter.end()

    def run(self):
        self.obj.append({'x': randrange(0, 600), 'y': randrange(0, 300), 'd': randrange(20, 200)})
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())