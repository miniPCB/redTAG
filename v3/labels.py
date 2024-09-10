# labels.py

import tkinter as tk
from tkinter import messagebox
import json
from common import label_list_frame, labels_list, LABELS_FILE

selected_label_var = tk.StringVar()

def apply_selected_label():
    selected_label = selected_label_var.get()
    if selected_label:
        apply_label(selected_label)
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

def remove_label():
    selected_label = selected_label_var.get()
    if selected_label:
        labels_list.remove(selected_label)
        save_labels_to_file()
        update_label_list()
        messagebox.showinfo("Success", f"Process Message '{selected_label}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

def update_label_list():
    if label_list_frame is None:
        raise ValueError("label_list_frame is not initialized.")
        
    for widget in label_list_frame.winfo_children():
        widget.destroy()
    for label in labels_list:
        tk.Radiobutton(label_list_frame, text=label, variable=selected_label_var, value=label).pack(anchor=tk.W)

def save_labels_to_file():
    try:
        with open(LABELS_FILE, 'w') as file:
            json.dump(labels_list, file)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save labels to file: {e}")

def load_labels_from_file():
    global labels_list
    if os.path.exists(LABELS_FILE):
        try:
            with open(LABELS_FILE, 'r') as file:
                labels_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load labels from file: {e}")
