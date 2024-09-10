import tkinter as tk

# Declare variables here, but don't initialize them yet
selected_label_var = None
selected_red_tag_message_var = None

# Function to initialize Tkinter variables
def init_tkinter_vars():
    global selected_label_var, selected_red_tag_message_var
    selected_label_var = tk.StringVar()
    selected_red_tag_message_var = tk.StringVar()

# Other common variables
labels_list = []
red_tag_messages_list = []
LABELS_FILE = "/home/pi/redTAG/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/redTagMessages.json"

# Widgets that will be set later
label_list_frame = None
red_tag_message_list_frame = None
