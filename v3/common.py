import tkinter as tk

# Common global variables
tab_control = None
board_info_tab = None
trends_tab = None
boards_subtab_control = None
messages_subtab = None
message_text = None
new_message_entry = None
selected_label_var = tk.StringVar()
selected_red_tag_message_var = tk.StringVar()
label_list_frame = None
red_tag_message_list_frame = None
labels_list = []
red_tag_messages_list = []
LABELS_FILE = "/home/pi/redTAG/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/redTagMessages.json"
