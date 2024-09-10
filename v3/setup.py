# setup.py

import tkinter as tk
from tkinter import ttk
from common import display_message_content, tab_control, board_info_tab, trends_tab, boards_subtab_control, messages_subtab
from labels import apply_selected_label, remove_label, update_label_list
from red_tags import apply_selected_red_tag_message, remove_red_tag_message, update_red_tag_messages_list
from utils import pull_from_github, delete_file
from barcode import scan_barcode

def setup_tabs(root):
    global tab_control, board_info_tab, trends_tab, boards_subtab_control, messages_subtab
    global message_text, board_name_label, board_var_label, board_rev_label, board_sn_label

    tab_control = ttk.Notebook(root)
    
    # Controls Tab
    controls_tab = ttk.Frame(tab_control)
    tab_control.add(controls_tab, text='Controls')

    controls_button_frame = ttk.Frame(controls_tab)
    controls_button_frame.pack(pady=10, padx=10, anchor=tk.W)

    scan_button = tk.Button(controls_button_frame, text="Scan a Barcode", command=scan_barcode)
    scan_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(controls_button_frame, text="Delete a File", command=delete_file)
    delete_button.pack(side=tk.LEFT, padx=5)

    update_button = tk.Button(controls_button_frame, text="Update", command=pull_from_github)
    update_button.pack(side=tk.LEFT, padx=5)

    controls_subtab_control = ttk.Notebook(controls_tab)
    controls_subtab_control.pack(expand=1, fill="both")

    process_messages_subtab = ttk.Frame(controls_subtab_control)
    controls_subtab_control.add(process_messages_subtab, text='Process Messages')
    
    new_label_frame = ttk.Frame(process_messages_subtab)
    new_label_frame.pack(pady=10, padx=10, fill=tk.X)

    new_label_entry = tk.Entry(new_label_frame, width=30)
    new_label_entry.pack(side=tk.LEFT, padx=5)

    add_label_button = tk.Button(new_label_frame, text="Add New Process Message", command=apply_selected_label)
    add_label_button.pack(side=tk.LEFT, padx=5)

    label_list_frame = ttk.Frame(process_messages_subtab)
    label_list_frame.pack(pady=10, padx=10, fill=tk.X)

    selected_label_var = tk.StringVar()

    label_button_frame = ttk.Frame(process_messages_subtab)
    label_button_frame.pack(pady=10)

    apply_label_button = tk.Button(label_button_frame, text="Apply Label", command=apply_selected_label)
    apply_label_button.pack(side=tk.LEFT, padx=5)

    remove_label_button = tk.Button(label_button_frame, text="Remove", command=remove_label)
    remove_label_button.pack(side=tk.LEFT, padx=5)

    red_tag_messages_subtab = ttk.Frame(controls_subtab_control)
    controls_subtab_control.add(red_tag_messages_subtab, text='Red Tag Messages')
    
    new_red_tag_message_frame = ttk.Frame(red_tag_messages_subtab)
    new_red_tag_message_frame.pack(pady=10, padx=10, fill=tk.X)

    new_red_tag_message_entry = tk.Entry(new_red_tag_message_frame, width=30)
    new_red_tag_message_entry.pack(side=tk.LEFT, padx=5)

    add_red_tag_message_button = tk.Button(new_red_tag_message_frame, text="Add New Red Tag Message", command=apply_selected_red_tag_message)
    add_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    red_tag_message_list_frame = ttk.Frame(red_tag_messages_subtab)
    red_tag_message_list_frame.pack(pady=10, padx=10, fill=tk.X)

    selected_red_tag_message_var = tk.StringVar()

    red_tag_button_frame = ttk.Frame(red_tag_messages_subtab)
    red_tag_button_frame.pack(pady=10)

    apply_red_tag_message_button = tk.Button(red_tag_button_frame, text="Apply Message", command=apply_selected_red_tag_message)
    apply_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    remove_red_tag_message_button = tk.Button(red_tag_button_frame, text="Remove", command=remove_red_tag_message)
    remove_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    # Trends Tab
    trends_tab = ttk.Frame(tab_control)
    tab_control.add(trends_tab, text='Trending')
    tk.Label(trends_tab, text="Trends functionality coming soon...", font=("Arial", 14)).pack(pady=20)
    tab_control.tab(trends_tab, state='disabled')

    # Board Information Tab
    board_info_tab = ttk.Frame(tab_control)
    tab_control.add(board_info_tab, text='Board Information')

    board_info_frame = ttk.Frame(board_info_tab)
    board_info_frame.pack(fill=tk.X, padx=10, pady=10)

    board_name_label = ttk.Label(board_info_frame, text="Board Name: N/A", font=("Arial", 12))
    board_name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

    board_var_label = ttk.Label(board_info_frame, text="Board Variant: N/A", font=("Arial", 12))
    board_var_label.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

    board_rev_label = ttk.Label(board_info_frame, text="Board Revision: N/A", font=("Arial", 12))
    board_rev_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

    board_sn_label = ttk.Label(board_info_frame, text="Board SN: N/A", font=("Arial", 12))
    board_sn_label.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

    boards_subtab_control = ttk.Notebook(board_info_tab)
    boards_subtab_control.pack(expand=1, fill="both")

    process_history_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(process_history_subtab, text='Process History')

    messages_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(messages_subtab, text='Messages')

    message_text = tk.Text(messages_subtab, wrap=tk.WORD)
    message_text.pack(expand=True, fill='both')

    new_message_entry = tk.Entry(messages_subtab, width=50)
    new_message_entry.pack(side=tk.LEFT, padx=10, pady=10)

    add_message_button = tk.Button(messages_subtab, text="Add Custom Message", command=apply_selected_label)
    add_message_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Set the default window size to 1280x720 pixels
    root.geometry("1280x720")

    # Disable the Board Information tab until a barcode is scanned
    tab_control.tab(board_info_tab, state='disabled')

    # Testing Subtab
    testing_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(testing_subtab, text='Testing')
    tk.Label(testing_subtab, text="Testing management will go here.").pack(pady=20)
    
    # About Tab
    about_tab = ttk.Frame(tab_control)
    tab_control.add(about_tab, text='About')
    tk.Label(about_tab, text="By Nolan Manteufel", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="Mesa Technologies", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="(c) 2024", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="Version 2.0", font=("Arial", 12)).pack(pady=5)

    tab_control.pack(expand=1, fill="both")
