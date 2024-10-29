import tkinter as tk
from tkinter import messagebox

# Find the Best Move
def best_move(board):
    best = -1000
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "_":
                board[i][j] = "x"
                val = minimax(board, 0, False)
                board[i][j] = "_"
                if val > best:
                    move = (i, j)
                    best = val
    return move

# Check the Game Board
def check(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != "_":
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != "_":
            return board[0][col]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != "_":
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != "_":
        return board[0][2]
    for row in board:
        if "_" in row:
            return None
    return "draw"

# Minimax Algorithm
def minimax(board, depth, is_maximizing):
    score = evaluate(board)
    if score == 10 or score == -10:
        return score
    if check(board) == "draw":
        return 0
    # Maximizing Player
    if is_maximizing:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "x"
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = "_"
        return best
    # Minimizing Player
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == "_":
                    board[i][j] = "o"
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = "_"
        return best

# Evaluate the Game Board
def evaluate(board):
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
            if board[row][0] == "o":
                return -10
            elif board[row][0] == "x":
                return 10
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
            if board[0][col] == "o":
                return -10
            elif board[0][col] == "x":
                return 10
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        if board[1][1] == "o":
            return -10
        elif board[1][1] == "x":
            return 10
    return 0

# Handle the Click Event
def on_click(row, col):
    if board[row][col] == "_" and turn[0] == 0:
        board[row][col] = "o"
        buttons[row][col].config(text="O", state="disabled", disabledforeground="blue")
        turn[0] = 1 - turn[0]
        check_winner()
        if turn[0] == 1:
            move = best_move(board)
            board[move[0]][move[1]] = "x"
            buttons[move[0]][move[1]].config(text="X", state="disabled", disabledforeground="red")
            turn[0] = 1 - turn[0]
            check_winner()

# Check the Winner of the Game
def check_winner():
    result = check(board)
    if result:
        if result == "x":
            messagebox.showinfo("Result", "You lose!")
        elif result == "o":
            messagebox.showinfo("Result", "You win!")
        else:
            messagebox.showinfo("Result", "It's a draw!")
        reset_board()

# Reset the Game Board
def reset_board():
    global board
    board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal")

# Center the window on the screen
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

# Initialize the Game Board
board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
turn = [0]

# Create the GUI
root = tk.Tk()
root.title("Tic Tac Toe")
title_label = tk.Label(root, text="Tic Tac Toe", font=('normal', 20, 'bold'))
title_label.grid(row=0, column=0, columnspan=3, pady=10)
buttons = [[None for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i+1, column=j, padx=5, pady=5)
center_window(root)

# Start the GUI event loop
root.mainloop()