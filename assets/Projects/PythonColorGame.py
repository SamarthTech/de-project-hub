import tkinter
import random
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0
timeleft = 30

def startGame(event):
    global timeleft
    if timeleft == 30:
        countdown()
    e.config(state=tkinter.NORMAL)
    e.focus_set()
    nextColour()

def nextColour():
    global score, timeleft
    if timeleft > 0:
        if e.get().lower() == colours[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

root = tkinter.Tk()
root.title("Python Color Game")
root.geometry("380x300+{}+{}".format(int(root.winfo_screenwidth()/2 - 190), int(root.winfo_screenheight()/2 - 150)))
root.resizable(False, False)
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!", font=('Helvetica', 12), pady=10)
instructions.pack()
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12), pady=10)
scoreLabel.pack()
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12), pady=10)
timeLabel.pack()
label = tkinter.Label(root, font=('Helvetica', 60), pady=10)
label.pack()
e = tkinter.Entry(root, font=('Helvetica', 10), bd=5)
e.pack(pady=10)
e.config(state=tkinter.DISABLED)
root.bind('<Return>', startGame)
root.mainloop()