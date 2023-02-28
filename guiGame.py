from board import Board
import time
from PySide2.QtGui import QFont
from PySide2.QtCore import QSize, QCoreApplication, QRect, QMetaObject
from PySide2.QtWidgets import QPushButton, QLabel, QMessageBox
from PySide2.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget
from PySide2.QtWidgets import QMenuBar, QStatusBar
import copy


colours = {
    'a': u"background-color: rgb(255, 255, 255);",
    'b': u"background-color: rgb(0, 0, 225);",
    'c': u"background-color: rgb(255, 225, 0);",
    'd': u"background-color: rgb(170, 0, 0);",
    'e': u"background-color: rgb(85, 170, 0);",
    'f': u"background-color: rgb(225, 0, 225);",
    'g': u"background-color: rgb(156, 170, 146);",
    'h': u"background-color: rgb(225, 0, 0);",
    'i': u"background-color: rgb(0, 225, 225);",
    'j': u"background-color: rgb(0, 225, 0);",
    0: u"background-color: rgb(0, 0, 0);"
}


class Ui_GameWindow(object):

    def __init__(self, height, width, types, matrix=None):
        self.width = width
        self.height = height
        self.types = types
        if matrix:
            self.board = Board(width, height, types, matrix)
        else:
            self.board = Board(width, height, types)
        self.przycisk1 = None
        self.przycisk2 = None
        self.points = 0
        self.level = 1
        self.threshold = 50
        self.buttonList = []
        self.record = 0

    def updatePoints(self):
        self.punkty_label.setText(QCoreApplication.translate(
            "MainWindow", f"Punkty: {str(self.points)}", None))
        self.mainWindow.repaint()
        if self.points >= self.threshold:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText(f'Poziom: {str(self.level+1)}')
            msgBox.setWindowTitle("Nowy poziom")
            msgBox.exec()
            self.board = Board(self.width, self.height, self.types)
            self.paintBoard(True)
            self.updateLevel()
            self.threshold += self.threshold * self.level

    def updateLevel(self):
        self.level += 1
        self.poziom_label.setText(QCoreApplication.translate(
            "MainWindow", f"Poziom: {str(self.level)}", None
            )
            )

    def blocksExchange(self):

        współrzędne1 = self.przycisk1
        współrzędne2 = self.przycisk2
        if Board.checkPosition(współrzędne1, współrzędne2):
            matrix = copy.deepcopy(self.board.matrix())
            if Board.exchangePossibility(współrzędne1, współrzędne2, matrix):
                self.board.changePlaces(współrzędne1, współrzędne2)
                while Board.findThreesOnBoard(self.board.matrix()):
                    self.board.markThrees()
                    self.points += self.board.countPoints() * self.level
                    self.paintBoard()
                    self.board.removeThrees(True)
                    self.paintBoard()
                self.updatePoints()
                if self.board.findOpportunities() is None:
                    self.finishGame()
        self.przycisk1 = None
        self.przycisk2 = None

    def getRecord(self):
        record = 0
        try:
            with open('record.txt', 'r') as file:
                record = int(file.read())
                file.close()
        except Exception:
            self.record = record
        return record

    def buttonPushed(self, y, x):
        if self.przycisk1 == (y, x):
            self.przycisk1 = None
            return
        if self.przycisk1 is None:
            self.przycisk1 = y, x
            return
        else:
            self.przycisk2 = y, x
            self.blocksExchange()

    def finishGame(self):
        message = f'Gratulacje!\nTwój wynik: {self.points}'
        if self.points > int(self.record):
            with open('record.txt', 'w') as file:
                file.writelines(str(self.points))
                file.close()
                message = f'NOWY REKORD!!!\nTwój wynik: {self.points}'
        self.rekord_label.setText(QCoreApplication.translate(
            "MainWindow", f"Rekord: {str(self.record)}", None))
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("KONIEC GRY")
        msgBox.exec()


    def paintBoard(self, newLevel=False):
        if self.board.matrix() is not None:
            for rowNumber in range(len(self.board.matrix())):
                row = self.board.matrix()[rowNumber]
                for columnNumber in range(len(row)):
                    type = self.board.type(rowNumber, columnNumber)
                    self.paintButton(rowNumber, columnNumber, type)
            if not newLevel:
                time.sleep(500 / 1000)

    def paintButton(self, row, column, type):

        button = self.buttonList[row][column]
        colour = colours[type]
        button.setStyleSheet(colour)
        self.mainWindow.repaint()

    def createButton(self, line, column):
        button = QPushButton(self.centralwidget)
        button.setMinimumSize(QSize(30, 30))
        button.setMaximumSize(QSize(150, 150))
        colour = colours[self.board.type(line, column)]
        button.setStyleSheet(colour)
        button.setObjectName(u"Button" + str(line) + str(column))
        button.line = line
        button.column = column
        button.setText("")

        def pushButton():
            self.buttonPushed(line, column)
        button.clicked.connect(pushButton)
        return button

    def setupUi(self, GameWindow):
        self.mainWindow = GameWindow
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.resize(900, 900)
        self.centralwidget = QWidget(GameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.MainLayout = QVBoxLayout()
        self.MainLayout.setObjectName(u"MainLayout")
        self.tekstHLayout = QHBoxLayout()
        self.tekstHLayout.setObjectName(u"tekstHLayout")
        self.punkty_label = QLabel(self.centralwidget)
        self.punkty_label.setObjectName(u"punkty_label")
        self.punkty_label.setMaximumSize(QSize(16777215, 20))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.punkty_label.setFont(font)

        self.tekstHLayout.addWidget(self.punkty_label)

        self.poziom_label = QLabel(self.centralwidget)
        self.poziom_label.setObjectName(u"poziom_label")
        self.poziom_label.setMaximumSize(QSize(16777215, 20))
        self.poziom_label.setFont(font)

        self.tekstHLayout.addWidget(self.poziom_label)

        self.rekord_label = QLabel(self.centralwidget)
        self.rekord_label.setObjectName(u"rekord_label")
        self.rekord_label.setMaximumSize(QSize(16777215, 20))
        self.rekord_label.setFont(font)

        self.tekstHLayout.addWidget(self.rekord_label)

        self.MainLayout.addLayout(self.tekstHLayout)

        self.BlocksVLayout = QVBoxLayout()
        self.BlocksVLayout.setObjectName(u"BlocksVLayout")

        for line in range(self.board.height()):

            HLayout = QHBoxLayout()
            HLayout.line = line
            self.buttonList.append([])

            for column in range(self.board.width()):
                button = self.createButton(line, column)
                self.buttonList[line].append(button)
                HLayout.addWidget(button)

            self.BlocksVLayout.addLayout(HLayout)

        self.MainLayout.addLayout(self.BlocksVLayout)

        self.HelpButton = QPushButton(self.centralwidget)
        self.HelpButton.setObjectName(u"HelpButton")

        def hint():
            współrzędne = self.board.findOpportunities()
            if współrzędne is None:
                self.finishGame()
            else:
                self.przycisk1 = współrzędne[0]
                self.przycisk2 = współrzędne[1]
                self.blocksExchange()

        self.HelpButton.clicked.connect(hint)
        self.MainLayout.addWidget(self.HelpButton)

        self.verticalLayout_3.addLayout(self.MainLayout)

        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GameWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 690, 30))
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GameWindow)
        self.statusbar.setObjectName(u"statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GameWindow)
        QMetaObject.connectSlotsByName(GameWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.punkty_label.setText(QCoreApplication.translate(
            "MainWindow", u"Punkty: 0", None))
        self.poziom_label.setText(QCoreApplication.translate(
            "MainWindow", u"Poziom: 1", None))
        self.rekord_label.setText(QCoreApplication.translate(
            "MainWindow", f"Rekord: {str(self.record)}", None))
        self.HelpButton.setText(QCoreApplication.translate(
            "MainWindow", u"Pomocy", None))
