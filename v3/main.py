import tkinter as tk
from setup import setup_tabs
from labels import load_labels_from_file, update_label_list
from red_tags import load_red_tag_messages_from_file, update_red_tag_messages_list
from common import init_tkinter_vars

if __name__ == "__main__":
    root = tk.Tk()
    root.title("redTAG")

    # Load labels and red tag messages
    load_labels_from_file()
    load_red_tag_messages_from_file()

    # Initialize Tkinter variables
    init_tkinter_vars()

    # Setup the tabs and UI
    setup_tabs(root)
    
    # Update the label and red tag message lists
    update_label_list()
    update_red_tag_messages_list()

    root.mainloop()
