import tkinter as tk
from setup import setup_tabs
from labels import load_labels_from_file, update_label_list
from red_tags import load_red_tag_messages_from_file, update_red_tag_messages_list

if __name__ == "__main__":
    root = tk.Tk()
    root.title("redTAG")

    # Load labels and red tag messages
    load_labels_from_file()
    load_red_tag_messages_from_file()

    # Setup the tabs and UI
    setup_tabs(root)
    
    # Update the label and red tag message lists
    update_label_list()
    update_red_tag_messages_list()

    root.mainloop()
