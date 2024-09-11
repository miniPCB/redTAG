import tkinter as tk
from tkinter import ttk

# Initialize the main root window
root = tk.Tk()

# Declare shared variables
tab_control = ttk.Notebook(root)
board_info_tab = ttk.Frame(tab_control)  # Frame for Board Information tab
trends_tab = ttk.Frame(tab_control)  # Frame for Trending tab
boards_subtab_control = ttk.Notebook(board_info_tab)  # Notebook for sub-tabs within Board Information
messages_subtab = ttk.Frame(boards_subtab_control)  # Frame for Messages sub-tab

labels_list = []
red_tag_messages_list = []

label_list_frame = None
red_tag_message_list_frame = None

LABELS_FILE = "/home/pi/redTAG/v4/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/v4/redTagMessages.json"
ICON_FILEPATHNAME = '/home/pi/redTAG/v4/icon.png'

def display_message_content(board_name, board_rev, board_var, board_sn):
    # Your code for displaying message content based on the parsed barcode
    pass
