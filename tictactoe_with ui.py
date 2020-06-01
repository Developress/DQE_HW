import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget, QGridLayout, QSizePolicy, \
                            QMessageBox


class MainWindow(QMainWindow):
    """Create the main window"""
    def __init__(self):
        super(MainWindow, self).__init__()

        # initialize everything before the start of the game
        self.counter = 0
        self.win_combinations = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9),
                                 (3, 5, 7))
        self.game_board = list(range(1, 10))
        self.computer_move = False
        self.mode = -1
        self.extra = "O"
        self.player = "X"
        self.central_widget = QWidget()
        self.btn_o = QPushButton(self.central_widget)
        self.btn_two_players = QPushButton(self.central_widget)
        self.btn_x = QPushButton(self.central_widget)
        self.btn_one_player = QPushButton(self.central_widget)
        self.label = QLabel(self.central_widget)
        self.buttons = {}
        self.layout = QGridLayout(self.central_widget)
        self.resize(800, 600)
        self.setWindowTitle("Tic Tac Toe")
        self.init_ui()

    def init_ui(self):
        """Initialize the elements of UI"""
        self.setCentralWidget(self.central_widget)
        self.central_widget.setStyleSheet("background-color: rgb(230, 230, 230);\n")

        # initialize the grid of buttons
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3 * i + j] = QPushButton(self.central_widget)
                self.buttons[3 * i + j].setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
                self.buttons[3 * i + j].setStyleSheet("background-color: white;\n"
                                                      "color: rgb(130, 130, 130);\n"
                                                      "font: 35pt \"Segoe UI\";\n"
                                                      "border-width: 0px;\n"
                                                      "border-style: solid;\n"
                                                      " border-radius: 10px;")
                self.layout.addWidget(self.buttons[3 * i + j], i, j)
                self.buttons[3 * i + j].hide()

        self.label.setText("Chose option")
        self.label.setGeometry(290, 140, 200, 50)
        self.label.setStyleSheet(u"font: 16pt \"Segoe UI\";")
        self.btn_one_player.setText("1 player")
        self.btn_one_player.setGeometry(290, 210, 160, 50)
        self.btn_one_player.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btn_x.setText("X")
        self.btn_x.setGeometry(290, 210, 160, 50)
        self.btn_x.setStyleSheet(
            u"background-color: rgb(130, 130, 130);"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btn_x.hide()
        self.btn_two_players.setText("2 players")
        self.btn_two_players.setGeometry(290, 280, 160, 50)
        self.btn_two_players.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btn_o.setText("O")
        self.btn_o.setGeometry(290, 280, 160, 50)
        self.btn_o.setStyleSheet(
            u"background-color: rgb(130, 130, 130);\n"
            "color: white;\n"
            "font: 12pt \"Segoe UI\";\n"
            "border-width: 0px;\n"
            "border-style: solid;\n"
            " border-radius: 10px;")
        self.btn_o.hide()

        # connect the buttons to on click functions
        self.btn_one_player.clicked.connect(self.btn_one_player_clicked)
        self.btn_two_players.clicked.connect(self.btn_two_players_clicked)
        self.btn_x.clicked.connect(self.btn_x_clicked)
        self.btn_o.clicked.connect(self.btn_o_clicked)

        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3 * i + j].clicked.connect(self.make_move)

    def btn_one_player_clicked(self):
        """Hide buttons for one player and two. Show the X and O buttons"""
        self.btn_one_player.hide()
        self.btn_two_players.hide()
        self.mode = 1
        self.btn_x.show()
        self.btn_o.show()

    def btn_two_players_clicked(self):
        """Hide buttons for one player and two. Start the game"""
        self.btn_one_player.hide()
        self.btn_two_players.hide()
        self.mode = 2
        self.start_game()

    def btn_x_clicked(self):
        """Let the user make the first move. Start the game"""
        self.computer_move = False
        self.start_game()

    def btn_o_clicked(self):
        """Let the computer make the first move. Starts the game"""
        self.computer_move = True
        self.start_game()

    def start_game(self):
        """Hide all the buttons, display the field and start the game"""
        self.label.hide()
        self.btn_x.hide()
        self.btn_o.hide()

        # display the grid of buttons
        for i in range(0, 3):
            for j in range(0, 3):
                self.buttons[3 * i + j].setText("")
                self.buttons[3 * i + j].show()

        # if the user plays with the computer and computer needs to move
        if self.mode == 1 and self.computer_move:
            self.make_computer_move()

    def make_move(self):
        """Perform the user's move and check the situation on the field"""
        self.counter += 1

        # get the button which was clicked
        sender = self.sender()

        # if the field is not occupied, then occupy it
        if sender.text() != "X" and sender.text() != "O":
            sender.setText(self.player)
        else:
            return

        # if the victory is confirmed, then form a message box and exit the game
        if self.check_for_win():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            string = "Congratulations! " + self.player + " won!"
            msg.setText(string)
            msg.setWindowTitle("Victory!")
            msg.exec()
            self.hide()

        # if all the fields are occupied, then confirm the draw,
        # form a message box and exit the game
        elif self.counter == 9:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("This is a draw")
            msg.setWindowTitle("Draw!")
            msg.exec()
            self.hide()

        # change the active player
        self.player, self.extra = self.extra, self.player

        # if the user plays with the computer and computer needs to move
        if self.mode == 1:
            self.computer_move = True
            self.make_computer_move()

    def make_computer_move(self):
        """Generate the random move and perform it"""
        move = random.randint(1, 9)

        # if the field is occupied, generates the random move again
        while self.buttons[move - 1].text() == "X" or self.buttons[move - 1].text() == "O":
            move = random.randint(1, 9)

        self.computer_move = False
        self.counter += 1

        # perform move
        self.buttons[move - 1].setText(self.player)

        # change the active player
        self.player, self.extra = self.extra, self.player

    def check_for_win(self):
        """
            Check all the win combinations to confirm the victory
            :return: True if the victory is confirmed, False if not
        """
        for i in self.win_combinations:
            win = False

            # if the field from the win combination matches with the player
            # then assign win to True
            for j in i:
                if self.buttons[j - 1].text() == self.player:
                    win = True

                # if the field from the win combination does not match with the player
                # then stop checking the current combination and check the next one
                else:
                    win = False
                    break

            # if the loop has not been breaking, then the victory is confirmed
            if win:
                return True

        # if the loop has been breaking all the time, then the victory is not confirmed
        return False


def window():
    """Create the instance of the window"""
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


window()
