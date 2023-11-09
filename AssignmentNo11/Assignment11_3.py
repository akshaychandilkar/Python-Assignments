import hashlib
import os
import sys

def find_duplicate_files(directory):
    # Create a dictionary to store file hashes and their paths
    file_hashes = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Calculate the MD5 hash of the file
            with open(file_path, 'rb') as file:
                file_hash = hashlib.md5(file.read()).hexdigest()
            
            # Check if this hash already exists in the dictionary
            if file_hash in file_hashes:
                duplicates.append(file_path)
            else:
                file_hashes[file_hash] = file_path
    
    return duplicates

def remove_duplicates(duplicates):
    with open('Log.txt', 'w') as log_file:
        for duplicate in duplicates:
            log_file.write(duplicate + '\n')
            os.remove(duplicate)
            print(f"Deleted duplicate file: {duplicate}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python DuplicateRemoval.py <directory_name>")
        sys.exit(1)

    directory_name = sys.argv[1]
    if not os.path.exists(directory_name):
        print(f"Directory '{directory_name}' does not exist.")
        sys.exit(1)

    duplicates = find_duplicate_files(directory_name)
    if duplicates:
        remove_duplicates(duplicates)
    else:
        print("No duplicate files found in the directory.")

if __name__ == "__main__":
    main()