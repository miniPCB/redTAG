import json
import os
import tkinter as tk
from tkinter import messagebox, StringVar, Radiobutton

LABELS_FILE = "/home/pi/redTAG/redLabels.json"

labels_list = []
selected_label_var = None
label_list_frame = None
new_label_entry = None

def init_labels_variables():
    global selected_label_var
    selected_label_var = StringVar()

def load_labels_from_file():
    global labels_list
    if os.path.exists(LABELS_FILE):
        try:
            with open(LABELS_FILE, 'r') as file:
                labels_list = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"Could not load labels from file: {e}")

def save_labels_to_file():
    try:
        with open(LABELS_FILE, 'w') as file:
            json.dump(labels_list, file)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save labels to file: {e}")

def update_label_list():
    for widget in label_list_frame.winfo_children():
        widget.destroy()
    for label in labels_list:
        Radiobutton(label_list_frame, text=label, variable=selected_label_var, value=label).pack(anchor=tk.W)

def add_new_label():
    new_label = new_label_entry.get().strip()
    if new_label:
        labels_list.append(new_label)
        save_labels_to_file()
        update_label_list()
        new_label_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "No Process Message entered.")

def apply_selected_label():
    selected_label = selected_label_var.get()
    if selected_label:
        apply_label(selected_label)
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

def apply_label(label_message):
    from barcode import scan_barcode_and_apply_message
    scan_barcode_and_apply_message(label_message, message_type="Process")

def remove_label():
    selected_label = selected_label_var.get()
    if selected_label:
        labels_list.remove(selected_label)
        save_labels_to_file()
        update_label_list()
        messagebox.showinfo("Success", f"Process Message '{selected_label}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")
