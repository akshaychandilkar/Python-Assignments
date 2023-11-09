import threading

def count_small_chars(string):
    small_count = sum(1 for char in string if char.islower())
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print(f"Small Characters Count: {small_count}")

def count_capital_chars(string):
    capital_count = sum(1 for char in string if char.isupper()) 
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print(f"Capital Characters Count: {capital_count}")

def count_digits(string):
    digits_count = sum(1 for char in string if char.isdigit()) 
    print(f"Thread ID: {threading.get_ident()}, Thread Name: {threading.current_thread().name}")
    print(f"Digits Count: {digits_count}")

def main():
    input_string = input("Enter a string: ")

    small_thread = threading.Thread(target=count_small_chars, args=(input_string,))
    capital_thread = threading.Thread(target=count_capital_chars, args=(input_string,))
    digits_thread = threading.Thread(target=count_digits, args=(input_string,))

    small_thread.name = "small"
    capital_thread.name = "capital"
    digits_thread.name = "digits"

    small_thread.start()
    capital_thread.start()
    digits_thread.start()

    small_thread.join()
    capital_thread.join()
    digits_thread.join()

if __name__ == "__main__":
    main()
