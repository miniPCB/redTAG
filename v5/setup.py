from tkinter import ttk, Frame, Label, Button, Entry, StringVar, Radiobutton, IntVar

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
        controls_frame = Frame(self.notebook)
        controls_frame.pack(fill='both', expand=True)

        button_frame = Frame(controls_frame)
        button_frame.pack(side="top", pady=(5, 5))

        scan_button = Button(button_frame, text="Scan a Barcode")
        delete_button = Button(button_frame, text="Delete a File")
        update_button = Button(button_frame, text="Update Local Files")

        scan_button.pack(side="left", padx=5, pady=5)
        delete_button.pack(side="left", padx=5, pady=5)
        update_button.pack(side="left", padx=5, pady=5)

        sub_notebook = ttk.Notebook(controls_frame)
        sub_notebook.pack(expand=True, fill='both', pady=(5, 0))

        process_messages_frame = Frame(sub_notebook)
        process_messages_frame.pack(fill='both', expand=True)
        self.add_process_messages_tab(process_messages_frame)
        sub_notebook.add(process_messages_frame, text="Process Messages")

        red_tag_messages_frame = Frame(sub_notebook)
        red_tag_messages_frame.pack(fill='both', expand=True)
        sub_notebook.add(red_tag_messages_frame, text="Red Tag Messages")

        self.notebook.add(controls_frame, text="Controls")

    def add_process_messages_tab(self, parent):
        # Entry for new process message
        self.new_message_var = StringVar()
        entry_frame = Frame(parent)
        entry_frame.pack(side="top", fill="x", pady=(10, 5), padx=10)

        entry_label = Label(entry_frame, text="Enter Process Message:")
        entry_label.pack(side="left")

        entry_field = Entry(entry_frame, textvariable=self.new_message_var)
        entry_field.pack(side="left", fill="x", expand=True, padx=(5, 10))

        add_button = Button(entry_frame, text="Add Process Message", command=self.add_process_message)
        add_button.pack(side="left")

        # Frame to hold the list of radio buttons
        self.messages_frame = Frame(parent)
        self.messages_frame.pack(fill="both", expand=True, pady=(10, 0), padx=10)

        # Variable to keep track of the selected message
        self.selected_message = IntVar(value=-1)

    def add_process_message(self):
        # Get the new message text
        new_message = self.new_message_var.get().strip()

        if new_message:
            # Get the current count of messages to use as the radio button value
            message_count = len(self.messages_frame.winfo_children())

            # Create a new radio button with the message
            radio_button = Radiobutton(
                self.messages_frame,
                text=new_message,
                variable=self.selected_message,
                value=message_count
            )
            radio_button.pack(anchor="w")

            # Clear the entry field after adding the message
            self.new_message_var.set("")

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

