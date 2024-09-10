# labels.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from common import label_list_frame, labels_list, selected_label_var, LABELS_FILE, SAVE_DIRECTORY
import json
import os
from utils import push_to_github, parse_pcb_barcode

def apply_selected_label():
    selected_label = selected_label_var.get()
    if selected_label:
        apply_label(selected_label)
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

def apply_label(label_message):
    while True:
        barcode = simpledialog.askstring("Apply Label", f"Apply Process Message: '{label_message}'. Scan a barcode (or type 'x' to finish):")
        
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
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {label_message}"
        
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

def remove_label():
    selected_label = selected_label_var.get()
    if selected_label:
        labels_list.remove(selected_label)
        save_labels_to_file()
        update_label_list()
        messagebox.showinfo("Success", f"Process Message '{selected_label}' removed successfully.")
    else:
        messagebox.showwarning("Warning", "No Process Message selected.")

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

def update_label_list():
    for widget in label_list_frame.winfo_children():
        widget.destroy()
    for label in labels_list:
        tk.Radiobutton(label_list_frame, text=label, variable=selected_label_var, value=label).pack(anchor=tk.W)
