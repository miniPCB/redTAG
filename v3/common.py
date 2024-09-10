# common.py

# Constants for file paths
LABELS_FILE = "/home/pi/redTAG/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/redTagMessages.json"

# Global lists to store labels and red tag messages
labels_list = []
red_tag_messages_list = []

# Tkinter Frames that will be initialized in setup.py
label_list_frame = None
red_tag_message_list_frame = None

# Current board information (set when a barcode is scanned)
current_board_name = None
current_board_rev = None
current_board_var = None
current_board_sn = None

# Tkinter elements to display board information
board_name_label = None
board_var_label = None
board_rev_label = None
board_sn_label = None

# Tab control elements (needed for controlling the UI flow between different tabs)
tab_control = None
board_info_tab = None
trends_tab = None
boards_subtab_control = None
messages_subtab = None

# Function to initialize Tkinter StringVars after root window is created
def init_tkinter_vars():
    global selected_label_var, selected_red_tag_message_var
    selected_label_var = tk.StringVar()
    selected_red_tag_message_var = tk.StringVar()
