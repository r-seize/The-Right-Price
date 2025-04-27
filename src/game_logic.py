import random

class GameLogic:
    def __init__(self):
        self.difficulty = "easy"
        self.secret_number = random.randint(1, 100)
        self.attempts = 0

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        self.reset_game()

    def reset_game(self):
        if self.difficulty == "easy":
            self.secret_number = random.randint(1, 100)
        elif self.difficulty == "hard":
            self.secret_number = random.randint(1, 500)
        elif self.difficulty == "extreme":
            self.secret_number = random.randint(1, 1000)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.secret_number:
            return "Too low!"
        elif guess > self.secret_number:
            return "Too high!"
        else:
            return "Correct!"