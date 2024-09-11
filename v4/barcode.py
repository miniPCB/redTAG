import tkinter as tk
from common import display_message_content, tab_control, board_info_tab, trends_tab, boards_subtab_control, messages_subtab
from utils import parse_pcb_barcode, push_to_github

def scan_barcode():
    barcode = tk.simpledialog.askstring("Scan Barcode", "Please scan a barcode:")
    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        display_message_content(board_name, board_rev, board_var, board_sn)
        # Enable the Board Information and Trends tabs
        tab_control.tab(board_info_tab, state='normal')
        tab_control.tab(trends_tab, state='normal')
        # Switch to the Board Information > Messages tab
        tab_control.select(board_info_tab)
        boards_subtab_control.select(messages_subtab)
    else:
        tk.messagebox.showwarning("Warning", "No barcode scanned.")
