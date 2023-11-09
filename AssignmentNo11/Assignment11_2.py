import hashlib
import os
import sys

def find_duplicate_files(directory):
    # Dictionary to store file hashes and their corresponding file paths
    file_hashes = {}

    # Iterate through all files in the directory and its subdirectories
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)

            # Calculate the MD5 hash of the file
            with open(filepath, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()

            # If the hash is already in the dictionary, it's a duplicate
            if file_hash in file_hashes:
                file_hashes[file_hash].append(filepath)
            else:
                file_hashes[file_hash] = [filepath]

    # Write the names of duplicate files to Log.txt
    with open('Log.txt', 'w') as log_file:
        for file_hash, file_paths in file_hashes.items():
            if len(file_paths) > 1:
                log_file.write(f'Duplicate files (Hash: {file_hash}):\n')
                for file_path in file_paths:
                    log_file.write(f'- {file_path}\n')

def main():
    if len(sys.argv) != 2:
        print("Usage: DirectoryDuplicate.py <directory>")
    else:
        directory = sys.argv[1]
        find_duplicate_files(directory)
        print("Duplicate files have been logged in Log.txt")

if __name__ == "__main__":
    main()