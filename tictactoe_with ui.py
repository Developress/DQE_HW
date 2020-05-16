from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout, QSizePolicy, QMessageBox
import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle("Tic Tac Toe")
        self.initUi()

    def initUi(self):
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("background-color: rgb(230, 230, 230);\n")
        self.layout = QGridLayout(self.centralWidget)
        self.buttons = {}
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3*i + j] = QPushButton(self.centralWidget)
                self.buttons[3*i + j].setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
                self.buttons[3*i + j].setStyleSheet("background-color: white;\n"
                    "color: rgb(130, 130, 130);\n"
                    "font: 35pt \"Segoe UI\";\n"
                    "border-width: 0px;\n"
                    "border-style: solid;\n"
                    " border-radius: 10px;")
                self.layout.addWidget(self.buttons[3*i + j], i, j)
                self.buttons[3*i + j].hide()
        self.label = QLabel(self.centralWidget)
        self.label.setText("Сhoose option")
        self.label.setGeometry(290, 140, 200, 50)
        self.label.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.btnOnePlayer = QPushButton(self.centralWidget)
        self.btnOnePlayer.setText("1 player")
        self.btnOnePlayer.setGeometry(290, 210, 160, 50)
        self.btnOnePlayer.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btnX = QPushButton(self.centralWidget)
        self.btnX.setText("X")
        self.btnX.setGeometry(290, 210, 160, 50)
        self.btnX.setStyleSheet(
            u"background-color: rgb(130, 130, 130);"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btnX.hide()
        self.btnTwoPlayers = QPushButton(self.centralWidget)
        self.btnTwoPlayers.setText("2 players")
        self.btnTwoPlayers.setGeometry(290, 280, 160, 50)
        self.btnTwoPlayers.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btnO = QPushButton(self.centralWidget)
        self.btnO.setText("O")
        self.btnO.setGeometry(290, 280, 160, 50)
        self.btnO.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btnO.hide()
        self.btnOnePlayer.clicked.connect(self.btnOnePlayerClicked)
        self.btnTwoPlayers.clicked.connect(self.btnTwoPlayersClicked)
        self.btnX.clicked.connect(self.btnXClicked)
        self.btnO.clicked.connect(self.btnOClicked)
        self.player = "X"
        self.extra = "O"
        self.mode = -1
        self.computerMove = False
        self.gameboard = list(range(1, 10))
        self.winCombinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9),
                           (3, 5, 7))
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3*i + j].clicked.connect(self.makeMove)
        self.counter = 0

    def btnOnePlayerClicked(self):
        self.btnOnePlayer.hide()
        self.btnTwoPlayers.hide()
        self.mode = 1
        self.btnX.show()
        self.btnO.show()
    def btnTwoPlayersClicked(self):
        self.btnOnePlayer.hide()
        self.btnTwoPlayers.hide()
        self.mode = 2
        self.startGame()
    def btnXClicked(self):
        self.computerMove = False
        self.startGame()
    def btnOClicked(self):
        self.computerMove = True
        self.startGame()
    def startGame(self):
        self.label.hide()
        self.btnX.hide()
        self.btnO.hide()
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3 * i + j].setText("")
                self.buttons[3*i + j].show()
        if self.mode == 1 and self.computerMove:
            self.makeComputerMove()

    def makeMove(self):
        self.counter+=1
        sender = self.sender()
        if sender.text() != "X" and sender.text() != "O":
            sender.setText(self.player)
        else:
            return
        if self.checkForWin():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            string = "Congratulations! " + self.player + " won!"
            msg.setText(string)
            msg.setWindowTitle("Victory!")
            msg.exec()
            self.hide()
        elif self.counter == 9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("This is a draw")
            msg.setWindowTitle("Draw!")
            msg.exec()
            self.hide()
        self.player, self.extra = self.extra, self.player
        if self.mode == 1:
            self.computerMove = True
            self.makeComputerMove()
    def makeComputerMove(self):
        move = random.randint(1, 9)
        while self.buttons[move - 1].text() == "X" or self.buttons[move - 1].text() == "O":
            move = random.randint(1, 9)
        self.computerMove = False
        self.counter += 1
        self.buttons[move-1].setText(self.player)
        self.player, self.extra = self.extra, self.player

    def checkForWin(self):
        for i in self.winCombinations:
            for j in i:
                if self.buttons[j-1].text() != self.player:
                    win = False
                    break
                else:
                    win = True
            if win:
                return True
        return False


def window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

window()