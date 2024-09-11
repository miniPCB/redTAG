import tkinter as tk
from common import red_tag_messages_list, red_tag_message_list_frame, RED_TAG_FILE
import json

selected_red_tag_message_var = None

def init_red_tag_variables():
    global selected_red_tag_message_var, red_tag_message_list_frame
    selected_red_tag_message_var = tk.StringVar()
    red_tag_message_list_frame = tk.Frame()

def apply_selected_red_tag_message():
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        # Logic to apply the selected red tag message
        pass
    else:
        tk.messagebox.showwarning("Warning", "No red tag message selected.")

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
        tk.Radiobutton(red_tag_message_list_frame, text=message, variable=selected_red_tag_message_var, value=message).pack(anchor=tk.W)

def load_red_tag_messages_from_file():
    global red_tag_messages_list
    try:
        with open(RED_TAG_FILE, 'r') as file:
            red_tag_messages_list = json.load(file)
    except FileNotFoundError:
        red_tag_messages_list = []

def save_red_tag_messages_to_file():
    try:
        with open(RED_TAG_FILE, 'w') as file:
            json.dump(red_tag_messages_list, file)
    except Exception as e:
        tk.messagebox.showerror("Error", f"Could not save red tag messages to file: {e}")
