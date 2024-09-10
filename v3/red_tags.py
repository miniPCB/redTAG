import json
import os
import tkinter as tk
from tkinter import messagebox, StringVar, Radiobutton

RED_TAG_FILE = "/home/pi/redTAG/redTagMessages.json"

red_tag_messages_list = []
selected_red_tag_message_var = None
red_tag_message_list_frame = None
new_red_tag_message_entry = None

def init_red_tag_variables():
    global selected_red_tag_message_var
    selected_red_tag_message_var = StringVar()

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
        messagebox.showerror("Error", f"Could not save Red Tag messages to file: {e}")

def update_red_tag_messages_list():
    for widget in red_tag_message_list_frame.winfo_children():
        widget.destroy()
    for message in red_tag_messages_list:
        Radiobutton(red_tag_message_list_frame, text=message, variable=selected_red_tag_message_var, value=message).pack(anchor=tk.W)

def add_new_red_tag_message():
    new_message = new_red_tag_message_entry.get().strip()
    if new_message:
        red_tag_messages_list.append(new_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        new_red_tag_message_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No Red Tag message entered.")

def apply_selected_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        apply_red_tag_message(selected_message)
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")

def apply_red_tag_message(red_tag_message):
    from barcode import scan_barcode_and_apply_message
    scan_barcode_and_apply_message(red_tag_message, message_type="Red Tag")

def remove_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        red_tag_messages_list.remove(selected_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        messagebox.showinfo("Success", f"Red Tag message '{selected_message}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")
