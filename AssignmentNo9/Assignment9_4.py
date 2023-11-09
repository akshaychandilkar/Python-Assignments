def compare_files(file1, file2):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            if content1 == content2:
                print("Success: Both files contain the same contents.")
            else:
                print("Failure: Contents of the files are different.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

def main():
    file1 = input("Enter the file name: ")
    file2 = input("Contents of the Compare file name: ")

    compare_files(file1, file2)

if __name__ == "__main__":
    main()