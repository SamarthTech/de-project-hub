import tkinter as tk
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title('Rock Paper Scissors')
        
        self.choices = ['rock', 'paper', 'scissors']
        self.user_choice = None
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text='Choose:', font=('Helvetica', 20)).pack(pady=20)
        
        self.result_label = tk.Label(self.root, text='', font=('Helvetica', 15))
        self.result_label.pack(pady=10)
        
        for choice in self.choices:
            button = tk.Button(self.root, text=choice.capitalize(), font=('Helvetica', 15), command=lambda c=choice: self.play(c))
            button.pack(pady=5)
    
    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}.\n{result}")
    
    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            return "You win!"
        else:
            return "Computer wins!"
    
if __name__ == '__main__':
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
