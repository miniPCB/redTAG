import re
import os
import datetime
import getpass
import socket
import subprocess

# Constants
GITREPO = "git@github.com:miniPCB/redTAG.git"
SAVE_DIRECTORY = "/home/pi/redTAG/redtags"

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

def apply_label(label_message):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before each label application
        print(f"Apply label: '{label_message}'. Type 'x' when finished.")
        barcode = input().strip()
        
        if barcode.lower() == 'x':
            print("Finished applying labels. Returning to the label selection screen.")
            break
        
        if not barcode:
            print("No barcode scanned. Please scan a valid barcode or type 'x' to finish.")
            continue
        
        # Parse the barcode
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        
        # Prepare the message to be added
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {label_message}"
        
        try:
            # Open the file in append mode and write the new label
            with open(file_name, 'a+') as file:
                # If the file is newly created, add headers
                if os.path.getsize(file_name) == 0:
                    file.write(f"Board Name: {board_name}\n")
                    file.write(f"Board Revision: {board_rev}\n")
                    file.write(f"Board Variant: {board_var}\n")
                    file.write(f"Board Serial Number: {board_sn}\n")
                file.write(f"{issue_message}\n")
            print(f"Label '{label_message}' applied to '{file_name}'.")
            
            # Push the changes to GitHub after each file operation
            push_to_github(file_name)
        
        except Exception as e:
            print(f"An error occurred while writing to the file '{file_name}': {e}")

        # Allow for the next barcode scan
        print("\nScan another barcode, or 'x' to exit.")

def push_to_github(file_name):
    try:
        # Stage the file for commit
        subprocess.run(['git', 'add', file_name], check=True)
        # Commit the file with a message
        commit_message = f"Update {file_name} with new message"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        # Push the changes to the remote repository
        subprocess.run(['git', 'push'], check=True)
        print(f"File '{file_name}' successfully pushed to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")

def display_label_screen():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("-----------------------------------------------------------------")
        print("\tLABELS:")
        print("\t[1] Label created")
        print("\t[2] Bring-up testing: PASS")
        print("\t[3] Final assembly testing: PASS")
        print("-----------------------------------------------------------------")
        print("\t[x] Return to Welcome page")
        print("-----------------------------------------------------------------")
        user_input = input("Select an option and press ENTER: ").strip().lower()

        if user_input == 'x':
            break  # Exit and return to the welcome screen
        elif user_input == '1':
            apply_label("LABEL CREATED")
        elif user_input == '2':
            apply_label("BRING-UP TEST: PASS")
        elif user_input == '3':
            apply_label("FINAL ASSEMBLY TEST: PASS")
        else:
            print("Invalid input. Please try again.")

def delete_file():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen before deletion
    print("-----------------------------------------------------------------")
    print("DELETE FILE")
    print("-----------------------------------------------------------------")
    barcode = input("Scan a barcode: ").strip()

    if barcode:
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        
        if os.path.exists(file_name):
            os.remove(file_name)
            print(f"File '{file_name}' deleted.")
            # Optionally, push changes to GitHub after deletion
            try:
                subprocess.run(['git', 'rm', file_name], check=True)
                subprocess.run(['git', 'commit', '-m', f"Delete {file_name}"], check=True)
                subprocess.run(['git', 'push'], check=True)
                print(f"File '{file_name}' successfully deleted and changes pushed to GitHub.")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while pushing deletion to GitHub: {e}")
        else:
            print(f"File '{file_name}' not found.")
    else:
        print("No barcode provided.")

    input("\nPress ENTER to return to the Engineer Menu.")

def engineer_menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("-----------------------------------------------------------------")
        print("\tENGINEER MENU:")
        print("\t[1] DELETE FILE")
        print("-----------------------------------------------------------------")
        print("\t[x] Return to Welcome page")
        print("-----------------------------------------------------------------")
        user_input = input("Select an option and press ENTER: ").strip().lower()

        if user_input == 'x':
            return  # Exit and return to the welcome screen
        elif user_input == '1':
            delete_file()  # Call the delete file function
        else:
            print("Invalid input. Please try again.")
            input("Press ENTER to return to the engineer menu.")
            engineer_menu()  # Re-display the engineer menu

def welcome_page():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        print("-----------------------------------------------------------------")
        print("\n  Welcome to redTAG!\n  A simple system for collecting Red Tag messages.")
        print("\n  By Nolan Manteufel\n  Mesa Technologies\n  (c)2024\n  (v)010")
        print("\n  Scan a barcode,\n  See previous messages,\n  Enter new messages!")
        print("-----------------------------------------------------------------")
        print("\tOPTIONS:")
        print("\t[] Press ENTER to scan a barcode")
        print("\t[1] Apply a label")
        print("\t[x] Exit program")
        print("-----------------------------------------------------------------")
        user_input = input("Select an option and press ENTER: ").strip().lower()

        if user_input == 'x':
            print("Exiting program...")
            break
        elif user_input == '1':
            display_label_screen()  # Display the label selection screen
        elif user_input == 'engr':
            engineer_menu()  # Display the engineer menu
        elif user_input == '':
            return 'scan'
        else:
            print("Invalid input. Please try again.")

def read_barcode():
    while True:
        next_action = welcome_page()
        if next_action == 'scan':
            print("Scan a barcode:")
            barcode = input().strip()
            if barcode:
                create_file_with_barcode_data(barcode)
        else:
            break

def prompt_user_for_action(board_name, board_rev, board_var, board_sn, existing_issues):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        print("redTAG!")
        print("------------------------------------------------------------------------------------------------------------")
        print(f"|    \tBoard Name: {board_name}")
        print(f"| \tBoard Rev: {board_rev}")
        print(f"| \tBoard Variant: {board_var}")
        print(f"| \tBoard SN: {board_sn}")
        print("|")
        if existing_issues:
            for issue in existing_issues:
                print(f"| \t{issue}")
        else:
            print("| \tNo existing issues.")
        print("|")
        print("------------------------------------------------------------------------------------------------------------")
        print("redTAG!")
        print("\n\n\n  OPTIONS:")
        print("  [1] Enter new message.")
        print("  [x] Return to welcome screen.")
 
        user_input = input("\nChoose an option: ").strip().lower()

        if user_input == '1':
            issue_message = input("Enter the new message: ").strip()
            # Add the current datetime, username, and computer name to the beginning of the message
            current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user_name = getpass.getuser()
            computer_name = socket.gethostname()
            issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - {issue_message}"
            return 'create', issue_message
        elif user_input == 'x':
            return 'welcome', None
        else:
            print("Invalid input. Please try again.")

def create_file_with_barcode_data(input_string):
    # Parse the barcode
    board_name, board_rev, board_var, board_sn = parse_pcb_barcode(input_string)

    # Create the full file path
    file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")

    # Read existing issues from the file
    existing_issues = read_existing_issues(file_name)

    while True:
        # Prompt the user for action
        action, issue_message = prompt_user_for_action(board_name, board_rev, board_var, board_sn, existing_issues)

        if action == 'create':
            try:
                # Open the file in append mode if it exists, or create it if it doesn't
                with open(file_name, 'a+') as file:
                    file.seek(0)
                    content = file.read()
                    if not content:  # If the file is empty (newly created), write headers
                        file.write(f"Board Name: {board_name}\n")
                        file.write(f"Board Revision: {board_rev}\n")
                        file.write(f"Board Variant: {board_var}\n")
                        file.write(f"Board Serial Number: {board_sn}\n")
                    if issue_message:
                        file.write(f"{issue_message}\n")
                print(f"File '{file_name}' updated with new issue.")
                existing_issues.append(issue_message)  # Add the new issue to the list

                # Re-read the file to ensure all issues are included (in case of multiple updates)
                existing_issues = read_existing_issues(file_name)

                # Push the changes to GitHub after each file operation
                push_to_github(file_name)
            except Exception as e:
                print(f"An error occurred while writing to the file '{file_name}': {e}")

        elif action == 'welcome':
            push_to_github(file_name)
            pull_from_github()
            break  # Exit the loop to return to the welcome page

def pull_from_github():
    try:
        # Reset any local changes to ensure a clean pull
        reset_result = subprocess.run(['git', 'reset', '--hard', 'HEAD'], check=True, text=True, capture_output=True)
        print(reset_result.stdout)

        # Fetch the latest changes from the remote repository
        fetch_result = subprocess.run(['git', 'fetch', 'origin'], check=True, text=True, capture_output=True)
        print(fetch_result.stdout)

        # Merge the latest changes from the remote repository, allowing unrelated histories to be merged
        merge_result = subprocess.run(['git', 'merge', 'origin/main','--allow-unrelated-histories'], check=True, text=True, capture_output=True)
        print(merge_result.stdout)

        # Pull the latest changes into the local branch, allowing unrelated histories to be merged
        pull_result = subprocess.run(['git', 'pull', '--allow-unrelated-histories'], check=True, text=True, capture_output=True)
        print(pull_result.stdout)

        print("Successfully fetched and pulled the latest files from GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while fetching or pulling from GitHub: {e}")
        print(f"Error details: {e.stderr}")

def configure_git_remote():
    try:
        # Set the correct remote repository URL
        subprocess.run(['git', 'remote', 'set-url', 'origin', GITREPO], check=True)
        print(f"Configured the remote repository to {GITREPO}.")

        # Verify the remote repository configuration
        result = subprocess.run(['git', 'remote', '-v'], check=True, text=True, capture_output=True)
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while configuring the remote repository: {e}")

if __name__ == "__main__":
    read_barcode()