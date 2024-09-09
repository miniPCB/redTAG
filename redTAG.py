import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import re
import os
import datetime
import getpass
import socket
import subprocess

# Constants
GITREPO = "git@github.com:miniPCB/redTAG.git"
SAVE_DIRECTORY = "/home/pi/redTAG/redtags"
VERSION = "v010"

def parse_pcb_barcode(input_string):
    board_name_pattern = r"^(.*?)-"
    board_rev_pattern = r"^[^-]*-(.*?)-"
    board_var_pattern = r"(?:[^-]*-){2}([^-]*)-"
    board_sn_pattern = r"(?:[^-]*-){3}([^-\s]*)"

    board_name = re.match(board_name_pattern, input_string).group(1).lower() if re.match(board_name_pattern, input_string) else "unknown"
    board_rev = re.match(board_rev_pattern, input_string).group(1) if re.match(board_rev_pattern, input_string) else "unknown"
    board_var = re.search(board_var_pattern, input_string).group(1) if re.search(board_var_pattern, input_string) else "unknown"
    board_sn = re.search(board_sn_pattern, input_string).group(1) if re.search(board_sn_pattern, input_string) else "unknown"

    return board_name, board_rev, board_var, board_sn

def read_existing_issues(file_name):
    issues = []
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                if line.startswith("Message:"):
                    issues.append(line.strip())
    return issues

def push_to_github(file_name):
    try:
        subprocess.run(['git', 'add', file_name], check=True)
        commit_message = f"Update {file_name} with new message"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        subprocess.run(['git', 'push'], check=True)
        messagebox.showinfo("Success", f"File '{file_name}' successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"An error occurred while pushing to GitHub: {e}")

def apply_label(label_message):
    def handle_barcode_scan():
        barcode = simpledialog.askstring("Scan Barcode", "Please scan a barcode:")
        if barcode:
            board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
            file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_name = getpass.getuser()
            computer_name = socket.gethostname()
            issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {label_message}"

            try:
                with open(file_name, 'a+') as file:
                    if os.path.getsize(file_name) == 0:
                        file.write(f"Board Name: {board_name}\n")
                        file.write(f"Board Revision: {board_rev}\n")
                        file.write(f"Board Variant: {board_var}\n")
                        file.write(f"Board Serial Number: {board_sn}\n")
                    file.write(f"{issue_message}\n")
                messagebox.showinfo("Success", f"Label '{label_message}' applied to '{file_name}'.")
                push_to_github(file_name)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while writing to the file '{file_name}': {e}")
        else:
            messagebox.showwarning("Warning", "No barcode scanned.")

    return handle_barcode_scan

def delete_file():
    barcode = simpledialog.askstring("Delete File", "Scan a barcode to delete the associated file:")
    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        if os.path.exists(file_name):
            os.remove(file_name)
            messagebox.showinfo("Success", f"File '{file_name}' deleted.")
            try:
                subprocess.run(['git', 'rm', file_name], check=True)
                subprocess.run(['git', 'commit', '-m', f"Delete {file_name}"], check=True)
                subprocess.run(['git', 'push'], check=True)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"An error occurred while pushing deletion to GitHub: {e}")
        else:
            messagebox.showwarning("Warning", f"File '{file_name}' not found.")
    else:
        messagebox.showwarning("Warning", "No barcode provided.")

def enter_new_message(board_name, board_rev, board_var, board_sn, existing_issues):
    file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")

    def submit_message():
        issue_message = message_entry.get()
        if issue_message:
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_name = getpass.getuser()
            computer_name = socket.gethostname()
            issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {issue_message}"
            try:
                with open(file_name, 'a+') as file:
                    if os.path.getsize(file_name) == 0:
                        file.write(f"Board Name: {board_name}\n")
                        file.write(f"Board Revision: {board_rev}\n")
                        file.write(f"Board Variant: {board_var}\n")
                        file.write(f"Board Serial Number: {board_sn}\n")
                    file.write(f"{issue_message}\n")
                messagebox.showinfo("Success", f"File '{file_name}' updated with new message.")
                push_to_github(file_name)
                message_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while writing to the file '{file_name}': {e}")
        else:
            messagebox.showwarning("Warning", "Message cannot be empty.")

    message_window = tk.Toplevel(root)
    message_window.title("Enter New Message")
    tk.Label(message_window, text="Enter your message:").pack(pady=5)
    message_entry = tk.Entry(message_window, width=50)
    message_entry.pack(pady=5)
    tk.Button(message_window, text="Submit", command=submit_message).pack(pady=10)

def scan_barcode():
    barcode = simpledialog.askstring("Scan Barcode", "Please scan a barcode:")
    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        existing_issues = read_existing_issues(file_name)

        def handle_selection():
            choice = option_var.get()
            if choice == '1':
                enter_new_message(board_name, board_rev, board_var, board_sn, existing_issues)
            elif choice == 'x':
                selection_window.destroy()

        selection_window = tk.Toplevel(root)
        selection_window.title("Options")
        option_var = tk.StringVar()
        option_var.set('1')  # Default to new message

        tk.Label(selection_window, text="Choose an option:").pack(pady=5)
        tk.Radiobutton(selection_window, text="Enter new message", variable=option_var, value='1').pack(anchor='w')
        tk.Radiobutton(selection_window, text="Return to welcome screen", variable=option_var, value='x').pack(anchor='w')
        tk.Button(selection_window, text="OK", command=handle_selection).pack(pady=10)
    else:
        messagebox.showwarning("Warning", "No barcode scanned.")

def label_screen():
    label_window = tk.Toplevel(root)
    label_window.title("Apply a Label")

    tk.Label(label_window, text="Choose a label to apply:").pack(pady=10)
    tk.Button(label_window, text="Label Created", command=apply_label("LABEL CREATED")).pack(pady=5)
    tk.Button(label_window, text="Bring-up Testing: PASS", command=apply_label("BRING-UP TEST: PASS")).pack(pady=5)
    tk.Button(label_window, text="Final Assembly Testing: PASS", command=apply_label("FINAL ASSEMBLY TEST: PASS")).pack(pady=5)
    tk.Button(label_window, text="Close", command=label_window.destroy).pack(pady=10)

def setup_tabs():
    tab_control = ttk.Notebook(root)
    
    # Labels Tab
    labels_tab = ttk.Frame(tab_control)
    tab_control.add(labels_tab, text='Labels')
    tk.Button(labels_tab, text="Apply a Label", command=label_screen).pack(pady=20)
    tk.Button(labels_tab, text="Delete a File", command=delete_file).pack(pady=20)
    
    # Trends Tab (Placeholder)
    trends_tab = ttk.Frame(tab_control)
    tab_control.add(trends_tab, text='Trends')
    tk.Label(trends_tab, text="Trends functionality coming soon...", font=("Arial", 14)).pack(pady=20)
    
    # Boards Tab (Placeholder)
    boards_tab = ttk.Frame(tab_control)
    tab_control.add(boards_tab, text='Boards')
    tk.Label(boards_tab, text="Boards functionality coming soon...", font=("Arial", 14)).pack(pady=20)
    
    # About Tab
    about_tab = ttk.Frame(tab_control)
    tab_control.add(about_tab, text='About')
    tk.Label(about_tab, text="By Nolan Manteufel", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="Mesa Technologies", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="(c) 2024", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text=f"Version {VERSION}", font=("Arial", 12)).pack(pady=5)

    tab_control.pack(expand=1, fill="both")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("redTAG")
    root.geometry("400x300")
    setup_tabs()
    root.mainloop()
