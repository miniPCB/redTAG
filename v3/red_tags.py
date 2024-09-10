import tkinter as tk
from common import selected_red_tag_message_var, red_tag_message_list_frame, red_tag_messages_list, RED_TAG_FILE
import json
from tkinter import messagebox

def update_red_tag_messages_list():
    """
    Update the list of red tag messages displayed with radio buttons.
    """
    for widget in red_tag_message_list_frame.winfo_children():
        widget.destroy()
    for message in red_tag_messages_list:
        tk.Radiobutton(red_tag_message_list_frame, text=message, variable=selected_red_tag_message_var, value=message).pack(anchor=tk.W)

def add_new_red_tag_message(new_red_tag_message_entry):
    """
    Add a new red tag message to the list and update the display.
    """
    new_message = new_red_tag_message_entry.get().strip()
    if new_message:
        red_tag_messages_list.append(new_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        new_red_tag_message_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No Red Tag message entered.")

def remove_red_tag_message():
    """
    Remove the selected red tag message from the list and update the display.
    """
    selected_message = selected_red_tag_message_var.get()
    if selected_message:
        red_tag_messages_list.remove(selected_message)
        save_red_tag_messages_to_file()
        update_red_tag_messages_list()
        messagebox.showinfo("Success", f"Red Tag message '{selected_message}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Red Tag message selected.")

def save_red_tag_messages_to_file():
    """
    Save the current list of red tag messages to the JSON file.
    """
    try:
        with open(RED_TAG_FILE, 'w') as file:
            json.dump(red_tag_messages_list, file)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save Red Tag messages to file: {e}")

def load_red_tag_messages_from_file():
    """
    Load the list of red tag messages from the JSON file.
    """
    global red_tag_messages_list
    if os.path.exists(RED_TAG_FILE):
        try:
            with open(RED_TAG_FILE, 'r') as file:
                red_tag_messages_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load Red Tag messages from file: {e}")
