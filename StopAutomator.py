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

# Set window size and position it in the center of the screen
window_width = 350
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordinate, y_coordinate))

# Apply a dark mode theme
style = ttk.Style()
style.theme_use('clam')

# Configure button style with dark mode
style.configure('Dark.TButton', background='#2c3e50', foreground='white', font=('Arial', 12), borderwidth=0, bordercolor="white", relief='flat')
style.map('Dark.TButton', background=[('active', '#34495e')])

# Create a frame to hold the buttons
frame = ttk.Frame(root)
frame.pack(expand=True, padx=20, pady=20)

# Create the "Create Game" button with dark mode styling
create_button = ttk.Button(frame, text="Create Game", command=create_game_wrapper, style='Dark.TButton', width=15)
create_button.grid(row=0, column=0, padx=10, pady=10)

# Create the "Hack Game" button with dark mode styling
hack_button = ttk.Button(frame, text="Hack Game", command=hack_game_wrapper, style='Dark.TButton', width=15)
hack_button.grid(row=0, column=1, padx=10, pady=10)

# Add some padding
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Add a label for displaying a link
link_var = tk.StringVar()
link_label = ttk.Label(root, textvariable=link_var)
link_label.pack(pady=5)


# Start the Tkinter event loop
root.mainloop()



# Quit the WebDriver when the GUI is closed
driver.quit()
