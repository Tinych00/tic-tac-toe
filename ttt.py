import tkinter as tk
from tkinter import messagebox

# Create the board
board = [" " for _ in range(9)]

# Function to check if the game is over
def is_game_over():
    return (
        check_winner("X") or
        check_winner("O") or
        " " not in board
    )

# Function to check for a win
def check_winner(player):
    return (
        (board[0] == board[1] == board[2] == player) or
        (board[3] == board[4] == board[5] == player) or
        (board[6] == board[7] == board[8] == player) or
        (board[0] == board[3] == board[6] == player) or
        (board[1] == board[4] == board[7] == player) or
        (board[2] == board[5] == board[8] == player) or
        (board[0] == board[4] == board[8] == player) or
        (board[2] == board[4] == board[6] == player)
    )

# Function to handle a move
def make_move(position):
    if board[position] == " " and not is_game_over():
        board[position] = current_player.get()
        buttons[position].config(text=current_player.get())
        if check_winner(current_player.get()):
            winner_label.config(text=f"Player {current_player.get()} wins!")
        elif " " not in board:
            winner_label.config(text="It's a tie!")
            messagebox.showinfo("Game Over", "It's a tie!")
        else:
            current_player.set("O" if current_player.get() == "X" else "X")

# Function to start a new game
def start_new_game():
    for i in range(9):
        buttons[i].config(text=" ")
    for i in range(len(board)):
        board[i] = " "
    winner_label.config(text="")
    current_player.set("X")

# Function to quit the game
def quit_game():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("230x260")  # Set the window size
root.resizable(False, False)  # Disable window resizing

# Create Tkinter StringVar to track the current player
current_player = tk.StringVar()
current_player.set("X")

# Create buttons for the Tic-Tac-Toe grid
buttons = []
for i in range(9):
    button = tk.Button(root, text=" ", width=10, height=3, command=lambda i=i: make_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Create a label for displaying the winner
winner_label = tk.Label(root, text="", font=("Helvetica", 16))
winner_label.grid(row=3, columnspan=3)

# Create a "New Game" button
new_game_button = tk.Button(root, text="New Game", command=start_new_game)
new_game_button.grid(row=4, column=0)

# Create a "Quit" button
quit_button = tk.Button(root, text="Quit", command=quit_game)
quit_button.grid(row=4, column=2)

# Start the Tkinter main loop
root.mainloop()
