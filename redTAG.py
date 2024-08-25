import re
import os
import datetime
import getpass
import socket
import subprocess

# Constants
GITREPO = "git@github.com:Mesa-NManteufel/redTAG.git"
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

def apply_label_label_created():
    while True:
        print("Scan a barcode to apply the 'LABEL CREATED' message, or type 'x' to finish:")
        barcode = input().strip()
        
        if barcode.lower() == 'x':
            print("Finished applying labels. Returning to the label selection screen.")
            break
        
        if not barcode:
            print("No barcode scanned. Please scan a valid barcode or type 'x' to finish.")
            continue
        
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - Label Created"
        
        with open(file_name, 'a+') as file:
            file.seek(0)
            content = file.read()
            if not content:  # If the file is empty (newly created), write headers
                file.write(f"Board Name: {board_name}\n")
                file.write(f"Board Revision: {board_rev}\n")
                file.write(f"Board Variant: {board_var}\n")
                file.write(f"Board Serial Number: {board_sn}\n")
            file.write(f"{issue_message}\n")
        
        print(f"Label 'LABEL CREATED' applied to '{file_name}'.")

def apply_label_bring_up_testing_pass():
    while True:
        print("Scan a barcode to apply the 'BRING-UP TESTING: PASS' message, or type 'x' to finish:")
        barcode = input().strip()
        
        if barcode.lower() == 'x':
            print("Finished applying labels. Returning to the label selection screen.")
            break
        
        if not barcode:
            print("No barcode scanned. Please scan a valid barcode or type 'x' to finish.")
            continue
        
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - Bring-up testing: PASS"
        
        with open(file_name, 'a+') as file:
            file.seek(0)
            content = file.read()
            if not content:  # If the file is empty (newly created), write headers
                file.write(f"Board Name: {board_name}\n")
                file.write(f"Board Revision: {board_rev}\n")
                file.write(f"Board Variant: {board_var}\n")
                file.write(f"Board Serial Number: {board_sn}\n")
            file.write(f"{issue_message}\n")
        
        print(f"Label 'BRING-UP TESTING: PASS' applied to '{file_name}'.")

def apply_label_final_assembly_testing_pass():
    while True:
        print("Scan a barcode to apply the 'FINAL ASSEMBLY TESTING: PASS' message, or type 'x' to finish:")
        barcode = input().strip()
        
        if barcode.lower() == 'x':
            print("Finished applying labels. Returning to the label selection screen.")
            break
        
        if not barcode:
            print("No barcode scanned. Please scan a valid barcode or type 'x' to finish.")
            continue
        
        board_name, board_rev, board_var, board_sn = parse_pcb_barcode(barcode)
        file_name = os.path.join(SAVE_DIRECTORY, f"{board_name}-{board_rev}-{board_var}-{board_sn}.txt")
        
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        user_name = getpass.getuser()
        computer_name = socket.gethostname()
        issue_message = f"Message: {current_datetime} - {user_name}@{computer_name} - Final assembly testing: PASS"
        
        with open(file_name, 'a+') as file:
            file.seek(0)
            content = file.read()
            if not content:  # If the file is empty (newly created), write headers
                file.write(f"Board Name: {board_name}\n")
                file.write(f"Board Revision: {board_rev}\n")
                file.write(f"Board Variant: {board_var}\n")
                file.write(f"Board Serial Number: {board_sn}\n")
            file.write(f"{issue_message}\n")
        
        print(f"Label 'FINAL ASSEMBLY TESTING: PASS' applied to '{file_name}'.")

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
            apply_label_label_created()
            input("\nPress ENTER to return to the label selection screen.")
        elif user_input == '2':
            apply_label_bring_up_testing_pass()
            input("\nPress ENTER to return to the label selection screen.")
        elif user_input == '3':
            apply_label_final_assembly_testing_pass()
            input("\nPress ENTER to return to the label selection screen.")
        else:
            print("Invalid input. Please try again.")

def welcome_page():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        print("-----------------------------------------------------------------")
        print("\n  Welcome to redTAG!\n  A simple system for collecting Red Tag messages.")
        print("\n  By Nolan Manteufel\n  Mesa Technologies\n  (c)2024")
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

        elif action == 'welcome':
            push_to_github(file_name)
            pull_from_github()
            break  # Exit the loop to return to the welcome page

def push_to_github(file_name):
    try:
        # Stage the file for commit
        subprocess.run(['git', 'add', file_name], check=True)
        # Commit the file with a message
        commit_message = f"Update {file_name} with new issue"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        # Push the changes to the remote repository
        subprocess.run(['git', 'push'], check=True)
        print(f"Successfully pushed {file_name} to GitHub.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pushing to GitHub: {e}")

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
