from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QProgressBar

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("The Right Price")
        MainWindow.resize(800, 600)  # --> + GRAND

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.title = QtWidgets.QLabel("The Right Price")
        self.title.setFont(QFont("Comic Sans MS", 32, QFont.Weight.Bold))
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)

        self.difficulty_box = QtWidgets.QComboBox()
        self.difficulty_box.addItems(["Easy (1-100)", "Hard (1-500)", "Extreme (1-1000)"])
        self.difficulty_box.setFixedWidth(200)
        self.difficulty_box.setStyleSheet("font-size: 16px;")
        self.layout.addWidget(self.difficulty_box, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.timer_label = QtWidgets.QLabel("Time remaining: 00:01:00")
        self.timer_label.setFont(QFont("Arial", 20))
        self.timer_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.timer_label)

        self.progress_bar = QProgressBar()
        self.progress_bar.setMaximum(60)
        self.progress_bar.setValue(60)
        self.progress_bar.setFixedHeight(30)
        self.layout.addWidget(self.progress_bar)

        self.instruction = QtWidgets.QLabel("Guess a number between 1 and 100")
        self.instruction.setFont(QFont("Arial", 18))
        self.instruction.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.instruction)

        self.input_guess = QtWidgets.QLineEdit()
        self.input_guess.setPlaceholderText("Enter your guess...")
        self.input_guess.setFixedHeight(40)
        self.input_guess.setFont(QFont("Arial", 16))
        self.layout.addWidget(self.input_guess)

        self.button_check = QtWidgets.QPushButton("Check")
        self.button_check.setFixedHeight(50)
        self.button_check.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.button_check)

        self.result_label = QtWidgets.QLabel("")
        self.result_label.setFont(QFont("Arial", 20))
        self.result_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.result_label)

        MainWindow.setCentralWidget(self.centralwidget)