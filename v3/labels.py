import tkinter as tk
from common import selected_label_var, label_list_frame, labels_list, LABELS_FILE
import json
from tkinter import messagebox

def update_label_list():
    """
    Update the list of labels displayed with radio buttons.
    """
    for widget in label_list_frame.winfo_children():
        widget.destroy()
    for label in labels_list:
        tk.Radiobutton(label_list_frame, text=label, variable=selected_label_var, value=label).pack(anchor=tk.W)

def add_new_label(new_label_entry):
    """
    Add a new label to the list and update the display.
    """
    new_label = new_label_entry.get().strip()
    if new_label:
        labels_list.append(new_label)
        save_labels_to_file()
        update_label_list()
        new_label_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No Process Message entered.")

def remove_label():
    """
    Remove the selected label from the list and update the display.
    """
    selected_label = selected_label_var.get()
    if selected_label:
        labels_list.remove(selected_label)
        save_labels_to_file()
        update_label_list()
        messagebox.showinfo("Success", f"Process Message '{selected_label}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

def save_labels_to_file():
    """
    Save the current list of labels to the JSON file.
    """
    try:
        with open(LABELS_FILE, 'w') as file:
            json.dump(labels_list, file)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save labels to file: {e}")

def load_labels_from_file():
    """
    Load the list of labels from the JSON file.
    """
    global labels_list
    if os.path.exists(LABELS_FILE):
        try:
            with open(LABELS_FILE, 'r') as file:
                labels_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load labels from file: {e}")
