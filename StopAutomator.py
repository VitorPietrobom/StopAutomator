# gui.py
import tkinter as tk
from tkinter import ttk
from selenium import webdriver
from GameCreator import create_game
from GameHacker import hack_game

def create_game_wrapper():
    global driver, link
    link = create_game(driver)
    link_var.set(("Link: stopots.com/" + link) if link else "No game created")


def hack_game_wrapper():
    global driver, link
    if link is None:
        print("Create a game first")
        return
    else:
        hack_game(driver)
    pass

link = None

# Create the WebDriver instance
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Create the main application window
root = tk.Tk()
root.title("Stop Automator v2.0")

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
style.configure('TButton', foreground='black', font=('Arial', 12), borderwidth=0, bordercolor="white")

# Create a frame to hold the buttons
frame = ttk.Frame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Create the "Create Game" button
create_button = ttk.Button(frame, text="Create Game", command=create_game_wrapper, style='TButton', width=15)
create_button.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill='both')

# Create the "Hack Game" button
hack_button = ttk.Button(frame, text="Hack Game", command=hack_game_wrapper, style='TButton', width=15)
hack_button.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill='both')

# Create a label to display the link
link_var = tk.StringVar()
link_label = ttk.Label(root, textvariable=link_var)
link_label.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()


# Quit the WebDriver when the GUI is closed
driver.quit()
