"""Task 1: Directory Inspector:

Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. Your script should prompt the user for the directory path and then display the contents.
"""

import os

def list_directory_contents(path):
    try:
        # Check if the given path is a valid directory
        if not os.path.isdir(path):
            print(f"The path '{path}' is not a valid directory.")
            return
        
        # List all files and subdirectories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                if entry.is_dir():
                    print(f"[DIR] {entry.name}")
                else:
                    print(f"[FILE] {entry.name}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ")
    list_directory_contents(directory_path)
