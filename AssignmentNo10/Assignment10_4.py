import os
import shutil
import sys

def copy_files_by_extension(source_dir, dest_dir, file_extension):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return

        # Create the destination directory if it doesn't exist
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        # Iterate through files in the source directory
        for filename in os.listdir(source_dir):
            if filename.endswith(file_extension):
                source_file_path = os.path.join(source_dir, filename)
                dest_file_path = os.path.join(dest_dir, filename)
                shutil.copy(source_file_path, dest_file_path)
                print(f"Copying {filename} to {dest_dir}")

        print("Copy operation completed successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryCopyExt.py <source_dir> <dest_dir> <file_extension>")
    else:
        source_dir = sys.argv[1]
        dest_dir = sys.argv[2]
        file_extension = sys.argv[3]
        copy_files_by_extension(source_dir, dest_dir, file_extension)

if __name__ == "__main__":
    main()