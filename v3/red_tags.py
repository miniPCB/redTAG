import tkinter as tk
from tkinter import messagebox, simpledialog
from common import (
    red_tag_message_list_frame,
    red_tag_messages_list,
    selected_red_tag_message_var,
    RED_TAG_FILE,
    SAVE_DIRECTORY
)
import json
import os
from utils import push_to_github, parse_pcb_barcode

def apply_selected_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        apply_red_tag_message(selected_message)
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")

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
        user_name = os.getlogin()
        computer_name = os.uname().nodename
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

def load_red_tag_messages_from_file():
    global red_tag_messages_list
    if os.path.exists(RED_TAG_FILE):
        try:
            with open(RED_TAG_FILE, 'r') as file:
                red_tag_messages_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load Red Tag messages from file: {e}")

def update_red_tag_messages_list():
    for widget in red_tag_message_list_frame.winfo_children():
        widget.destroy()
    for message in red_tag_messages_list:
        tk.Radiobutton(red_tag_message_list_frame, text=message, variable=selected_red_tag_message_var, value=message).pack(anchor=tk.W)
