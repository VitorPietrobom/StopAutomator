import tkinter as tk
from tkinter import ttk

import GameCreator

def create_game():
    GameCreator.create()
    pass

def hack_game():
    # Add your code for hacking a game here
    pass

# Create the main application window
root = tk.Tk()
root.title("Game GUI")

# Set the window size and position it in the center of the screen
window_width = 300
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Apply a simple style to the buttons
style = ttk.Style()
style.configure('TButton', foreground='black', font=('Arial', 12))

# Create a frame to hold the buttons
frame = ttk.Frame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Create the "Create Game" button
create_button = ttk.Button(frame, text="Create Game", command=create_game)
create_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill='both')

# Create the "Hack Game" button
hack_button = ttk.Button(frame, text="Hack Game", command=hack_game)
hack_button.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill='both')

# Start the Tkinter event loop
root.mainloop()
