from setup import setup_tabs, initialize_application
from labels import *
from red_tags import *

if __name__ == "__main__":
    current_board_name = current_board_rev = current_board_var = current_board_sn = None
    root = tk.Tk()
    load_labels_from_file()  # Load labels from JSON file on startup
    load_red_tag_messages_from_file()  # Load Red Tag messages from JSON file on startup
    setup_tabs(root)
    root.mainloop()