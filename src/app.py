import sys
from PyQt6 import QtWidgets, QtCore, QtGui
from game_logic import GameLogic
from ui_main_window import Ui_MainWindow

class TheRightPriceApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.game_active = True

        self.difficulty_mapping = {
            "Easy (1-100)": "easy",
            "Hard (1-500)": "hard",
            "Extreme (1-1000)": "extreme"
        }

        self.game = GameLogic()
        self.total_time = 60
        self.remaining_time = self.total_time
        self.elapsed_ms = 0

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(10)

        self.color_animation = QtCore.QVariantAnimation()
        self.color_animation.valueChanged.connect(self.animate_color)

        self.ui.button_check.clicked.connect(self.check_guess)
        self.ui.input_guess.returnPressed.connect(self.check_guess)
        self.ui.difficulty_box.currentTextChanged.connect(self.change_difficulty)

        self.update_progress_bar_style(initial=True)


    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def update_timer(self):
        if not self.game_active:
            return

        self.elapsed_ms += 10
        seconds_passed = self.elapsed_ms / 1000
        seconds_left = self.total_time - seconds_passed
        self.remaining_time = max(0, seconds_left)

        self.ui.progress_bar.setValue(int(self.remaining_time))
        self.update_progress_bar_style()

        if int(seconds_left) != int(seconds_left + 0.01):
            self.ui.timer_label.setText(f"Time remaining: {self.format_time(int(seconds_left))}")

        if self.remaining_time <= 0:
            self.game_active = False
            self.timer.stop()
            QtWidgets.QMessageBox.information(self, "Time's up!", "You ran out of time!")
            self.reset_game()



    def update_progress_bar_style(self, initial=False):
        if self.remaining_time > 30:
            target_color = QtGui.QColor("#4CAF50")  # Green
        elif 10 < self.remaining_time <= 30:
            target_color = QtGui.QColor("#FFA500")  # Orange
        else:
            target_color = QtGui.QColor("#FF4500")  # Red

        if initial:
            self.current_color = target_color
            self.apply_progressbar_color(target_color)
        else:
            self.start_color_animation(self.current_color, target_color)

    def start_color_animation(self, from_color, to_color):
        self.color_animation.stop()
        self.color_animation.setStartValue(from_color)
        self.color_animation.setEndValue(to_color)
        self.color_animation.setDuration(500)
        self.color_animation.start()

    def animate_color(self, color):
        if isinstance(color, QtGui.QColor):
            self.apply_progressbar_color(color)
            self.current_color = color

    def apply_progressbar_color(self, color: QtGui.QColor):
        hex_color = color.name()
        self.ui.progress_bar.setTextVisible(False)
        self.ui.progress_bar.setStyleSheet(f"""
            QProgressBar {{
                border: 2px solid grey;
                border-radius: 5px;
                background-color: #FFFFFF;
            }}
            QProgressBar::chunk {{
                background-color: {hex_color};
                width: 20px;
            }}
        """)

    def check_guess(self):
        try:
            guess = int(self.ui.input_guess.text())
            result = self.game.check_guess(guess)
            self.ui.result_label.setText(result)

            if result == "Correct!":
                self.timer.stop()
                QtWidgets.QMessageBox.information(self, "Victory ! 🏆", f"You found it in {self.game.attempts} attempts!")
                self.reset_game()

        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid input", "Please enter a valid number!")

        self.ui.input_guess.clear()

    def reset_game(self):
        self.game.reset_game()

        if self.game.difficulty == "extreme":
            self.total_time = 45
        else:
            self.total_time = 60

        self.remaining_time = self.total_time
        self.elapsed_ms = 0
        self.game_active = True

        self.timer.start(10)
        self.ui.timer_label.setText(f"Time remaining: {self.format_time(self.total_time)}")
        self.ui.progress_bar.setMaximum(self.total_time)
        self.ui.progress_bar.setValue(self.total_time)
        self.update_progress_bar_style(initial=True)
        self.ui.result_label.setText("")
        self.ui.input_guess.clear()


    def change_difficulty(self, difficulty_text):
        difficulty = self.difficulty_mapping.get(difficulty_text, "easy")
        self.game.set_difficulty(difficulty)
        self.reset_game()

        if difficulty == "easy":
            self.ui.instruction.setText("Guess a number between 1 and 100")
        elif difficulty == "hard":
            self.ui.instruction.setText("Guess a number between 1 and 500")
        elif difficulty == "extreme":
            self.ui.instruction.setText("Guess a number between 1 and 1000")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TheRightPriceApp()
    window.show()
    sys.exit(app.exec())