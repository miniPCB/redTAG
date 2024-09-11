import tkinter as tk
from setup import setup_tabs
from common import root

# Set the icon using the full path to the icon file
root.iconphoto(False, tk.PhotoImage(file='/home/pi/redTAG/v3/icon.png'))

# Set up the tabs and the rest of the GUI
setup_tabs(root)

# Start the main event loop
root.mainloop()
