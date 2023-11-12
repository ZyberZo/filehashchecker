# Import necessary libraries
import hashlib
import tkinter as tk
from tkinter import filedialog

# Function to calculate SHA-256 hash of a file
def calculate_hash(file_path, block_size=4096):
    hasher = hashlib.sha256()  # Create a hash object

    # Open the file and read it in chunks
    with open(file_path, 'rb') as file:
        chunk = file.read(block_size)
        while chunk:
            hasher.update(chunk)  # Update the hash with each chunk
            chunk = file.read(block_size)

    return hasher.hexdigest()  # Return the hexadecimal representation of the hash

# Function to check the hash of a selected file
def perform_hash_check():
    # Create a Tkinter root window (but don't show it)
    root = tk.Tk()
    root.withdraw()

    # Ask the user to choose a file using a simple dialog
    file_path = filedialog.askopenfilename(title="Select a file for hash check")

    # If the user didn't choose any file, exit
    if not file_path:
        print("No file selected. Exiting.")
        return

    # Ask the user to input the expected hash
    expected_hash = input("Enter the expected hash for the file: ")

    try:
        # Calculate the actual hash of the selected file
        actual_hash = calculate_hash(file_path)

        # Display file information and hashes
        print("\nFile Path:", file_path)
        print("Expected Hash:", expected_hash)
        print("Actual Hash:  ", actual_hash)

        # Check if the expected and actual hashes match
        if expected_hash == actual_hash:
            print("Hash check passed. The file integrity is intact.")
        else:
            print("Hash check failed. The file might be corrupted or modified.")

    # Handle the case where the file is not found
    except FileNotFoundError:
        print("File not found. Please select a valid file.")

    # Handle other unexpected errors
    except Exception as e:
        print("An error occurred:", e)

# Execute the file hash check when the script is run
if __name__ == "__main__":
    perform_hash_check()
