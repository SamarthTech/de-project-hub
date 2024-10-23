import tkinter as tk
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title('Hangman Game')
        
        self.word_list = ['python', 'java', 'kotlin', 'javascript']
        self.word = random.choice(self.word_list)
        self.guessed_word = ['_'] * len(self.word)
        self.guessed_letters = []
        self.tries = 6

        self.setup_gui()
        self.update_display()

    def setup_gui(self):
        self.canvas = tk.Canvas(self.root, width=400, height=300)
        self.canvas.pack()
        
        self.label_word = tk.Label(self.root, text=' '.join(self.guessed_word), font=('Helvetica', 20))
        self.label_word.pack(pady=20)
        
        self.entry_guess = tk.Entry(self.root, font=('Helvetica', 14))
        self.entry_guess.pack(pady=10)
        
        self.button_guess = tk.Button(self.root, text='Guess', command=self.process_guess)
        self.button_guess.pack(pady=10)
        
        self.label_message = tk.Label(self.root, text='', font=('Helvetica', 14))
        self.label_message.pack(pady=10)
    
    def update_display(self):
        self.label_word.config(text=' '.join(self.guessed_word))
        self.canvas.delete("all")
        self.draw_hangman(self.tries)
    
    def process_guess(self):
        guess = self.entry_guess.get().lower()
        self.entry_guess.delete(0, tk.END)
        if guess in self.guessed_letters:
            self.label_message.config(text='Already guessed that letter.')
        elif guess not in self.word:
            self.guessed_letters.append(guess)
            self.tries -= 1
            self.label_message.config(text=f'Incorrect! {self.tries} tries left.')
        else:
            self.guessed_letters.append(guess)
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.guessed_word[i] = guess
            self.label_message.config(text='Correct!')

        self.update_display()
        if self.tries == 0:
            self.label_message.config(text=f'Sorry, you lost! The word was "{self.word}".')
        if '_' not in self.guessed_word:
            self.label_message.config(text=f'Congrats, you won! The word was "{self.word}".')

    def draw_hangman(self, tries):
        hangman_parts = [
            self.canvas.create_line(150, 200, 250, 200),   # base
            self.canvas.create_line(200, 200, 200, 50),    # pole
            self.canvas.create_line(200, 50, 250, 50),     # top
            self.canvas.create_line(250, 50, 250, 75),     # rope
            self.canvas.create_oval(240, 75, 260, 95),     # head
            self.canvas.create_line(250, 95, 250, 145),    # body
            self.canvas.create_line(250, 105, 230, 125),   # left arm
            self.canvas.create_line(250, 105, 270, 125),   # right arm
            self.canvas.create_line(250, 145, 230, 175),   # left leg
            self.canvas.create_line(250, 145, 270, 175)    # right leg
        ]
        for i in range(6-tries):
            self.canvas.itemconfig(hangman_parts[i], state='hidden')

if __name__ == '__main__':
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
