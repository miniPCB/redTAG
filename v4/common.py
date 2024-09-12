import os
import tkinter as tk
from tkinter import ttk
from setup import *
from utils import *

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

GITREPO = "git@github.com:miniPCB/redTAG.git"
SAVE_DIRECTORY = "/home/pi/redTAG/redtags"
LABELS_FILE = "/home/pi/redTAG/v4/redLabels.json"
RED_TAG_FILE = "/home/pi/redTAG/v4/redTagMessages.json"
ICON_FILEPATHNAME = '/home/pi/redTAG/v4/icon.png'

def display_message_content(board_name, board_rev, board_var, board_sn):
    global current_board_name, current_board_rev, current_board_var, current_board_sn
    current_board_name, current_board_rev, current_board_var, current_board_sn = board_name, board_rev, board_var, board_sn
    file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            content = file.read()
        message_text.delete(1.0, tk.END)  # Clear the existing content
        message_text.insert(tk.END, content)  # Insert the new content
    else:
        messagebox.showwarning("Warning", f"File '{file_name}' not found.")
        message_text.delete(1.0, tk.END)

    # Update the board info section
    board_name_label.config(text=f"Board Name: {board_name}")
    board_var_label.config(text=f"Board Variant: {board_var}")
    board_rev_label.config(text=f"Board Revision: {board_rev}")
    board_sn_label.config(text=f"Board SN: {board_sn}")

def add_new_message():
    new_message = new_message_entry.get().strip()
    if new_message and current_board_name:
        file_name = os.path.join(SAVE_DIRECTORY, f"{current_board_name}-{current_board_rev}-{current_board_var}-{current_board_sn}.txt")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        full_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {new_message}"

        try:
            with open(file_name, 'a+') as file:
                file.write(f"{full_message}\n")
            push_to_github(file_name, suppress_message=True)  # Suppress the success message here
            display_message_content(current_board_name, current_board_rev, current_board_var, current_board_sn)
            new_message_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Message added successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while writing to the file '{file_name}': {e}")
    else:
        messagebox.showwarning("Warning", "No message entered or no barcode scanned.")

def delete_file():
    barcode = simpledialog.askstring("Delete File", "Scan a barcode to delete the associated file:")
    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        if os.path.exists(file_name):
            os.remove(file_name)
            messagebox.showinfo("Success", f"File '{file_name}' deleted.")
            try:
                subprocess.run(['git', 'rm', file_name], check=True)
                subprocess.run(['git', 'commit', '-m', f"Delete {file_name}"], check=True)
                subprocess.run(['git', 'push'], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"An error occurred while pushing deletion to GitHub: {e}")
        else:
            messagebox.showwarning("Warning", f"File '{file_name}' not found.")
    else:
        messagebox.showwarning("Warning", "No barcode provided.")