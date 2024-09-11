# common.py

import tkinter as tk
import os
from tkinter import messagebox

# Global variables
tab_control = None
board_info_tab = None
trends_tab = None
boards_subtab_control = None
messages_subtab = None
message_text = None
new_message_entry = None
selected_label_var = None
selected_red_tag_message_var = None
label_list_frame = None
red_tag_message_list_frame = None
labels_list = []
red_tag_messages_list = []
LABELS_FILE = "/home/pi/redTAG/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/redTagMessages.json"
SAVE_DIRECTORY = "/home/pi/redTAG/redtags"
ICON_FILEPATHNAME = '/home/pi/redTAG/v3/icon.png'

# Function to initialize Tkinter variables after root is created
def initialize_variables():
    global selected_label_var, selected_red_tag_message_var
    selected_label_var = tk.StringVar()
    selected_red_tag_message_var = tk.StringVar()

def display_message_content(board_name, board_rev, board_var, board_sn):
    global message_text
    file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        message_text.delete(1.0, tk.END)  # Clear the existing content
        message_text.insert(tk.END, content)  # Insert the new content
    else:
        messagebox.showwarning("Warning", f"File '{file_name}' not found.")
        message_text.delete(1.0, tk.END)

    # Update the board info section if needed
    # board_name_label.config(text=f"Board Name: {board_name}")
    # board_var_label.config(text=f"Board Variant: {board_var}")
    # board_rev_label.config(text=f"Board Revision: {board_rev}")
    # board_sn_label.config(text=f"Board SN: {board_sn}")
