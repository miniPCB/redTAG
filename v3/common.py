# common.py

import tkinter as tk
from tkinter import ttk

# Define global variables to be shared
tab_control = None
board_info_tab = None
trends_tab = None
boards_subtab_control = None
messages_subtab = None

def display_message_content(board_name, board_rev, board_var, board_sn):
    global current_board_name, current_board_rev, current_board_var, current_board_sn
    current_board_name, current_board_rev, current_board_var, current_board_sn = board_name, board_rev, board_var, board_sn
    file_name = f"/home/pi/redTAG/redtags/{board_name}-{board_rev}-{board_var}-{board_sn}.txt"
    
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        message_text.delete(1.0, tk.END)  # Clear the existing content
        message_text.insert(tk.END, content)  # Insert the new content
    else:
        tk.messagebox.showwarning("Warning", f"File '{file_name}' not found.")
        message_text.delete(1.0, tk.END)

    # Update the board info section
    board_name_label.config(text=f"Board Name: {board_name}")
    board_var_label.config(text=f"Board Variant: {board_var}")
    board_rev_label.config(text=f"Board Revision: {board_rev}")
    board_sn_label.config(text=f"Board SN: {board_sn}")

# Define other shared global variables if needed
message_text = None
board_name_label = None
board_var_label = None
board_rev_label = None
board_sn_label = None

current_board_name = current_board_rev = current_board_var = current_board_sn = None
