from tkinter import Tk
from tkinter import ttk
from setup import setup_tabs

def main():
    root = Tk()
    app = setup_tabs(root)
    root.mainloop()

if __name__ == "__main__":
    main()
