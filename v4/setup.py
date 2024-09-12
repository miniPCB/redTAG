#import tkinter as tk
#from tkinter import ttk
from labels import load_labels_from_file
from red_tags import load_red_tag_messages_from_file
from common import *
from barcode import scan_barcode
from utils import pull_from_github

def setup_tabs(root):
    global tab_control, board_info_tab, boards_subtab_control, messages_subtab, trending_tab
    global board_name_label, board_var_label, board_rev_label, board_sn_label
    global new_label_entry, label_list_frame, selected_label_var
    global new_red_tag_message_entry, red_tag_message_list_frame, selected_red_tag_message_var

    tab_control = ttk.Notebook(root)
    
    # Controls Tab
    controls_tab = ttk.Frame(tab_control)
    tab_control.add(controls_tab, text='Controls')

    # Add the "Scan a Barcode", "Delete a File", and "Update" buttons side-by-side
    controls_button_frame = ttk.Frame(controls_tab)
    controls_button_frame.pack(pady=10, padx=10, anchor=tk.W)

    scan_button = tk.Button(controls_button_frame, text="Scan a Barcode", command=scan_barcode)
    scan_button.pack(side=tk.LEFT, padx=5)

    delete_button = tk.Button(controls_button_frame, text="Delete a File", command=delete_file)
    delete_button.pack(side=tk.LEFT, padx=5)

    update_button = tk.Button(controls_button_frame, text="Update", command=pull_from_github)
    update_button.pack(side=tk.LEFT, padx=5)

    # Sub-tabs within Controls Tab
    controls_subtab_control = ttk.Notebook(controls_tab)
    controls_subtab_control.pack(expand=1, fill="both")

    # Process Messages Subtab within Controls
    process_messages_subtab = ttk.Frame(controls_subtab_control)
    controls_subtab_control.add(process_messages_subtab, text='Process Messages')
    
    # Add New Process Message field and button
    new_label_frame = ttk.Frame(process_messages_subtab)
    new_label_frame.pack(pady=10, padx=10, fill=tk.X)

    new_label_entry = tk.Entry(new_label_frame, width=30)
    new_label_entry.pack(side=tk.LEFT, padx=5)

    add_label_button = tk.Button(new_label_frame, text="Add New Process Message")
    add_label_button.pack(side=tk.LEFT, padx=5)

    # List of labels with radio buttons
    label_list_frame = ttk.Frame(process_messages_subtab)
    label_list_frame.pack(pady=10, padx=10, fill=tk.X)

    # Apply and Remove Label buttons
    label_button_frame = ttk.Frame(process_messages_subtab)
    label_button_frame.pack(pady=10)

    apply_label_button = tk.Button(label_button_frame, text="Apply Label")
    apply_label_button.pack(side=tk.LEFT, padx=5)

    remove_label_button = tk.Button(label_button_frame, text="Remove")
    remove_label_button.pack(side=tk.LEFT, padx=5)

    # Red Tag Messages Subtab within Controls
    red_tag_messages_subtab = ttk.Frame(controls_subtab_control)
    controls_subtab_control.add(red_tag_messages_subtab, text='Red Tag Messages')
    
    # Add New Red Tag Message field and button
    new_red_tag_message_frame = ttk.Frame(red_tag_messages_subtab)
    new_red_tag_message_frame.pack(pady=10, padx=10, fill=tk.X)

    new_red_tag_message_entry = tk.Entry(new_red_tag_message_frame, width=30)
    new_red_tag_message_entry.pack(side=tk.LEFT, padx=5)

    add_red_tag_message_button = tk.Button(new_red_tag_message_frame, text="Add New Red Tag Message")
    add_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    # List of Red Tag messages with radio buttons
    red_tag_message_list_frame = ttk.Frame(red_tag_messages_subtab)
    red_tag_message_list_frame.pack(pady=10, padx=10, fill=tk.X)

    # Apply and Remove Red Tag Message buttons
    red_tag_button_frame = ttk.Frame(red_tag_messages_subtab)
    red_tag_button_frame.pack(pady=10)

    apply_red_tag_message_button = tk.Button(red_tag_button_frame, text="Apply Message")
    apply_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    remove_red_tag_message_button = tk.Button(red_tag_button_frame, text="Remove")
    remove_red_tag_message_button.pack(side=tk.LEFT, padx=5)

    # Trending Tab (renamed from Trends)
    trending_tab = ttk.Frame(tab_control)
    tab_control.add(trending_tab, text='Trending')
    tk.Label(trending_tab, text="Trending functionality coming soon...", font=("Arial", 14)).pack(pady=20)
    tab_control.tab(trending_tab, state='disabled')  # Disable the Trending tab until a barcode is scanned
    
    # Board Information Tab with Subtabs
    board_info_tab = ttk.Frame(tab_control)
    tab_control.add(board_info_tab, text='Board Information')

    # Board Info Section at the Top
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

    # Subtabs within Board Information
    boards_subtab_control = ttk.Notebook(board_info_tab)
    boards_subtab_control.pack(expand=1, fill="both")

    # Process History Subtab (renamed from Labels)
    process_history_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(process_history_subtab, text='Process History')
    tk.Label(process_history_subtab, text="Process history management will go here.").pack(pady=20)

    # Messages Subtab
    messages_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(messages_subtab, text='Messages')
    
    global message_text, new_message_entry
    message_text = tk.Text(messages_subtab, wrap=tk.WORD)
    message_text.pack(expand=True, fill='both')

    new_message_entry = tk.Entry(messages_subtab, width=50)
    new_message_entry.pack(side=tk.LEFT, padx=10, pady=10)
    
    add_message_button = tk.Button(messages_subtab, text="Add Custom Message")
    add_message_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Testing Subtab
    testing_subtab = ttk.Frame(boards_subtab_control)
    boards_subtab_control.add(testing_subtab, text='Testing')
    tk.Label(testing_subtab, text="Testing management will go here.").pack(pady=20)
    
    # Build Information Tab
    build_info_tab = ttk.Frame(tab_control)
    tab_control.add(build_info_tab, text='Build Information')
    tk.Label(build_info_tab, text="Build information functionality coming soon...", font=("Arial", 14)).pack(pady=20)

    # Quality Information Tab
    quality_info_tab = ttk.Frame(tab_control)
    tab_control.add(quality_info_tab, text='Quality Information')
    tk.Label(quality_info_tab, text="Quality information functionality coming soon...", font=("Arial", 14)).pack(pady=20)
    
    # About Tab
    about_tab = ttk.Frame(tab_control)
    tab_control.add(about_tab, text='About')
    tk.Label(about_tab, text="By Nolan Manteufel", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="Mesa Technologies", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="(c) 2024", font=("Arial", 12)).pack(pady=5)
    tk.Label(about_tab, text="Version 2.0", font=("Arial", 12)).pack(pady=5)

    tab_control.pack(expand=1, fill="both")

def initialize_application():
    root = tk.Tk()
    root.title("redTAG")
    root.geometry("1280x720")


    try:
        icon = PhotoImage(file=ICON_FILEPATHNAME)
        root.iconphoto(False, icon)
    except Exception as e:
        print(f"Error loading icon: {e}")

    #icon = tk.PhotoImage(file=ICON_FILEPATHNAME)
    #root.iconphoto(False, icon)
    load_labels_from_file()  # Load labels from JSON file on startup
    load_red_tag_messages_from_file()  # Load Red Tag messages from JSON file on startup
    return root
