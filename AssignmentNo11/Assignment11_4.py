import os
import hashlib
import time

def find_duplicate_files(directory):
    # Create a dictionary to store file hashes
    file_hashes = {}
    duplicates = []

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Calculate the hash of each file
            with open(file_path, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()

            # Check if this hash is already in the dictionary
            if file_hash in file_hashes:
                duplicates.append((file_path, file_hashes[file_hash]))
            else:
                file_hashes[file_hash] = file_path

    return duplicates

def main():
    start_time = time.time()
    directory = input("Enter the directory name: ")
    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    duplicates = find_duplicate_files(directory)

    if duplicates:
        with open("Log.txt", "w") as log_file:
            for duplicate in duplicates:
                log_file.write(f"Duplicate: {duplicate[0]} (Original: {duplicate[1]})\n")
                os.remove(duplicate[0])
        print("Duplicate files deleted. Log file created as 'Log.txt'.")
    else:
        print("No duplicate files found in the directory.")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time: {execution_time:.2f} seconds")

if __name__ == "__main__":
    main()