import os
import sys
import logging

# Function to list all files with a given extension in a directory
def list_files_with_extension(directory, extension):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory '{directory}' not found.")
        
        if not os.path.isdir(directory):
            raise NotADirectoryError(f"'{directory}' is not a directory.")
        
        with os.scandir(directory) as entries:
            files_with_extension = [entry.name for entry in entries if entry.is_file() and entry.name.endswith(extension)]
        
        return files_with_extension

    except FileNotFoundError as e:
        logging.error(str(e))
    except NotADirectoryError as e:
        logging.error(str(e))
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    return []
def main():
    if len(sys.argv) != 3:
        print("Usage: DirectoryFileSearch.py <directory> <extension>")
        sys.exit(1)

    directory = sys.argv[1]
    extension = sys.argv[2]
    
    # Configure logging to write messages to a log file
    log_filename = "automation.log"
    logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    
    logging.info(f"Searching for files with extension '{extension}' in directory '{directory}'")

    files_found = list_files_with_extension(directory, extension)

    if files_found:
        logging.info("Files found:")
        for file in files_found:
            logging.info(file)
    else:
        logging.info(f"No files found with extension '{extension}' in directory '{directory}'")

    print("Process complete. Check the log file for details.")

if __name__ == "__main__":
    main()