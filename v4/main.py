from tkinter import Tk
from setup import SetupWindow

def main():
    root = Tk()
    app = SetupWindow(root)
    root.mainloop()

if __name__ == "__main__":
    main()
