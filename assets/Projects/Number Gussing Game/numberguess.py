import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Number Guessing Game')
        
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(root, text="Guess a number between 1 and 100", font=('Helvetica', 14))
        self.label.pack(pady=20)
        
        self.entry = tk.Entry(root, font=('Helvetica', 14))
        self.entry.pack(pady=10)
        
        self.button = tk.Button(root, text='Guess', font=('Helvetica', 14), command=self.check_guess)
        self.button.pack(pady=20)
        
        self.result_label = tk.Label(root, font=('Helvetica', 14))
        self.result_label.pack(pady=20)
    
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            if guess < 1 or guess > 100:
                self.result_label.config(text="Please guess a number within the range 1 to 100.")
            elif guess < self.number_to_guess:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.number_to_guess:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Congratulations! You guessed the number in {self.attempts} attempts.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
