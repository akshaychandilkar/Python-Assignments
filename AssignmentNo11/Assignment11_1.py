import hashlib
import os
import sys

# Function to calculate the checksum of a file
def calculate_checksum(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            checksum = hashlib.md5(file_content).hexdigest()
            return checksum
    except Exception as e:
        log_message(f"Error calculating checksum for {file_path}: {str(e)}")
        return None

# Function to log messages to a log file
def log_message(message):
    with open("logfile.txt", "a") as log_file:
        log_file.write(message + "\n")

# Function to list files in a directory and calculate checksum for each
def directory_checksum(directory_name):
    try:
        if not os.path.exists(directory_name):
            message = f"Directory {directory_name.capitalize()} does not exist."
            log_message(message)  # Log the message to the file
            return

        message = f"Calculating checksum for files in '{directory_name}':"
        print(message)  # Print the message to console
        log_message(message)  # Log the message to the file

        for root, _, files in os.walk(directory_name):
            for file in files:
                file_path = os.path.join(root, file)
                checksum = calculate_checksum(file_path)
                if checksum is not None:
                    # Format the file path to avoid extra spaces
                    file_path = file_path.replace("\\", "/")  # Replace backslashes with forward slashes
                    message = f"File: {file_path} | Checksum: {checksum}"
                    print(message)  # Print the message to console
                    log_message(message)  # Log the message to the file

        message = "Checksum calculation completed."
        print(message)  # Print the message to console
        log_message(message)  # Log the message to the file
    except Exception as e:
        log_message(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 2:
        log_message("Usage: DirectoryChecksum.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]
    directory_checksum(directory_name)

if __name__ == "__main__":
    main()