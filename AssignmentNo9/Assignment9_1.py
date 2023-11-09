import os 

def main():
    print("Enter the file Name : ")
    file_name = input()
    
    if os.path.exists(file_name):
        print("The file '{file_name}' exists in the current directory.")
    else:
        print("The file '{file_name}' does not exist in the current directory.")
    
if __name__ == "__main__":
    main()