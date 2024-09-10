# main.py

import tkinter as tk
from setup import setup_tabs
from common import initialize_variables

if __name__ == "__main__":
    root = tk.Tk()
    root.title("redTAG")
    
    initialize_variables()  # Initialize Tkinter variables after root is created

    setup_tabs(root)
    root.mainloop()
