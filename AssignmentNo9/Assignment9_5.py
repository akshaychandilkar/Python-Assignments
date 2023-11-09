def count_string_frequency(filename, target_string):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            frequency = content.count(target_string)
            return frequency
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return -1

def main():
    filename = input("Enter the file name : ")
    target_string = input("Enter the string to search : ")

    frequency = count_string_frequency(filename, target_string)

    if frequency != -1:
        print(f"The string '{target_string}' appears {frequency} times in {filename}.")

if __name__ == "__main__":
    main()