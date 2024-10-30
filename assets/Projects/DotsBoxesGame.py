from tkinter import *
import numpy as np

board_size = 600
num_dots = 3
dot_color = '#7BC043'
p1_color = '#0492CF'
p1_light = '#67B0CF'
p2_color = '#EE4035'
p2_light = '#EE7E77'
green_color = '#7BC043'
dot_width = 0.25 * board_size / num_dots
edge_width = 0.1 * board_size / num_dots
dist_between_dots = board_size / (num_dots)

window = Tk()
window.title('Dots Boxes Game')
window.geometry(f"{board_size}x{board_size}+{int(window.winfo_screenwidth()/2 - board_size/2)}+{int(window.winfo_screenheight()/2 - (board_size)/2)}")
window.resizable(False, False)
canvas = Canvas(window, width=board_size, height=board_size)
canvas.pack()

p1_turn = False
reset_board = False
turn_text_handle = []
marked_boxes = []

board_status = np.zeros(shape=(num_dots - 1, num_dots - 1))
row_status = np.zeros(shape=(num_dots, num_dots - 1))
col_status = np.zeros(shape=(num_dots - 1, num_dots))

p1_score = 0
p2_score = 0

def play_again():
    global p1_turn, reset_board, marked_boxes, p1_score, p2_score
    refresh_board()
    global board_status, row_status, col_status
    board_status = np.zeros(shape=(num_dots - 1, num_dots - 1))
    row_status = np.zeros(shape=(num_dots, num_dots - 1))
    col_status = np.zeros(shape=(num_dots - 1, num_dots))
    p1_turn = False
    reset_board = False
    marked_boxes = []
    p1_score = 0
    p2_score = 0
    display_turn_text()

def is_occupied(logical_pos, type):
    r, c = logical_pos
    if type == 'row' and row_status[c][r] == 0:
        return False
    if type == 'col' and col_status[c][r] == 0:
        return False
    return True

def grid_to_logical(grid_pos):
    grid_pos = np.array(grid_pos)
    pos = (grid_pos - dist_between_dots / 4) // (dist_between_dots / 2)
    type = False
    logical_pos = []
    if pos[1] % 2 == 0 and (pos[0] - 1) % 2 == 0:
        r = int((pos[0] - 1) // 2)
        c = int(pos[1] // 2)
        logical_pos = [r, c]
        type = 'row'
    elif pos[0] % 2 == 0 and (pos[1] - 1) % 2 == 0:
        c = int((pos[1] - 1) // 2)
        r = int(pos[0] // 2)
        logical_pos = [r, c]
        type = 'col'
    return logical_pos, type

def mark_box():
    global marked_boxes, p1_score, p2_score
    for r in range(num_dots - 1):
        for c in range(num_dots - 1):
            if row_status[r][c] == 1 and row_status[r+1][c] == 1 and col_status[r][c] == 1 and col_status[r][c+1] == 1:
                if [r, c] not in marked_boxes:
                    marked_boxes.append([r, c])
                    if p1_turn:
                        p1_score += 1
                        color = p1_light
                    else:
                        p2_score += 1
                        color = p2_light
                    shade_box([r, c], color)

def update_board(type, logical_pos):
    r, c = logical_pos
    if type == 'row':
        row_status[c][r] = 1
    elif type == 'col':
        col_status[c][r] = 1

def is_game_over():
    return (row_status == 1).all() and (col_status == 1).all()

def make_edge(type, logical_pos):
    if type == 'row':
        start_x = dist_between_dots / 2 + logical_pos[0] * dist_between_dots
        end_x = start_x + dist_between_dots
        start_y = dist_between_dots / 2 + logical_pos[1] * dist_between_dots
        end_y = start_y
    elif type == 'col':
        start_y = dist_between_dots / 2 + logical_pos[1] * dist_between_dots
        end_y = start_y + dist_between_dots
        start_x = dist_between_dots / 2 + logical_pos[0] * dist_between_dots
        end_x = start_x
    color = p1_color if p1_turn else p2_color
    canvas.create_line(start_x, start_y, end_x, end_y, fill=color, width=edge_width)

def display_game_over():
    global p1_score, p2_score
    if p1_score > p2_score:
        text = 'Winner: Player 1'
        color = p1_color
    elif p2_score > p1_score:
        text = 'Winner: Player 2'
        color = p2_color
    else:
        text = 'It\'s a tie'
        color = 'gray'
    canvas.delete("all")
    canvas.create_text(board_size / 2, board_size / 3, font="cmr 45 bold", fill=color, text=text)
    score_text = f'Scores\nPlayer 1: {p1_score}\nPlayer 2: {p2_score}'
    canvas.create_text(board_size / 2, 5 * board_size / 8, font="cmr 30 bold", fill=green_color, text=score_text)
    global reset_board
    reset_board = True
    canvas.create_text(board_size / 2, 15 * board_size / 16, font="cmr 20 bold", fill="gray", text='Click to play again')

def refresh_board():
    for i in range(num_dots):
        x = i * dist_between_dots + dist_between_dots / 2
        canvas.create_line(x, dist_between_dots / 2, x, board_size - dist_between_dots / 2, fill='gray', dash=(2, 2))
        canvas.create_line(dist_between_dots / 2, x, board_size - dist_between_dots / 2, x, fill='gray', dash=(2, 2))
    for i in range(num_dots):
        for j in range(num_dots):
            start_x = i * dist_between_dots + dist_between_dots / 2
            end_x = j * dist_between_dots + dist_between_dots / 2
            canvas.create_oval(start_x - dot_width / 2, end_x - dot_width / 2, start_x + dot_width / 2, end_x + dot_width / 2, fill=dot_color, outline=dot_color)

def display_turn_text():
    text = 'Current Turn: Player ' + ('1' if p1_turn else '2')
    color = p1_color if p1_turn else p2_color
    global turn_text_handle
    canvas.delete(turn_text_handle)
    turn_text_handle = canvas.create_text(board_size / 2, dist_between_dots / 8, font="cmr 20 bold", text=text, fill=color)

def shade_box(box, color):
    start_x = dist_between_dots / 2 + box[1] * dist_between_dots + edge_width / 2
    start_y = dist_between_dots / 2 + box[0] * dist_between_dots + edge_width / 2
    end_x = start_x + dist_between_dots - edge_width
    end_y = start_y + dist_between_dots - edge_width
    canvas.create_rectangle(start_x, start_y, end_x, end_y, fill=color, outline='')

def click(event):
    global p1_turn, reset_board
    if not reset_board:
        grid_pos = [event.x, event.y]
        logical_pos, valid_input = grid_to_logical(grid_pos)
        if valid_input and not is_occupied(logical_pos, valid_input):
            update_board(valid_input, logical_pos)
            make_edge(valid_input, logical_pos)
            prev_boxes = len(marked_boxes)
            mark_box()
            refresh_board()
            new_boxes = len(marked_boxes)
            if new_boxes == prev_boxes:
                p1_turn = not p1_turn
            if is_game_over():
                display_game_over()
            else:
                display_turn_text()
    else:
        canvas.delete("all")
        play_again()
        reset_board = False

play_again()
window.bind('<Button-1>', click)
window.mainloop()