import sys
from random import randrange
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 10, 131, 61))
        self.pushButton.setStyleSheet("background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(208, 203, 255), stop:1 rgba(255, 255, 255, 255));\n"
"font: 20pt \"Nirmala UI\";")
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Run"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setGeometry(200, 200, 800, 500)
        self.pushButton.clicked.connect(self.run)
        self.obj = []

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for e in self.obj:
            painter.setBrush(QBrush(e['color']))
            painter.drawEllipse(e['x'], e['y'], e['d'], e['d'])
        painter.end()

    def run(self):
        self.obj.append({'x': randrange(0, 600), 'y': randrange(0, 300), 'd': randrange(20, 200),
                         'color': QColor(randrange(0, 256), randrange(0, 256), randrange(0, 256))})
        self.update()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())