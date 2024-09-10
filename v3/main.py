import tkinter as tk
from setup import setup_tabs
from common import init_tkinter_vars

if __name__ == "__main__":
    root = tk.Tk()
    root.title("redTAG")

    # Initialize Tkinter variables
    init_tkinter_vars()

    setup_tabs(root)
    root.mainloop()
