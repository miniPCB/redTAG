import os
import datetime
import getpass
import socket
from tkinter import messagebox, simpledialog
from utils import parse_pcb_barcode, push_to_github

SAVE_DIRECTORY = "/home/pi/redTAG/redtags"

def scan_barcode():
    barcode = simpledialog.askstring("Scan Barcode", "Please scan a barcode:")
    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        display_message_content(board_name, board_rev, board_var, board_sn)
        # Enable the Board Information and Trends tabs
        from setup import tab_control, board_info_tab, trends_tab, boards_subtab_control, messages_subtab
        tab_control.tab(board_info_tab, state='normal')
        tab_control.tab(trends_tab, state='normal')
        tab_control.select(board_info_tab)
        boards_subtab_control.select(messages_subtab)
    else:
        messagebox.showwarning("Warning", "No barcode scanned.")

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

def scan_barcode_and_apply_message(message, message_type):
    while True:
        barcode = simpledialog.askstring(f"Apply {message_type} Message", f"Apply {message_type} message: '{message}'. Scan a barcode (or type 'x' to finish):")
        
        if barcode is None or barcode.lower() == 'x':
            break
        
        if not barcode:
            messagebox.showwarning("Warning", "No barcode scanned. Please scan a valid barcode.")
            continue
        
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {message}"
        
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
