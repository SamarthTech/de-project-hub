import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Scientific Calculator')
        self.root.geometry('480x600')
        self.root.resizable(False, False)
        self.result = ''

        self.display = tk.Entry(root, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.display.grid(row=0, column=0, columnspan=5)
        
        self.create_buttons()
    
    def create_buttons(self):
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('cos', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('tan', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3), ('log', 4, 4),
            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3), ('exp', 5, 4)
        ]
        
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(self.root, text=text, padx=16, pady=16, bd=8, fg='black', bg='lightblue', font=('Arial', 18, 'bold'), command=self.calculate)
            else:
                btn = tk.Button(self.root, text=text, padx=16, pady=16, bd=8, fg='black', bg='white', font=('Arial', 18, 'bold'), command=lambda val=text: self.click(val))
            btn.grid(row=row, column=col)

    def click(self, value):
        if value == 'C':
            self.result = ''
        else:
            self.result += str(value)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.result)
    
    def calculate(self):
        try:
            self.result = str(eval(self.result))
        except:
            self.result = 'Error'
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.result)

if __name__ == '__main__':
    root = tk.Tk()
    calc = ScientificCalculator(root)
    root.mainloop()
