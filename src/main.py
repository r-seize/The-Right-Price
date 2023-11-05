import tkinter as tk
import random
from tkinter import messagebox
import threading
import time

class Rightprice:
    def __init__(self, root):
        self.root = root
        self.root.title("The Right price")
        self.root.geometry("400x350")

        self.titre_ascii = tk.Label(root, text="The Right price", font=("Courier", 20))
        self.titre_ascii.pack()

        self.timer_time = 60
        self.remaining_time = self.timer_time
        self.timer_label = tk.Label(root, text=f"Temps restant: {self.timer_time} secondes")
        self.timer_label.pack()

        self.secret_price = random.randint(1, 100)
        self.test_number = 0
        self.game_active = True

        self.label = tk.Label(root, text="I choose a price between 1 and 100 and try to guess it.")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Verify", command=self.check_proposal)
        self.button.pack()

        self.timer_thread = threading.Thread(target=self.count_minute)
        self.timer_thread.start()

    def check_proposal(self):
        if self.game_active:
            proposition = int(self.entry.get())
            self.test_number += 1

            if proposition < self.secret_price:
                message = "Too small ! Try again"
            elif proposition > self.secret_price:
                message = "Too big ! Try again"
            else:
                message = f"Great! You've put {self.test_number} trying to find the right price."
                self.test_number = 0
                self.secret_price = random.randint(1, 100)
                self.display_victory_message(message)

            self.label.config(text=message)
            self.entry.delete(0, tk.END)

    def count_minute(self):
        while self.remaining_time > 0:
            time.sleep(1)
            self.remaining_time -= 1
            self.timer_label.config(text=f"Time remaining: {self.remaining_time} seconds")

        self.display_victory_message("Time's up! The game is over.")

    def display_victory_message(self, message):
        self.game_active = False
        result = messagebox.askquestion("Congratulations! You've won!", message + "\nWould you like to play again?")
        if result == 'yes':
            self.game_active = True
            self.remaining_time = self.timer_time
            self.timer_label.config(text=f"Time remaining: {self.timer_time} seconds")
            self.label.config(text="I choose a number between 1 and 100 and try to guess it.")
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    jeu = Rightprice(root)
    root.mainloop()
