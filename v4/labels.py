import json
import os
from tkinter import messagebox, Radiobutton
from common import label_list_frame, labels_list, LABELS_FILE, selected_label_var

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
        Radiobutton(label_list_frame, text=label, variable=selected_label_var, value=label).pack(anchor=tk.W)

# Define other label-related functions here as needed
