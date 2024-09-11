import os
import tkinter as tk
from common import red_tag_messages_list, red_tag_message_list_frame, RED_TAG_FILE
import json
from utils import *

selected_red_tag_message_var = None

def init_red_tag_variables():
    global selected_red_tag_message_var, red_tag_message_list_frame
    selected_red_tag_message_var = tk.StringVar()
    red_tag_message_list_frame = tk.Frame()

def apply_selected_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        apply_red_tag_message(selected_message)
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")

def remove_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message in red_tag_messages_list:
        red_tag_messages_list.remove(selected_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()

def update_red_tag_messages_list():
    for widget in red_tag_message_list_frame.winfo_children():
        widget.destroy()
    for message in red_tag_messages_list:
        Radiobutton(red_tag_message_list_frame, text=message, variable=selected_red_tag_message_var, value=message).pack(anchor=tk.W)

def load_red_tag_messages_from_file():
    global red_tag_messages_list
    if os.path.exists(RED_TAG_FILE):
        try:
            with open(RED_TAG_FILE, 'r') as file:
                red_tag_messages_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load Red Tag messages from file: {e}")

def save_red_tag_messages_to_file():
    try:
        with open(RED_TAG_FILE, 'w') as file:
            json.dump(red_tag_messages_list, file)
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not save red tag messages to file: {e}")

def add_new_red_tag_message():
    new_message = new_red_tag_message_entry.get().strip()
    if new_message:
        red_tag_messages_list.append(new_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        new_red_tag_message_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No Red Tag message entered.")

def remove_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        red_tag_messages_list.remove(selected_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        messagebox.showinfo("Success", f"Red Tag message '{selected_message}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")

def save_red_tag_messages_to_file():
    try:
        with open(RED_TAG_FILE, 'w') as file:
            json.dump(red_tag_messages_list, file)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save Red Tag messages to file: {e}")

def apply_red_tag_message(red_tag_message):
    while True:
        barcode = simpledialog.askstring("Apply Red Tag Message", f"Apply Red Tag message: '{red_tag_message}'. Scan a barcode (or type 'x' to finish):")
        
        if barcode is None or barcode.lower() == 'x':
            break
        
        if not barcode:
            messagebox.showwarning("Warning", "No barcode scanned. Please scan a valid barcode.")
            continue
        
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {red_tag_message}"
        
        try:
            with open(file_name, 'a+') as file:
                if os.path.getsize(file_name) == 0:
                    file.write(f"Board Name: {board_name}\n")
                    file.write(f"Board Revision: {board_rev}\n")
                    file.write(f"Board Variant: {board_var}\n")
                    file.write(f"Board Serial Number: {board_sn}\n")
                file.write(f"{issue_message}\n")
            push_to_github(file_name, suppress_message=True)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while writing to the file '{file_name}': {e}")
