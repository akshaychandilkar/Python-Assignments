import sys

def copy_file_content(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
            content = input_file.read()
            output_file.write(content)
        print(f"Contents from {input_filename} copied to {output_filename} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    if len(sys.argv) == 3:
        input_filename = sys.argv[1]
        output_filename = sys.argv[2]
    else:
        input_filename = input("Enter the file name: ")
        output_filename = input("Contents of the copy to file name: ")

        copy_file_content(input_filename, output_filename)

if __name__ == "__main__":
    main()