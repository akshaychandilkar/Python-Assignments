import os
import sys

def rename_files(directory, old_extension, new_extension):
    try:
        # Check if the specified directory exists
        if not os.path.exists(directory):
            print(f"The directory '{directory}' does not exist.")
            return

        # Iterate through files in the directory
        for filename in os.listdir(directory):
            if filename.endswith(old_extension):
                # Generate the new filename with the new extension
                new_filename = filename.replace(old_extension, new_extension)
                # Rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
                print(f"Renamed '{filename}' to '{new_filename}'")

        print("File renaming completed.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) != 4:
        print("Usage: DirectoryRename.py <directory> <old_extension> <new_extension>")
    else:
        directory = sys.argv[1]
        old_extension = sys.argv[2]
        new_extension = sys.argv[3]
        rename_files(directory, old_extension, new_extension)


if __name__ == "__main__":
    main()