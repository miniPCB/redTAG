from tkinter import ttk, Frame, Label

class setup_tabs:
    def __init__(self, master):
        self.master = master
        self.master.title("Red Tag")  # Set window title
        self.master.geometry("1280x720")  # Set window size

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

        # Add a simple label to the Controls tab
        label = Label(controls_frame, text="Controls Tab Content")
        label.pack(pady=10, padx=10)

        # Add the Controls tab to the notebook
        self.notebook.add(controls_frame, text="Controls")

    def add_trending_tab(self):
        # Create a new frame for the Trending tab
        trending_frame = Frame(self.notebook)
        trending_frame.pack(fill='both', expand=True)

        # Add a simple label to the Trending tab
        label = Label(trending_frame, text="Trending Tab Content")
        label.pack(pady=10, padx=10)

        # Add the Trending tab to the notebook
        self.notebook.add(trending_frame, text="Trending")

    def add_board_information_tab(self):
        # Create a new frame for the Board Information tab
        board_info_frame = Frame(self.notebook)
        board_info_frame.pack(fill='both', expand=True)

        # Add a simple label to the Board Information tab
        label = Label(board_info_frame, text="Board Information Tab Content")
        label.pack(pady=10, padx=10)

        # Add the Board Information tab to the notebook
        self.notebook.add(board_info_frame, text="Board Information")

    def add_build_information_tab(self):
        # Create a new frame for the Build Information tab
        build_info_frame = Frame(self.notebook)
        build_info_frame.pack(fill='both', expand=True)

        # Add a simple label to the Build Information tab
        label = Label(build_info_frame, text="Build Information Tab Content")
        label.pack(pady=10, padx=10)

        # Add the Build Information tab to the notebook
        self.notebook.add(build_info_frame, text="Build Information")

    def add_quality_information_tab(self):
        # Create a new frame for the Quality Information tab
        quality_info_frame = Frame(self.notebook)
        quality_info_frame.pack(fill='both', expand=True)

        # Add a simple label to the Quality Information tab
        label = Label(quality_info_frame, text="Quality Information Tab Content")
        label.pack(pady=10, padx=10)

        # Add the Quality Information tab to the notebook
        self.notebook.add(quality_info_frame, text="Quality Information")
