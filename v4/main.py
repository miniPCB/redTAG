from setup import setup_tabs, initialize_application

if __name__ == "__main__":
    root = initialize_application()
    setup_tabs(root)
    root.mainloop()
