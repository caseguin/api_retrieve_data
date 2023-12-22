import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create a function to handle button clicks
def handle_click(row, col):
    print(f"Button clicked at row {row}, column {col}")

# Create buttons for the Tic-Tac-Toe grid
buttons = [[None, None, None],
           [None, None, None],
           [None, None, None]]

for row in range(3):
    for col in range(3):
        button = tk.Button(window, text="", width=10, height=3,
                           command=lambda row=row, col=col: handle_click(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

# Start the Tkinter main loop
window.mainloop()
