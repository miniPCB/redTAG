from tkinter import ttk, Frame, Label, Button

class setup_tabs:
    def __init__(self, master):
        self.master = master
        self.master.title("Red Tag")
        self.master.geometry("1280x720")

        # Create the main notebook (tab control)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(expand=True, fill='both')

        # Add the tabs to the notebook
        self.add_controls_tab()
        self.add_trending_tab()
        self.add_board_information_tab()
        self.add_build_information_tab()
        self.add_quality_information_tab()

    def add_controls_tab(self):
        # Create a new frame for the Controls tab
        controls_frame = Frame(self.notebook)
        controls_frame.pack(fill='both', expand=True)

        # Add buttons near the top of the Controls tab
        scan_button = Button(controls_frame, text="Scan a Barcode")
        delete_button = Button(controls_frame, text="Delete a File")
        update_button = Button(controls_frame, text="Update Local Files")

        scan_button.pack(side="left", padx=10, pady=10)
        delete_button.pack(side="left", padx=10, pady=10)
        update_button.pack(side="left", padx=10, pady=10)

        # Create sub-tabs under the buttons
        sub_notebook = ttk.Notebook(controls_frame)
        sub_notebook.pack(expand=True, fill='both', pady=(10, 0))

        # Process Messages tab
        process_messages_frame = Frame(sub_notebook)
        process_messages_frame.pack(fill='both', expand=True)
        sub_notebook.add(process_messages_frame, text="Process Messages")

        # Red Tag Messages tab
        red_tag_messages_frame = Frame(sub_notebook)
        red_tag_messages_frame.pack(fill='both', expand=True)
        sub_notebook.add(red_tag_messages_frame, text="Red Tag Messages")

        # Add the Controls tab to the notebook
        self.notebook.add(controls_frame, text="Controls")

    def add_trending_tab(self):
        trending_frame = Frame(self.notebook)
        trending_frame.pack(fill='both', expand=True)
        label = Label(trending_frame, text="Trending Tab Content")
        label.pack(pady=10, padx=10)
        self.notebook.add(trending_frame, text="Trending")

    def add_board_information_tab(self):
        board_info_frame = Frame(self.notebook)
        board_info_frame.pack(fill='both', expand=True)
        label = Label(board_info_frame, text="Board Information Tab Content")
        label.pack(pady=10, padx=10)
        self.notebook.add(board_info_frame, text="Board Information")

    def add_build_information_tab(self):
        build_info_frame = Frame(self.notebook)
        build_info_frame.pack(fill='both', expand=True)
        label = Label(build_info_frame, text="Build Information Tab Content")
        label.pack(pady=10, padx=10)
        self.notebook.add(build_info_frame, text="Build Information")

    def add_quality_information_tab(self):
        quality_info_frame = Frame(self.notebook)
        quality_info_frame.pack(fill='both', expand=True)
        label = Label(quality_info_frame, text="Quality Information Tab Content")
        label.pack(pady=10, padx=10)
        self.notebook.add(quality_info_frame, text="Quality Information")

