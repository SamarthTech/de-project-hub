import tkinter as tk
import time

class MobileStyleClock:
    def __init__(self, root):
        self.root = root
        self.root.title('Gradient Style Clock')
        self.canvas = tk.Canvas(root, width=400, height=200)
        self.canvas.pack()

        self.gradient_bg()
        
        self.time_label = tk.Label(root, font=('Helvetica', 40, 'bold'), bg='black', fg='white')
        self.canvas.create_window(200, 80, window=self.time_label)

        self.date_label = tk.Label(root, font=('Helvetica', 16), bg='black', fg='white')
        self.canvas.create_window(200, 130, window=self.date_label)

        self.update_time()

    def gradient_bg(self):
        for i in range(256):
            color = f'#{i:02x}{(255-i):02x}ff'
            self.canvas.create_line(0, i, 400, i, fill=color)

    def update_time(self):
        current_time = time.strftime('%I:%M:%S %p')
        current_date = time.strftime('%A, %d %B %Y')
        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)
        self.root.after(1000, self.update_time)

if __name__ == '__main__':
    root = tk.Tk()
    clock = MobileStyleClock(root)
    root.mainloop()
