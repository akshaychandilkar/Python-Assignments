import os
import shutil
import sys

def copy_directory_contents(source_dir, target_dir):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy all files from source to target directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        target_file = os.path.join(target_dir, filename)
        if os.path.isfile(source_file):
            shutil.copy2(source_file, target_file)
            print(f"Copying '{source_file}' to '{target_file}'")

def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryCopy.py <source_directory> <target_directory>")
    else:
        source_directory = sys.argv[1]
        target_directory = sys.argv[2]
        copy_directory_contents(source_directory, target_directory)

if __name__ == "__main__":
    main()