import tkinter as tk
from common import (
    root, tab_control, board_info_tab, trends_tab, boards_subtab_control, messages_subtab,
    display_message_content, label_list_frame, red_tag_message_list_frame,
    update_label_list, update_red_tag_messages_list, load_labels_from_file, load_red_tag_messages_from_file
)
from labels import init_label_variables, apply_selected_label, remove_label
from red_tags import init_red_tag_variables, apply_selected_red_tag_message, remove_red_tag_message
from utils import delete_file, pull_from_github

def setup_tabs(root):
    # Set the window icon
    root.iconphoto(False, tk.PhotoImage(file='/home/pi/redTAG/v3/icon.png'))

    # Set the default window size to 1280x720 pixels
    root.geometry("1280x720")

    # Add the main tabs
    tab_control.add(board_info_tab, text='Board Information')
    tab_control.add(trends_tab, text='Trending')
    tab_control.add(boards_subtab_control, text='Boards Subtab Control')
    tab_control.add(messages_subtab, text='Messages')
    tab_control.pack(expand=1, fill="both")

    # Load labels and red tag messages
    load_labels_from_file()
    load_red_tag_messages_from_file()

    # Initialize the variables for labels and red tag messages
    init_label_variables()
    init_red_tag_variables()

    # Update the lists after loading
    update_label_list()
    update_red_tag_messages_list()
