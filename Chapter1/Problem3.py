import os

# Specify the directory path (you can change it to any directory)
directory_path = "."

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory_path)

    print(f"Contents of directory '{os.path.abspath(directory_path)}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
except Exception as e:
    print(f"An error occurred: {e}")
