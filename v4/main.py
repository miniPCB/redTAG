from tkinter import tk
from tkinter import ttk
from setup import setup_tabs

def main():
    root = tk()
    app = setup_tabs(root)
    root.mainloop()

if __name__ == "__main__":
    main()
