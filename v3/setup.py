from labels import init_labels_variables, apply_selected_label, remove_label, new_label_entry, label_list_frame, selected_label_var
from red_tags import init_red_tag_variables, apply_selected_red_tag_message, remove_red_tag_message, new_red_tag_message_entry, red_tag_message_list_frame, selected_red_tag_message_var

def setup_tabs(root):
    global tab_control, board_info_tab, boards_subtab_control, messages_subtab, trends_tab
    global board_name_label, board_var_label, board_rev_label, board_sn_label
    global new_label_entry, label_list_frame, selected_label_var
    global new_red_tag_message_entry, red_tag_message_list_frame, selected_red_tag_message_var

    # Initialize variables for labels and red tag messages
    init_labels_variables()
    init_red_tag_variables()

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

    update_button = tk.Button(controls_button_frame, text="Update", command=update_message)
    update_button.pack(side=tk.LEFT, padx=5)

    # Continue with the rest of the setup...
