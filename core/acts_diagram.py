import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QSplitter, QLabel, QLineEdit, QHBoxLayout, \
    QPushButton


class ActsFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.diagram = QPixmap('')

        self.topRight = QFrame()
        self.topRight.setFrameShape(QFrame.StyledPanel)
        self.botRight = QFrame()
        self.botRight.setFrameShape(QFrame.StyledPanel)


        self.leftFrame = QFrame()
        self.leftFrame.setFrameShape(QFrame.StyledPanel)

        self.labelLeft = QLabel("", self.leftFrame)
        self.labelLeft.setAlignment(Qt.AlignCenter)
        self.labelLeft.setPixmap(self.diagram)

        self.rightFrame = QFrame()
        self.rightFrame.setFrameShape(QFrame.StyledPanel)

        splitter2 = QSplitter(Qt.Horizontal)

        splitter2.addWidget(self.leftFrame)
        splitter2.addWidget(self.rightFrame)
        splitter2.setSizes([30, 14])

        hbox = QHBoxLayout(self)
        hbox.addWidget(splitter2)

        self.textbox_errors = QLineEdit("", self.botRight)
        self.textbox_errors.readOnly = True
        self.textbox_errors.move(10, 180)
        self.textbox_errors.setFrame(False)
        font = QFont()
        font.setPointSize(11)
        self.textbox_errors.setFont(font)
        self.textbox_errors.setMinimumSize(15, 15)
        self.textbox_errors.setMaximumSize(300, 20)
        self.textbox_errors.resize(300, 20)

        self.textbox_errors.setStyleSheet('background-color: #f0f0f0; border: none; color: red;')

        self.setLayout(hbox)
        self.crt()


    def crt(self):
        self.system = QLineEdit(self.rightFrame)
        self.system.move(10, 5)
        self.system.resize(100, 20)
        self.system.setPlaceholderText('название системы')

        self.actor = QLineEdit(self.rightFrame)
        self.actor.move(10, 40)
        self.actor.resize(120, 20)
        self.actor.setPlaceholderText('эктор')
        self.actor_nick = QLineEdit(self.rightFrame)
        self.actor_nick.move(140, 40)
        self.actor_nick.setPlaceholderText('сокращение')
        self.actor_nick.resize(80, 20)
        self.actor_b = QPushButton('создать', self.rightFrame)
        self.actor_b.move(230, 40)

        self.action = QLineEdit(self.rightFrame)
        self.action.move(10, 65)
        self.action.resize(120, 20)
        self.action.setPlaceholderText('действие')
        self.action_nick = QLineEdit(self.rightFrame)
        self.action_nick.move(140, 65)
        self.action_nick.setPlaceholderText('сокращение')
        self.action_nick.resize(80, 20)
        self.action_b = QPushButton('создать', self.rightFrame)
        self.action_b.move(230, 65)







class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.createMenus()
        self.area = ActsFrame()
        self.setCentralWidget(self.area)

    def createMenus(self):
        self.update = self.menuBar().addAction("&Обновить", self.update)

        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addSeparator()

        self.editMenu = self.menuBar().addMenu("&Edit")
        self.editMenu.addSeparator()

        self.helpMenu = self.menuBar().addMenu("&Help")

    def update(self):
        self.area.update()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.setGeometry(1000, 1000, 1000, 600)
    ex.setWindowTitle('диаграмма прецедентов')
    ex.show()
    sys.exit(app.exec_())