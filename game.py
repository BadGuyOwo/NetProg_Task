from tkinter import *
from tkinter import messagebox

# Function to reset the game
def reset():
    for button in buttons:
        button["text"] = " "

# Function to handle button clicks
def button_click(button):
    global turn
    if button["text"] == " ":
        if turn == 1:
            button["text"] = "X"
            turn = 2
        elif turn == 2:
            button["text"] = "O"
            turn = 1
        check_for_winner()

# Function to check for a winner
def check_for_winner():
    # List of winning combinations
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combination in winning_combinations:
        if buttons[combination[0]]["text"] == buttons[combination[1]]["text"] == buttons[combination[2]]["text"] != " ":
            winner = buttons[combination[0]]["text"]
            messagebox.showinfo("Winner!", f"Player {winner} wins!")
            return

    # Check for tie
    if all(button["text"] != " " for button in buttons):
        messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")

# Create the main window
window = Tk()
window.title("Welcome to The Gaming world TIC-Tac-Toe ")
window.geometry("400x300")

# Create buttons for the game
buttons = []
for i in range(3):
    for j in range(3):
        button = Button(window, text=" ", bg="white", fg="black", width=3, height=1, font=('Helvetica', '20'))
        button.grid(row=i+1, column=j, padx=5, pady=5)
        button.config(command=lambda b=button: button_click(b))
        buttons.append(button)

# Add a reset button
reset_btn = Button(window, text="Reset", bg="white", fg="black", width=5, height=1, font=('Helvetica', '12'), command=reset)
reset_btn.grid(row=4, column=1, columnspan=2)

# Variable to keep track of player turn
turn = 1

# Start the main loop
window.mainloop()
